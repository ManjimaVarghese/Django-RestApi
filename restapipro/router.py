from restapiapp.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('User',UserViewset)