from rest_framework import serializers
from .models import Contestent, AmountReceived

class ContestentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Contestent
    fields =  '__all__'


class AmountReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmountReceived
        fields = ('contestent_id', 'jrnlno', 'amount', 'date')
        
