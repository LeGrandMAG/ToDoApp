from django.contrib import admin
from .models import Memo
# Register your models here.

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created']
    list_filter = ['title', 'created']
    
