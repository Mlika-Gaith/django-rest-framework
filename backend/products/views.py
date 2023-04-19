from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
product_mixin_view = ProductMixinView.as_view()

class ProductListCreateAPIView(StaffEditorPermissionMixin,
                               UserQuerySetMixin,
                               generics.ListCreateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    #IsAuthenticatedOrReadOnly allows to read data but not to create it
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content) # very similar to form.save() and model.save()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        # print(request.user)
        # return super().get_queryset(*args, **kwargs)
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=request.user)



product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(StaffEditorPermissionMixin,
                           UserQuerySetMixin,
                           generics.RetrieveAPIView):
    #permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin,
                           UserQuerySetMixin,
                           generics.UpdateAPIView):
    #permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(StaffEditorPermissionMixin,
                            UserQuerySetMixin,
                            generics.DestroyAPIView):
    #permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()



class ProductListAPIView(generics.ListAPIView):
    """_summary_

    NOT GOING TO USE THIS METHOD !!!
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()

@api_view(["GET","POST"])
def product_alt_view(request,pk=None, *args, **kwargs):
    method =  request.method

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)


    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
                serializer.save(content=content)
                return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)