from django.contrib import admin
from .models import Country, State, Company, Director
# Register your models here.

class CompanyInline(admin.TabularInline):
    model = Director.company.through

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'country',)
    inlines = [
        CompanyInline
    ]

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', )

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'din', 'pan')
    inlines = [
        CompanyInline
    ]



# admin.site.unregister(CompanyAdmin)
# admin.site.unregister(DirectorAdmin)
# admin.site.unregister(CountryAdmin)
# admin.site.unregister(StateAdmin)


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Company, CompanyAdmin)