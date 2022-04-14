from django.db import models
from api.models.resource import Resource


class ProductManufacturer(Resource):
    """
    A manufacturer of products.
    """
    name: str = models.CharField(max_length=512)