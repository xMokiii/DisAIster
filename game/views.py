from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import asyncio

from .services.deathByai import DeathByAI


def index(request):
    if request.GET.get('new_game'):
        request.session.clear()
        return HttpResponseRedirect(reverse('game:scenario'))
    return render(request, "game/index.html")


def scenario(request):
    existing_scenario = request.session.get("game_scenario")
    if existing_scenario and request.method == "GET":
        return render(request, "game/scenario.html", {"scenario": existing_scenario})
    
    if request.method == "POST":
        player_action = request.POST.get("player_action")
        if player_action and existing_scenario:
            request.session["player_action"] = player_action
            return HttpResponseRedirect(reverse("game:result"))
    
    is_ajax = request.headers.get("Accept") == "application/json"
    
    if not is_ajax:
        return render(request, "game/loading.html", {
            "message": "Génération de catastrophe en cours...",
            "check_url": reverse("game:scenario"),
        })
    
    try:
        game = DeathByAI()
        scenario = asyncio.run(game.generate_scenario())
        
        if not scenario or not scenario.strip():
            raise ValueError("Scénario vide")
        
        request.session.update({
            "game_scenario": scenario,
            "game_state": "waiting_for_action"
        })
        
        return JsonResponse({
            'ready': True,
            'redirect_url': reverse('game:scenario')
        })
        
    except Exception as e:
        return JsonResponse({
            'ready': False,
            'error': str(e)
        })


def result(request):
    player_action = request.session.get("player_action")
    scenario = request.session.get("game_scenario")
    
    existing_result = request.session.get("game_result")
    if existing_result and request.method == "GET":
        return render(request, "game/result.html", {
            "result": existing_result,
            "scenario": scenario, 
            "player_action": player_action
        })
    
    if not player_action or not scenario:
        return HttpResponseRedirect(reverse("game:index"))
    
    is_ajax = request.headers.get("Accept") == "application/json"
    
    if not is_ajax:
        return render(request, "game/loading.html", {
            "message": "L'IA décide de votre sort...",
            "check_url": reverse("game:result"),
        })
    
    try:
        game = DeathByAI()
        game.current_scenario = scenario
        result = asyncio.run(game.evaluate_survival(player_action))
        
        request.session.update({
            "game_result": result,
            "game_state": "finished"
        })
        
        return JsonResponse({
            'ready': True,
            'redirect_url': reverse('game:result')
        })
        
    except Exception as e:
        return JsonResponse({
            'ready': False,
            'error': str(e)
        })

