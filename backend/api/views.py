from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer
from django.http import JsonResponse

# Create your api endpoints here 
def api_home_old(request, *args, **kwargs):
    print(request.GET) # url query params
    #print(request.POST)
    """body = request.body
    data = {}
    try :
        data = json.loads(body)
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers) # avoid request.headers is not json serializable error
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    return JsonResponse(data)"""
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        """
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price"""
        # easy way of serialization turning our model to json format
        data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
    # using JsonResponse : returns json by default
    return JsonResponse(data)
    # using HttpResponse : returns json by default
        # json_data_str = json.dumps(dict(data))
    # return HttpResponse(data, headers={"content-type":"application/json"})


#@api_view(["GET"])
def api_home_old_2(request, *args, **kwargs):
    """_summary_
        DRF API view
    """
    instance= Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=["id","title","price"])
        data = ProductSerializer(instance).data
    return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception= True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
