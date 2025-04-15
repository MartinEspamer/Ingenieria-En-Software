from django.urls import path
from . import views

app_name = "encuestas"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetalleView.as_view(), name="detalles"),
    path("<int:pk>/results/", views.ResultadosView.as_view(), name="resultados"),
    path("<int:pk>/votos/", views.voto, name="votos"),
]