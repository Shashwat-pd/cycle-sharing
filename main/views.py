from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cycle, User, Order, Request
from .utils import sort_by_distance
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse

import json
# Create your views here.
class CustomerHomeView(ListView):
    model = Cycle
    template_name = 'home.html'
    context_object_name = 'cycles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cycles = Cycle.objects.filter(available = True)
        # reverse cycles
        cycles = cycles[::-1]
        context['cycles'] = cycles
        return context

class RentalHomeView(ListView):
    model = Order
    template_name = 'rental_home.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cycles = Cycle.objects.filter(user = User.objects.get(id=1))
        requests = Request.objects.all()
        context['cycles'] = cycles
        context['requests'] = requests
        return context


@csrf_exempt
def add_cycle(request):
    if request.method == 'POST':
        print(request.FILES)
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        user = User.objects.get(id=1)
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        current_location = str(latitude) + ',' + str(longitude)

        cycle = Cycle(name=name, 
                    description=description,
                    rate=price,
                    user=user,
                    current_location=current_location,
                    image = image
                    )
        cycle.save()
        return redirect('home')
    else:
        return render(request, 'add_cycle.html')

@csrf_exempt
def request_cycle(request):
    print("---------")
    if request.method == 'POST':
        requests = Request.objects.all()
        active_requesting_users = [request.user for request in requests if request.status == 'in_progress']

        if request.POST.get('user') in active_requesting_users:
            return HttpResponse("You already have an active request")

        cycle_id = request.POST.get('cycle_id')
        cycle = Cycle.objects.get(id=cycle_id)
        estimated_time = request.POST.get('time')
        estimated_cost = cycle.rate * int(estimated_time)
        end_point_lat = request.POST.get('latitude')
        end_point_long = request.POST.get('longitude')
        end_point = str(end_point_lat) + ',' + str(end_point_long)
        user = User.objects.get(id=1)
        status = 'in_progress'
        cycle_request = Request(
                    cycle=cycle, 
                    user=user,
                    estimated_time=estimated_time,
                    estimated_price=estimated_cost,
                    end_point=end_point,
                    status=status)
        cycle_request.save()
        return redirect('home')
    else:
        return render(request, 'book_cycle.html')

@csrf_exempt
def approve(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        request = Request.objects.get(id=request_id)

        cycle = request.cycle
        cycle.available = False
        cycle.save()

        order = Order(cycle=cycle, user=request.user, starting_point=request.cycle.current_location, end_point=request.end_point, status='in_progress')
        order.save()
        request.status = 'approved'
        return redirect('rental_home')

def change_availability(request, id):
    cycle = Cycle.objects.get(id=id)
    cycle.available = not cycle.available
    cycle.save()
    return redirect('rental_home')

def delete_cycle(request, id):
    cycle = Cycle.objects.get(id=id)
    cycle.delete()
    return redirect('rental_home')



def booking(request, id):
    cycle = Cycle.objects.get(id=id)
    cycle_lat = cycle.current_location.split(',')[0]
    cycle_long = cycle.current_location.split(',')[1]
    return render(request, 'book_cycle.html', {'cycle': cycle, 'cycle_lat': cycle_lat, 'cycle_long': cycle_long})

class OrderListView(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ongoing_order = Order.objects.filter(user = User.objects.get(id=1), status='in_progress')
        completed_order = Order.objects.filter(user = User.objects.get(id=1), status='completed')
        cycle_requests = Request.objects.filter(user = User.objects.get(id=1))
        
        print('\n\n\n')
        print(ongoing_order)
        print('\n\n\n')

        context['ongoing_order'] = ongoing_order
        context['completed_order'] = completed_order

        context['cycle_request'] = cycle_requests[0]
        return context


def accept_request(request, id):
    request = Request.objects.get(id=id)

    cycle = request.cycle
    user = request.user
    status = 'in_progress'
    price = request.estimated_price
    starting_point = request.cycle.current_location
    end_point = request.end_point

    order = Order(cycle=cycle, user=user, status=status, price=price, starting_point=starting_point, end_point=end_point)
    order.save()

    request.delete()
    return redirect('rental_home')


def deny_request(request, id):
    request = Request.objects.get(id=id)
    request.cycle.available = True
    request.delete()
    return redirect('rental_home')

def cancel_request(request, id):
    request = Request.objects.get(id=id)
    request.cycle.available = True
    request.delete()
    return redirect('home')


def complete_order(request, id):
    order = Order.objects.get(id=id)
    order.status = 'completed'
    order.cycle.available = True
    cycle = order.cycle
    cycle.current_location = order.end_point
    order.save()
    return redirect('home')

def cancel_order(request, id):
    order = Order.objects.get(id=id)
    order.status = 'cancelled'
    order.cycle.available = True
    order.save()
    return redirect('home')



































































































































































































































































































