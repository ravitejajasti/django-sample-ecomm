from django.contrib import admin
from .models import Country, State, Company, Director, OrderType, Order
# Register your models here.

class CompanyInline(admin.TabularInline):
    model = Director.company.through

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'country',)
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

class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', )

# admin.site.unregister(CompanyAdmin)
# admin.site.unregister(DirectorAdmin)
# admin.site.unregister(CountryAdmin)
# admin.site.unregister(StateAdmin)


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderType, OrderTypeAdmin)