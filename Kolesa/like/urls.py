from rest_framework import routers
from like.views import LikeViewSet
router = routers.DefaultRouter()
router.register(r'', LikeViewSet , basename='likes')


urlpatterns = [

]

urlpatterns = router.urls