from django.contrib import admin

from .models import Task, Department, TeamMember

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "starting_point", "goal", "satisfaction_rate")
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head", "stuff")

class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ("task",)

admin.site.register(Task, TaskAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(TeamMember, TeamAdmin)