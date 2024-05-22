from rest_framework import serializers

from .models import Author ,Book ,Review ,Category


class AuthorSerializer(serializers.ModelSerializer): 
    books_count = serializers.SerializerMethodField()
    class  Meta:
        model = Author 
        fields =['name','age','biography' ,'books_count']

    def get_books_count(self,obj):
        return obj.book_author.count()
    
class CategorySerializer(serializers.ModelSerializer): 
    class  Meta:
        model = Category 
        fields =['name','image']

class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name =serializers.StringRelatedField()
    class  Meta:
        model = Review 
        fields =['reviewer_name','content','created_at','rating']
        
class BookListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    author =serializers.StringRelatedField()
    in_stock=serializers.SerializerMethodField()

    class  Meta:
        model = Book 
        fields =['title','author','category','image','description','quantity','price','in_stock']

    def get_in_stock(self,obj):
        if(obj.quantity > 0):
            return True
        else:
            return False

class BookDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author =AuthorSerializer()
    review_book = ReviewSerializer(many=True )
    class  Meta:
        model = Book 
        fields =['title','author','category','image','description','review_book',
                 'quantity','price','publication_date']




