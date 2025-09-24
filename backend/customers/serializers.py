from rest_framework import serializers  # type: ignore

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""

    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "full_name"]

    def validate_email(self, value):
        """Custom email validation."""
        if value:
            value = value.lower().strip()
        return value

    def validate(self, data):
        """Custom validation for the serializer."""
        # Check for unique email if creating or updating email
        email = data.get("email")
        if email:
            customer_id = self.instance.id if self.instance else None
            if Customer.objects.filter(email=email).exclude(id=customer_id).exists():
                raise serializers.ValidationError(
                    {"email": "A customer with this email already exists."}
                )

        return data


class CustomerListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing customers."""

    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = ["id", "full_name", "email", "phone", "is_active"]
