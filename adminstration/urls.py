from django.urls import path, include
from rest_framework.routers import DefaultRouter
from adminstration import views

router = DefaultRouter()
router.register(r'secao',views.SecaoViewSet)
router.register(r'graducao',views.GraduacaoViewSet)
router.register(r'militar',views.MilitarViewSet)



urlpatterns = [
    path('', include(router.urls)),
]