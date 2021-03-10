from rest_framework import viewsets
from rest_framework import permissions

from cosmetic_analyze.models import Profile, Cosmetic, Category, Ingredient, Comment
from cosmetic_analyze.serializers import ProfileSerializer, CosmeticSerializer, CategorySerializer, IngredientSerializer, CommentSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-joined_at')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class CosmeticViewSet(viewsets.ModelViewSet):
    queryset = Cosmetic.objects.all()
    serializer_class = CosmeticSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
