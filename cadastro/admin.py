from django.contrib import admin

from cadastro.models import Marca, Cliente, Modelo, Veiculo

# Register your models here.
admin.site.register(Marca)

admin.site.register(Cliente)

admin.site.register(Modelo)

admin.site.register(Veiculo)
