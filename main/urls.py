from django.urls import path

from . import views, utils

urlpatterns = [
    path('', views.CustomerHomeView.as_view(), name='home'),
    path('rental_home/', views.RentalHomeView.as_view(), name='rental_home'),
    path('add_cycle/', views.add_cycle, name='add_cycle'),
    path('request_cycle/', views.request_cycle, name='request_cycle'),
    path('approve/', views.approve, name='approve'),
    path('booking/<int:id>', views.booking, name='booking'),
    path('change_availability/<int:id>', views.change_availability, name='change_availability'),
    path('delete_cycle/<int:id>', views.delete_cycle, name='delete_cycle'),
    path('orders/', views.OrderListView.as_view(), name='orders'),

    path('accept_request/<int:id>', views.accept_request, name='accept_request'),
    path('deny_request/<int:id>', views.deny_request, name='deny_request'),
    path('cancel_request/<int:id>', views.cancel_request, name='cancel_request'),
    path('complete_order/<int:id>', views.complete_order, name='complete_order'),
    path('cancel_order/<int:id>', views.cancel_order, name='cancel_order'),

    #path('get_position/', utils.get_position, name='get_position')
]