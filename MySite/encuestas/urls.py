from django.urls import path
from . import views
urlpatterns = [
    # ej: /encuestas/
    path("", views.index, name="index"),
    # ex: /encuestas/5/
    path("<int:pregunta_id>/", views.detalle, name="detalles"),
    # ex: /encuestas/5/resultados/
    path("<int:pregunta_id>/results/", views.resultados, name="resultados"),
    # ex: /encuestas/5/votos/
    path("<int:pregunta_id>/votos/", views.voto, name="votos"),	
]
