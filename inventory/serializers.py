from rest_framework import serializers

from .models import Author ,Book ,Review ,Category


class AuthorSerializer(serializers.ModelSerializer): 
    class  Meta:
        model = Author 
        fields ='__all__'
class CategorySerializer(serializers.ModelSerializer): 
    class  Meta:
        model = Category 
        fields =['name','image']

class ReviewSerializer(serializers.ModelSerializer):
     class  Meta:
        model = Review 
        fields =['reviewer_name','content','created_at','rating']
class BookListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    author =serializers.StringRelatedField()

    class  Meta:
        model = Book 
        fields =['title','author','category','image','description','quantity','price']

class BookDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author =AuthorSerializer()
    review_book = ReviewSerializer(many=True )
    class  Meta:
        model = Book 
        fields =['title','author','category','image','description','review_book',
                 'quantity','price','publication_date']




