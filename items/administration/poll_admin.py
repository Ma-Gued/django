from django.contrib import admin
from items.models import Poll

# Administration du modèle Poll
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'category') 
    fields = ('question', 'category')

