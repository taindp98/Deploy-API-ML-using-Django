from django.urls import path
from .views import *

urlpatterns = [
    ## edit the prefix /pred to indicate another API
    path('pred', Prediction.as_view(), name = 'prediction'),
]