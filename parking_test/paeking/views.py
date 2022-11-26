from django.shortcuts import render
from .models import Parking

def search(request):
    search_query = request.GET.get('search', '') # передаётся имя ввода (строка поиска)

# если значение search_query существует (в строку поиска введён текст) ищем в нужных полях введённый текст
    if search_query:
        parking = Parking.objects.filter(name__icontains=search_query)  # странное поведение sqLite не отключается чувствительность к регистру
    else:
        parking = Parking.objects.all()   # вывод всего списка (можно забить, но пусть будет)
    context = {'parking': parking}
    return render(request, 'search.html', context)
