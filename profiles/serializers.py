from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  is_owner = serializers.SerializerMethodField()
  following_id = serializers.SerializerMethodField()
  products_count = serializers.ReadOnlyField()
  followers_count = serializers.ReadOnlyField()
  following_count = serializers.ReadOnlyField()

  def get_is_owner(self, obj):
    request = self.context['request']
    return request.user == obj.owner

  class Meta:
    model = Profile
    fields = [
    'id', 'owner', 'created_at', 'updated_at', 'name',
    'content', 'image', 'is_owner', 'following_id', 
    'products_count', 'followers_count', 'following_count'
    ]