from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('employees', views.EmployeeGenericViewSet)

urlpatterns = router.urls
