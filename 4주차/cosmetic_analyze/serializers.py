from cosmetic_analyze.models import Profile, Cosmetic, Category, Ingredient, Comment
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    joined_at = serializers.ReadOnlyField(source='user.date_joined')
    #user = serializers.HyperlinkedRelatedField(many=True, view_name='profiles:Profile-detail', read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        #extra_kwargs = {'url': {'view_name': 'profiles:user-detail'}}

class CosmeticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cosmetic
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    #author = serializers.HyperlinkedRelatedField(many=True, view_name='comments:Comment-detail', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        #extra_kwargs = {'url': {'view_name': 'comments:user-detail'}}


