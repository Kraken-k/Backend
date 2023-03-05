from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


def UserActivationView (request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        print(post_url)
        post_data = {'uid': uid, 'token': token}
        print(post_data)
        requests.post(post_url, data = post_data)
        return render(request,'add.html')
       
