from django.contrib import admin

from histories.models import History

# Register your models here.
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
     model = History
