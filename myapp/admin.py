from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publisher, Book, Member, Order

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Order)