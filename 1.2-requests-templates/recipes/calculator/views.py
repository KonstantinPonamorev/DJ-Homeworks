from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe_omlet_view(request):
    serving = int(request.GET.get('serving', 1))
    context = {}
    context['recipe'] = {}
    for item in DATA['omlet']:
        context['recipe'][item] = DATA['omlet'][item] * serving
    result = render(request, 'calculator/index.html', context)
    return HttpResponse(result)

def recipe_pasta_view(request):
    serving = int(request.GET.get('serving', 1))
    context = {}
    context['recipe'] = {}
    for item in DATA['pasta']:
        context['recipe'][item] = DATA['pasta'][item] * serving
    result = render(request, 'calculator/index.html', context)
    return HttpResponse(result)

def recipe_buter_view(request):
    serving = int(request.GET.get('serving', 1))
    context = {}
    context['recipe'] = {}
    for item in DATA['buter']:
        context['recipe'][item] = DATA['buter'][item] * serving
    result = render(request, 'calculator/index.html', context)
    return HttpResponse(result)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
