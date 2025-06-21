from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserModelSerializer(serializers.ModelSerializer):
    password1= serializers.CharField(write_only=True, required = True, validators = [validate_password])
    password2 = serializers.CharField(write_only=True,required = True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError({"error" : "passwords did not match!"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data["username"], email = validated_data["email"])
        user.set_password(validated_data["password1"])
        user.save()
        return user
    

