from rest_framework import serializers
from .models import ModalData


class ModalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalData
        fields = "__all__"
        # fields = (
        #     "report_name",
        #     "format",
        #     "email",
        #     "schedule",
        #     "time",
        #     "date",)

