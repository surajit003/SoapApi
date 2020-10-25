from django.shortcuts import render
from django.http import HttpResponse
from .utils import create_request_body_for_number_conversion
import requests
# Create your views here.
def send_request_for_number_conversion(request,number):
    if request.method =='GET':
        response = requests.post('https://www.dataaccess.com/webservicesserver/NumberConversion.wso',
                                 headers ={"Content-Type":"text/xml; charset=utf-8"},
                                 data=create_request_body_for_number_conversion(number))
        return HttpResponse(response.content)

