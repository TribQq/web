from django.contrib import admin
from .models import *


class AdminSortIndex(admin.ModelAdmin):
   ordering = ['sort_index']

admin.site.register(PortfolioProjectCard, AdminSortIndex)
admin.site.register(PortfolioSkillCard, AdminSortIndex)
