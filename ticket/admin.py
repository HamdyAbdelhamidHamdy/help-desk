from django.contrib import admin

from ticket.models import Ticket

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ['name','email','status','priority']
    list_editable = ['status']


admin.site.register(Ticket, TicketAdmin)