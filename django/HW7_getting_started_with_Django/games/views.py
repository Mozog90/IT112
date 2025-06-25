from django.shortcuts import render, get_object_or_404
from .models import Game
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    user_name = request.GET.get('user_name', '')
    return render(request, 'games/home.html', {'user_name': user_name})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'games/game_detail.html', {'game': game})

def api_game_list(request):
    games = Game.objects.all().values()
    return JsonResponse(list(games), safe=False, content_type="application/json")

def api_game_detail(request):
    game_id = request.GET.get('id')
    try:
        game = Game.objects.values().get(id=game_id)
        return JsonResponse(game, content_type="application/json")
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, content_type="application/json")

@csrf_exempt
def api_game_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            game = Game.objects.create(
                title=data['title'],
                genre=data['genre'],
                release_year=data['release_year'],
                rating=data['rating']
            )
            return JsonResponse({'success': True, 'id': game.id}, content_type="application/json")
        except Exception as e:
            return JsonResponse({'error': str(e)}, content_type="application/json")
    return JsonResponse({'error': 'Invalid request method'}, content_type="application/json")
