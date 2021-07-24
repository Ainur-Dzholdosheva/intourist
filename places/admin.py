from django.contrib import admin
from .models import Place, FeedBack

admin.site.register(Place)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', 'place', 'user', 'checked']
    list_editable = ['checked']
    list_filter = ['checked']
    search_fields = ['text', 'place__name', 'place__description', 'place__location']

    fields = ['user', 'place', 'text']
    readonly_fields = ['place', 'text']

admin.site.register(FeedBack, FeedbackAdmin)
