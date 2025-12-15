from rest_framework.routers import DefaultRouter
from workflows.views import WorkflowViewSet

router = DefaultRouter()
router.register("workflows", WorkflowViewSet)

urlpatterns = router.urls
