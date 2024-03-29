from rest_framework import serializers

from .models import Product

from rest_framework.reverse import reverse

from .validators import validate_title, validate_title_no_hello, unique_product_title

from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only = True)
    # url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field='pk'
    )
    # email = serializers.EmailField(write_only=True)
    # custom validation over here
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model = Product
        fields = [
            'owner',
            'edit_url',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount',
            'public'
        ]

    def get_my_user_data(self,obj):
        return{
            "username": obj.user.username
        }
    
    """def get_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)"""
    

    """def create(self, validated_data):
        # return Product.objects.create(**validated_data)
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        # print(email,obj)
        return obj
    
    def update(self,instance, validated_data):
        email = validated_data.pop('email')
        # instance, title = validated_data.get('title')
        return super().update(instance, validated_data)"""
    

    def validate_title(self,value):
        request = self.context.get('request')
        user = request.user
        # look if title already exists
        qs = Product.objects.filter(user=user,title__iexact=value)
        if qs.exists(): # if title exists
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)

    def get_discount (self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()
       

