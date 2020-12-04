from rest_framework import serializers
from .models import Clasa

class ClasaSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Clasa
        fields = ( 'id', 'cod' , 'profesor' , 'created_at' )
