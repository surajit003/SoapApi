from django.conf.urls import url
from . import views

app_name = "playground"

urlpatterns = [
    url(
        r"^number-conversion/(?P<number>[\w-]+)/$",
        views.send_request_for_number_conversion,
        name="send_request_for_number_conversion",
    ),
    url(
        r"^currencies/(?P<iso_code>[\w-]+)/$",
        views.send_request_for_all_currencies,
        name="send_request_for_all_currencies",
    ),
]
