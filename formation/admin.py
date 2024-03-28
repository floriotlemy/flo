from django.contrib import admin
from .models import Categorie, Formation

# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Formation)
class FormationModel(admin.ModelAdmin):
    list_display = ('titre','categorie','duree','tarif')
    list_filter = ['categorie']
    list_per_page = 10
    search_fields = ['titre','categorie','duree','tarif']