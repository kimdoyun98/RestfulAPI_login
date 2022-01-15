# 응답을 받고 로직을 제공하는 곳 //view라고 하지만 MVC 모델에서 Control 역할
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Addresses
from .serializer import AddressesSerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate


# Create your views here.
@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def address(request, pk):
    obj = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def login(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_name = data['name']
        obj = Addresses.objects.get(name=search_name)
        if data['phone_number'] == obj.phone_number:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

@csrf_exempt
def app_login(request):

    if request.method == 'POST':
        print("request log : " + str(request.body))
        id = request.POST.get('userid','')
        pw = request.POST.get('userpw', '')
        print("id : " + id + " pw : " + pw)

        result = authenticate(username=id, password=pw)

        if result :
            return JsonResponse({'code': '0000','msg': '로그인 성공입니다.'} ,status=200)
        else:
            return JsonResponse({'code': '1001','msg': '로그인 실패입니다.'} ,status=200)


    return render(request, 'html 주소')

