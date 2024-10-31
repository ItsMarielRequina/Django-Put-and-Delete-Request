from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Tag
from .serializers import TagSerializer
from rest_framework.response import Response
from rest_framework import status

class TagDetailView(APIView):
    def put(self, request, id):
        tag = get_object_or_404(Tag, id=id)
        serializer = TagSerializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        tag = get_object_or_404(Tag, id=id)
        tag.delete()
        return Response({"message": "Tag deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
