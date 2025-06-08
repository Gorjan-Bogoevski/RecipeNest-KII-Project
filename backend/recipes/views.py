from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Recipe
from bson import ObjectId
from bson.errors import InvalidId

from bson import ObjectId  # ✅ важно
from bson.json_util import dumps

class RecipeListCreateView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        recipe_list = []
        for r in recipes:
            doc = r.to_mongo().to_dict()
            doc["_id"] = str(doc["_id"])  # ✅ конвертира ObjectId во стринг
            recipe_list.append(doc)
        return Response(recipe_list)

    def post(self, request):
        try:
            data = request.data
            print("📥 Incoming data:", data)

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
            print("❌ Error:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetailView(APIView):
    def get(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=ObjectId(recipe_id))
            data = recipe.to_mongo().to_dict()
            data["_id"] = str(data["_id"])
            return Response(data)
        except (Recipe.DoesNotExist, InvalidId):
            return Response({"error": "Recipe not found"}, status=404)