from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "fullname",
            "phone",
            "address",
            "birthday",
            "created",
            "updated",
            "password",
        )
        read_only_fields = ("id", "created", "updated")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.fullname = validated_data.get("fullname", instance.fullname)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.address = validated_data.get("address", instance.address)
        instance.birthday = validated_data.get("birthday", instance.birthday)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance