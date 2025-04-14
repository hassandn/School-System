from rest_framework import viewsets
from permissions import IsAdmin
from rest_framework.response import Response
from rest_framework.decorators import action
from django.apps import apps
from rest_framework import serializers


class AdminModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet to allow admin to manage any model in the system.
    """

    permission_classes = [IsAdmin]

    def get_queryset(self):
        model_name = self.kwargs.get("model_name")
        app_label = self.kwargs.get("app_label")
        model = apps.get_model(app_label, model_name)
        return model.objects.all()

    def get_serializer_class(self):
        model_name = self.kwargs.get("model_name")
        app_label = self.kwargs.get("app_label")
        self.model = apps.get_model(app_label, model_name)

        class DynamicModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = self.model
                fields = "__all__"

        return DynamicModelSerializer

    @action(detail=True, methods=["get"])
    def dynamic_action(self, request, *args, **kwargs):
        model_name = self.kwargs.get("model_name")
        app_label = self.kwargs.get("app_label")
        model = apps.get_model(app_label, model_name)
        queryset = model.objects.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
