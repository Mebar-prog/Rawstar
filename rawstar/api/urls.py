from django.urls import path,include
from .views import AmountReceivedViewSet, ContestentGetCreate, ContestentUpdateDelete, ImageView, records_view
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'amountreceived', AmountReceivedViewSet)
urlpatterns = [
    path('', ContestentGetCreate.as_view()),
    path('<int:pk>',ContestentUpdateDelete.as_view()),
    path('singers/<str:image_name>', ImageView.as_view(), name='image'),
    # path('votes/', AmountReceivedViewSet.as_view(), name='amount_received'),
    path('', include(router.urls)),
    path('records/', records_view, name='records'),

]
