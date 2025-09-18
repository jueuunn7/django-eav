from rest_framework.routers import DefaultRouter

from eav.views import BoardViewSets


router = DefaultRouter(trailing_slash=False)
router.register("board", BoardViewSets, basename="blog")
