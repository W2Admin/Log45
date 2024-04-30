from rest_framework import serializers
from .models import Organisation, Industry

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty")
        return value
    

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'