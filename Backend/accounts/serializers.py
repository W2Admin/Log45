from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from organisations.models import Organisation
from rest_framework import serializers

class UserCreateSerializer(DjoserUserCreateSerializer):
    org_name = serializers.CharField(max_length=200, required=True)
    org_description = serializers.CharField(required=True)

    class Meta(DjoserUserCreateSerializer.Meta):
        fields = ['id', 'name', 'email', 'password', 'org_name', 'org_description']

    def create(self, validated_data):
        org_name = validated_data.pop('org_name')
        org_description = validated_data.pop('org_description')

        # Create the organization
        organisation = Organisation.objects.create(name=org_name, description=org_description)

        # Assign the organisation to the user
        validated_data['organisation'] = organisation

        return super().create(validated_data)
