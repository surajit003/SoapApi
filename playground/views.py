from django.shortcuts import render
from django.http import HttpResponse
from .utils import (
    create_request_body_for_number_conversion,
    create_request_body_for_all_currencies,
)
import requests
from bs4 import BeautifulSoup
import lxml

# Create your views here.
def send_request_for_number_conversion(request, number):
    if request.method == "GET":
        response = requests.post(
            "https://www.dataaccess.com/webservicesserver/NumberConversion.wso",
            headers={"Content-Type": "text/xml; charset=utf-8"},
            data=create_request_body_for_number_conversion(number),
        )
        return HttpResponse(response.content)


def send_request_for_all_currencies(request, iso_code):
    if request.method == "GET":
        response = requests.post(
            "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso",
            headers={"Content-Type": "text/xml; charset=utf-8"},
            data=create_request_body_for_all_currencies(),
        )
        content = BeautifulSoup(response.content, "xml")
        currency_data = content.find_all("m:tCurrency")
        for d in currency_data:
            code = d.find("m:sISOCode").string
            if code == iso_code.upper():
                return HttpResponse(d.find("m:sName").string)
        else:
            return HttpResponse("No currency name with that ISO CODE")
