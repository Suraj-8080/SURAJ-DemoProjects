from rest_framework.serializers import ModelSerializer
from .models import Address, User

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['address']

class UserSeralizer(ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email_name','phone_name','address']

    def create(self, validated_data):
        address = validated_data.pop('address')
        userObj = User.objects.create(**validated_data)
        Address.objects.create(**address,user=userObj)
        return userObj

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        address = validated_data.pop('address')
        addObj = Address.objects.filter(user = instance).update(**address)
        userObj = User.objects.filter(**validated_data).update(**validated_data)
        #Address.objects.update(**address,user=userObj)
        return super().update(instance, validated_data)