from django.conf.urls import url, include
from skipass.views import get_all

urlpatterns = [
    url(r'^api/get/$', get_all),

]
