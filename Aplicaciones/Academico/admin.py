from django.contrib import admin
#importamos el models de nuestro proyecto, osea nuestro curso # 
from .models import Curso

# Register your models here.
admin.site.register(Curso)