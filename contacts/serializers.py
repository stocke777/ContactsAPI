from .models import Contact
from rest_framework.serializers import ModelSerializer


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'country_code', 'contact_picture', 'is_favorite']