from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

admin.site.register(User, UserAdmin)
admin.site.site_header = "Gestão Datadomus "
admin.site.site_title = "Gestão Datadomus"
admin.site.index_title = "Bem vindo à Gestão Datadomus!"