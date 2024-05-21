from rest_framework import serializers

from .models import Author ,Book ,Review ,Category


class AuthorSerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Author 
        fields ='__all__'

class BookListSerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Book 
        fields ='__all__'
class BookDetailSerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Book 
        fields ='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Review 
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Category 
        fields ='__all__'