from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


from .models import *
from .serializers import *
# from django.http import JsonResponse


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)
    # return JsonResponse(routes, safe=False)


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all().order_by('-updated_at')
    note_serializer = NoteSerializer(notes, many=True)
    return Response(note_serializer.data)


@api_view(['GET'])
def get_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note_serializer = NoteSerializer(note, many=False)
    return Response(note_serializer.data)


@api_view(['POST'])
def note_create(request):
    data = request.data
    note = Note.objects.create(body = data['body'])
    note_serializer = NoteSerializer(note, many=False)
    #print(f'data : {data}\ndata.POST: {request.POST}\nserializer: {note_serializer}') 
    return Response('note created')




@api_view(['PUT'])
def note_update(request, note_id):
    data = request.data
    note = get_object_or_404(Note, id=note_id)
    serializer = NoteSerializer(instance=note, data=data) # 1#50#52
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def note_delete(reques, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return Response('Note deleted')


