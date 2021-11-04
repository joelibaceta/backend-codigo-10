from django.contrib import admin

from core.models import Task

from core.models import Category

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'finished')
    list_filter = ('due_date', 'finished')
    search_fields = ['title']
    ordering = ('due_date',)
    fields = ('title', 'description', 'category', ('due_date', 'finished'), 'attachtment')

admin.site.register(Task, TaskAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)