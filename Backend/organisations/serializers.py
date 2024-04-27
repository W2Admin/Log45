from rest_framework import serializers
from .models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['id', 'name', 'description']

    def validate_name(self, value):
        # Example custom validation: Ensure that the name is not empty
        if not value:
            raise serializers.ValidationError("Name cannot be empty")
        return value