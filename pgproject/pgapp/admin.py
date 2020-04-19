from django.contrib import admin
from .models import Details,Orders

# Register your models here.


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    # ordering = ('price',)
    search_fields = ('title',)
admin.site.register(Details,DetailsAdmin)
admin.site.register(Orders)