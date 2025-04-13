from django.urls import path
from . import views

app_name = "encuestas"
urlpatterns = [
    # ej: /encuestas/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /encuestas/5/
    path("<int:pk>/", views.DetalleView.as_view(), name="detalles"),
    # ex: /encuestas/5/resultados/
    path("<int:pk>/results/", views.ResultadosView.as_view(), name="resultados"),
    # ex: /encuestas/5/votos/
    path("<int:pk>/votos/", views.voto, name="votos"),	
]
