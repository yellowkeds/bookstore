from django.contrib import admin
from .models import Registration, Contact

# Register your models here.
class Information(admin.StackedInline):
    model = Contact
    extra = 1

class InformationAdmin(admin.ModelAdmin):
    inlines = [Information]

admin.site.register(Registration, InformationAdmin)