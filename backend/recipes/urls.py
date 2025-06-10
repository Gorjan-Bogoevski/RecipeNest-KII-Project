from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<str:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]

