from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view()),
    path('recipes/<str:recipe_id>/', RecipeDetailView.as_view()),  # 👈 додај го ова
]