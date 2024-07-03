from django.shortcuts import render, get_object_or_404
from .models import CarsModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def cars(request):
    all_cars = CarsModel.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'all_cars': paged_cars,
    }
    return render(request, 'cars\cars.html', data)

def car_details(request, id):
    single_car = get_object_or_404(CarsModel, pk=id)
    print(single_car.car_title, single_car.city)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars\car_details.html', data)