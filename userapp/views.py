from django.shortcuts import render
from django.conf import settings
from .models import Flatmate
from .models import Room
from .models import ImageModel
from .models import SavedRooms
from .serializers import UserSignupSerializer, UserSerializer, MyModelSerializer, FlatmateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

import json
from datetime import datetime           

# Create your views here.

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = UserSignupSerializer(data=data)
    if serializer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(username=data['email'], first_name=data['firstname'], last_name=data['lastname'], email=data['email'], password=make_password(data['password']))
            user.save()
            Flatmate.objects.create(auth=user, name=data['firstname'], email=data['email'])
            Room.objects.create(auth=user, name=data['firstname'], email=data['email'])
            ImageModel.objects.create(auth=user, name=data['firstname'], email=data['email'])
            return Response({'message':'User Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'User Already Exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verifyEmail(request):
    data = request.data
    print(data)
    if User.objects.filter(username=data['email']).exists():
        user = User.objects.get(username=data['email'])
        return Response(UserSerializer(instance=user).data, status=status.HTTP_200_OK)
    else:
        return Response({'message':'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verifyPassword(request):
    data = request.data
    if User.objects.filter(username=data['email']).exists():
        user = User.objects.get(username=data['email'])
        if user.check_password(data['password']):
            return Response(UserSerializer(instance=user).data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid Password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def address(request):
    data = request.data
    email = data.get('email')
    address = data.get('address')
    try:
        flatmate = Flatmate.objects.get(email=email)
        flatmate.address = address
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def size(request):
    data = request.data
    email = data.get('email')
    size = data.get('size')
    try:
        room = Room.objects.get(email = email)
        room.size = size
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def kind(request):
    data = request.data
    email = data.get('email')
    kind = data.get('kind')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.kind = kind
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)@api_view(['POST'])

@api_view(['POST'])        
def roomsize(request):
    data = request.data
    email = data.get('email')
    roomsize = data.get('roomsize')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.roomsize = roomsize
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def rent(request):
    data = request.data
    email = data.get('email')
    rent = data.get('rent')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.rent = rent
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def available(request):
    data = request.data
    email = data.get('email')
    available = data.get('available')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.available = available
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def suitable(request):
    data = request.data
    email = data.get('email')
    suitable = data.get('suitable')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.suitable = suitable
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def flat(request):
    data = request.data
    email = data.get('email')
    flat = data.get('flat')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.flat = flat
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def provided(request):
    data = request.data
    email = data.get('email')
    provided = data.get('provided')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.provided = provided
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def roomIncluded(request):
    data = request.data
    email = data.get('email')
    roomIncluded = data.get('roomIncluded')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.roomIncluded = roomIncluded
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def image(request):
    data = request.data
    email = data.get('email')
    print(request.FILES.getlist('images'))
    print(email)
    try:
        image_instance = ImageModel.objects.get(email=email)
    except ObjectDoesNotExist:
        return Response("ImageModel instance does not exist", status=status.HTTP_400_BAD_REQUEST)
    try:
        for image in request.FILES.getlist('images'):

            print(image)
            # Save the image file to a location on your server
            image_instance.room_image_field.save(image.name, image)
            
            # Save the file path in the corresponding model instance
            image_instance.room_file_path = image_instance.room_image_field.url
            
            # Save the model instance to the database
            image_instance.save()
        return Response()

    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("Images uploaded successfully")

@api_view(['POST'])        
def description(request):
    data = request.data
    email = data.get('email')
    description = data.get('description')
    try:
        flatmate = Flatmate.objects.get(email = email)
        flatmate.description = description
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def getStart(request):
    data = request.data
    email = data.get('email')
    getStart = data.get('getStart')
    print(getStart)
    try:
        room = Room.objects.get(email = email)
        room.getStart = getStart
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def describeItem(request):
    data = request.data
    email = data.get('email')
    describeItem = data.get('describeItem')
    try:
        room = Room.objects.get(email = email)
        room.describeItem = describeItem
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def roomAddress(request):
    data = request.data
    email = data.get('email')
    address = data.get('address')
    try:
        room = Room.objects.get(email = email)
        room.address = address
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def living(request):
    data = request.data
    email = data.get('email')
    living = data.get('living')
    try:
        room = Room.objects.get(email = email)
        room.living = living
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def country(request):
    data = request.data
    email = data.get('email')
    country = data.get('country')
    try:
        room = Room.objects.get(email = email)
        room.country = country
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def myImage(request):
    data = request.data
    email = data.get('email')
    print(request.FILES.getlist('images'))
    print(email)
    try:
        image_instance = ImageModel.objects.get(email=email)
    except ObjectDoesNotExist:
        return Response("ImageModel instance does not exist", status=status.HTTP_400_BAD_REQUEST)
    try:
        for image in request.FILES.getlist('images'):

            print(image)
            # Save the image file to a location on your server
            image_instance.user_image_field.save(image.name, image)
            
            # Save the file path in the corresponding model instance
            image_instance.user_file_path = image_instance.user_image_field.url
            
            # Save the model instance to the database
            image_instance.save()
        return Response()

    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("Images uploaded successfully")

@api_view(['POST'])        
def preparePay(request):
    data = request.data
    email = data.get('email')
    preparePay = data.get('preparePay')
    try:
        room = Room.objects.get(email = email)
        room.preparePay = preparePay
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def kind(request):
    data = request.data
    email = data.get('email')
    kind = data.get('kind')
    try:
        room = Room.objects.get(email = email)
        room.kind = kind
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def room_size(request):
    data = request.data
    email = data.get('email')
    room_size = data.get('roomsize')
    try:
        room = Room.objects.get(email = email)
        room.room_size = room_size
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def move_date(request):
    data = request.data
    email = data.get('email')
    move_date = data.get('move_date')
    try:
        room = Room.objects.get(email = email)
        print('---------------')
        print(room)
        print(room.move_date)
        print(move_date)
        room.move_date = move_date
        room.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'message': 'Room Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def coming(request):
    data = request.data
    email = data.get('email')
    coming = data.get('coming')
    try:
        flatmate = Room.objects.get(email = email)
        flatmate.coming = coming
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def description_room(request):
    data = request.data
    email = data.get('email')
    description = data.get('description')
    try:
        flatmate = Room.objects.get(email = email)
        flatmate.description = description
        flatmate.save()
        return Response()
    except User.DoesNotExist:
        return Response({'message': 'User Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Flatmate.DoesNotExist:
        return Response({'message': 'Flatmate Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def profile(request):
    email = request.data.get('email')
    flatmate = Flatmate.objects.get(email=email)
    flatmate_serializer = FlatmateSerializer(flatmate)
    room = Room.objects.get(email=email)
    room_serializer = MyModelSerializer(room)
    if not room:
        return Response({'error': 'No room found'}, status=404)
    print(room_serializer)

    #get the string of getStart
    getStart_str = room_serializer.data.get('getStart')
    #convert string into json
    getStart_json = json.loads(getStart_str)
    print(getStart_json)
    name = getStart_json.get('name')
    print(name)
    gender = getStart_json.get('gender')
    birthday = getStart_json.get('birthday')
    birthday_object = datetime.fromisoformat(birthday[:-1])
    year = birthday_object.year
    age = 2023 - year
    #get the string of move_date
    move_date_str = room_serializer.data.get('move_date')
    #convert string into json
    move_date_json = json.loads(move_date_str)
    immediately = move_date_json.get('immediately')
    minimum_term = move_date_json.get('minimum_term')
    if(immediately == 'true'):
        move_date = "now"
    else:
        move_date = move_date_json.get('from_date')
    if(minimum_term == 'true'):
        stay_duration = "No plans"
    elif(minimum_term == False):
        stay_duration = move_date_json.get('minimum_month')

    #Address
    address = room_serializer.data.get('address')

    #Preparepay
    preparePay = room_serializer.data.get('preparePay')
    print(preparePay)
    #description
    description = room_serializer.data.get('description')

    #get the string of describeItem
    describeItem_str = room_serializer.data.get('describeItem')
    #convert string into json
    describeItem_json = json.loads(describeItem_str)
    describe = describeItem_json.get('describe')
    identify = describeItem_json.get('identify')
    accessibility = describeItem_json.get('accessibility')
    
    kind = room_serializer.data.get('kind')
    room_size = room_serializer.data.get('room_size')
    
    print('---------------------')
    print(kind,room_size)
    size_str = room_serializer.data.get('size')
    print(room_serializer.data.get('size'))
    size_json = json.loads(size_str)
    print(size_json)

    matching_rooms = SavedRooms.objects.filter(kind=kind, room_size = room_size,cost__lte = preparePay)
    matching_names = [{'name':room.name,'cost':room.cost} for room in matching_rooms]
    print(matching_names)
    return Response({
        'name': name, 
        'gender': gender, 
        'age': age,
        'move_date':move_date,
        'stay_duration':stay_duration,
        'preparePay':preparePay,
        'address':address,
        'description':description,
        'describe':describe,
        'identify':identify,
        'accessibility':accessibility,
        'kind':kind,
        'room_size':room_size,
        'size':size_json,
        'matching_names':matching_names
        },
        status=200)