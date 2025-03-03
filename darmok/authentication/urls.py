from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    # post views
    path('', views.landing_page, name='landing_page'),
    # path(
    #     '<int:year>/<int:month>/<int:day>/<slug:post>/',
    #     views.post_detail,
    #     name='post_detail'
    # ),
]