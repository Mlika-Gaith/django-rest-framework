from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product


# this is to specify which fields do you want to be searched and accessible by Algolia
@register(Product)
class ProductIndex(AlgoliaIndex):
    # only search public records
    should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'publish_timestamp',
        'public'
    ]
    tags = 'get_tags_list'