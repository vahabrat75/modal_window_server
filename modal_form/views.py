from rest_framework import generics
from modal_form.serializers import ModalDataSerializer


class SaveModalData(generics.CreateAPIView):

    serializer_class = ModalDataSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

# Create your views here.
