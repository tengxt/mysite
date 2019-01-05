from django.contrib import admin
from .models import Userip, DayNumber, VisitNumber

# Register your models here.
@admin.register(Userip)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'count')

@admin.register(DayNumber)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'day')

@admin.register(VisitNumber)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')
