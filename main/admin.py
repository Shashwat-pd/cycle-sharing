from django.contrib import admin
from .models import Cycle, User, Order, UserCycle, Request
# Register your models here.
admin.site.register(Cycle)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Request)
admin.site.register(UserCycle)