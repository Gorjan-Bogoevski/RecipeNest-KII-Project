from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from bson.errors import InvalidId
from .models import Recipe

class RecipeListCreateView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        recipe_list = []
        for r in recipes:
            doc = r.to_mongo().to_dict()
            doc["_id"] = str(doc["_id"])
            recipe_list.append(doc)
        return Response(recipe_list)

    def post(self, request):
        try:
            data = request.data
            recipe = Recipe(
                title=data["title"],
                cook_time=int(data["cook_time"]),
                ingredients=data.get("ingredients", []),
                steps=data.get("steps", []),
                tags=data.get("tags", []),
                image_url=data.get("image_url", "")
            )
            recipe.save()
            return Response({"message": "Recipe created"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetailView(APIView):
    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(id=ObjectId(pk))
            data = recipe.to_mongo().to_dict()
            data["_id"] = str(data["_id"])
            return Response(data)
        except (Recipe.DoesNotExist, InvalidId):
            return Response({"error": "Recipe not found"}, status=404)

    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(id=ObjectId(pk))
            data = request.data
            recipe.title = data.get("title", recipe.title)
            recipe.cook_time = int(data.get("cook_time", recipe.cook_time))
            recipe.ingredients = data.get("ingredients", recipe.ingredients)
            recipe.steps = data.get("steps", recipe.steps)
            recipe.tags = data.get("tags", recipe.tags)
            recipe.image_url = data.get("image_url", recipe.image_url)
            recipe.save()
            return Response({"message": "Recipe updated"})
        except (Recipe.DoesNotExist, InvalidId) as e:
            return Response({"error": "Recipe not found"}, status=404)

    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(id=ObjectId(pk))
            recipe.delete()
            return Response({"message": "Recipe deleted"})
        except (Recipe.DoesNotExist, InvalidId):
            return Response({"error": "Recipe not found"}, status=404)
