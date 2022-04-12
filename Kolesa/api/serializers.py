
from rest_framework.serializers import ModelSerializer
from api.models import City, Brand, Models, Comment

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarCreateSerializer(ModelSerializer):
    class Meta:
        model = Models
        fields = '__all__'

class CarShortSerializer(ModelSerializer):
    class Meta:
        model = Models
        fields = ('id', 'title', 'transmission', 'steering', 'color', 'drive_unit', 'cleared_RK',
                  'description', 'contacts', 'year')


class CarSerializer(ModelSerializer):
    city = CitySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    class Meta(CarShortSerializer.Meta):
        print("serializer 1")
        fields = CarShortSerializer.Meta.fields + ('city', 'brand') #+  ('brand','title')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"