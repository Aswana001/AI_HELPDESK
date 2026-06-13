from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = [
            "created_by",
            "category",
            "status",
            "ai_suggestion",
            "created_at",
            "updated_at"
        ]

    def validate_title(self, value):
        """Ensure title is not empty"""
        if not value or len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters"
            )
        return value

    def validate_description(self, value):
        """Ensure description is valid"""
        if not value or len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Description must be at least 5 characters"
            )
        if len(value) > 5000:
            raise serializers.ValidationError(
                "Description cannot exceed 5000 characters"
            )
        return value


class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["status"]

    def validate_status(self, value):
        """Validate status is valid choice"""
        valid_statuses = ["open", "in_progress", "resolved"]
        if value not in valid_statuses:
            raise serializers.ValidationError(
                f"Status must be one of: {', '.join(valid_statuses)}"
            )
        return value