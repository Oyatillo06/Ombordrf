from rest_framework.serializers import ModelSerializer

from .models import *


class ProductSer(ModelSerializer):
    class Meta:
        model=Product
        fields=["id","nom","brend_nomi","kelgan_narx","sotuvdagi_narx","miqdor","ombor"]


class StatsSer(ModelSerializer):
    class Meta:
        model=Stats
        fields=["id","client","product","sanasi","miqdor","umumiy_summa","tolandi","nasiya","ombor"]


class ClientSer(ModelSerializer):
    class Meta:
        model=Client
        fields=["id","ism","tel","dokon_nomi","joylashuv","qarz","ombor"]


class OmborSer(ModelSerializer):
    class Meta:
        model=Ombor
        fields=["id","ism","dokon_nomi","joylashuv","turi","tel","user"]
