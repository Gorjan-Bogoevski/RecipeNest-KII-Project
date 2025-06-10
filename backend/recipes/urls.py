from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path('api/recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('api/recipes/<str:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]