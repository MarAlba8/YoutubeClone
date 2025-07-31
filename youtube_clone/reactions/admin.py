from django.contrib import admin

from reactions.models import Reaction

# Register your models here.
@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
     model = Reaction
