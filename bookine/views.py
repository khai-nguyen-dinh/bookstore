import uuid

from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from bookine.serializers import *


# decorator pattern
def signin_decorator(position):
    def decorator(function):
        def wrapper(request):
            if request.method == 'POST':
                data = JSONParser().parse(request)
                serializer = UserSigninSerializer(data=data)
                if serializer.is_valid():
                    _usr = User.objects.filter(username=data.get('username'),
                                               password=data.get('password'), manager=position).first()
                    if _usr:
                        return function(JsonResponse({'id': _usr.id}, status=201))
                    else:
                        function(JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND))
                return function(JsonResponse(serializer.errors, status=400))

            return function(JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND))

        return wrapper

    return decorator


# for user
@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@signin_decorator(0)
def sign_in_user(request):
    return request


@csrf_exempt
def get_all_book(request):
    if request.method == 'get(':
        list_book = Book.objects.all()
        serializer = BookSerializer(data=list_book, many=True)
        serializer.is_valid(raise_exception=False)
        return JsonResponse(serializer.data, safe=False)
    # return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


def detail_book(request, id):
    if request.method == 'GET':
        book = Book.objects.filter(id=id).first()
        serializer = BookSerializer(book, many=False)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def add_cart(request):
    '''
    method POST user_id,book_id, count
    :param request: 
    :return: 
    '''
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data.get('user_id')
            book_id = data.get('book_id')
            count = data.get('count')

            user = User.objects.filter(id=user_id).first()
            book = Book.objects.filter(id=book_id).first()
            cart = Cart.objects.filter(user=user, is_payment=0).first()
            if cart:
                cart = Cart.objects.filter(user=user, book=book).first()
                if cart:
                    cart.count = cart.count + int(count)
                else:
                    cart = Cart(user=user, book=book, count=count, no=cart.no)
                cart.save()
            else:
                cart = Cart(user=user, book=book, count=count, no=uuid.uuid1().hex)
                cart.save()
            return JsonResponse({'messages': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def get_cart(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_id = data.get('user_id')
        user = User.objects.filter(id=user_id).first()
        cart = Cart.objects.filter(user=user, is_payment=0)
        serializer = CartSerializer(cart, many=True)
        return JsonResponse(serializer.data, safe=False)



@csrf_exempt
@signin_decorator(1)
def sign_in_staff(request):
    return request


@csrf_exempt
@signin_decorator(2)
def sign_in_manage(request):
    return request
