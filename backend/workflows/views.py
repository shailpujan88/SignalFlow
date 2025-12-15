from rest_framework.viewsets import ModelViewSet
from .models import Workflow
from .serializers import WorkflowSerializer

class WorkflowViewSet(ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer
