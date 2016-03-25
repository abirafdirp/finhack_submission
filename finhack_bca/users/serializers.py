from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


class UserSerializer(UserDetailsSerializer):
    name = serializers.CharField(max_length=255, allow_blank=True)
    type = serializers.ReadOnlyField()

    balance = serializers.ReadOnlyField()

    # BCA's mandatory fields, email is used as primary id bca
    date_of_birth = serializers.DateField()
    mobile_number = serializers.CharField(max_length=30)
    email = serializers.EmailField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'name',
            'type',
            'balance',
            'date_of_birth',
            'mobile_number',
            'email'
        )

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.date_of_birth = validated_data['date_of_birth']
        instance.mobile_number = validated_data['mobile_number']
        instance.email = validated_data['email']

        instance = super(UserSerializer, self).update(instance, validated_data)

        return instance
