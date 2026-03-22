from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Keyword, Flag
from .serializers import KeywordSerializer, FlagSerializer
from .services import run_scan
from django.utils import timezone
from .mock_data import load_mock_data
from django.shortcuts import get_object_or_404


class KeywordCreateView(APIView):
    def post(self, request):
        serializer = KeywordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ScanView(APIView):
    def post(self, request):
        load_mock_data()
        run_scan()
        return Response({"message": "Scan completed"})


class FlagListView(APIView):
    def get(self, request):
        flags = Flag.objects.all()
        serializer = FlagSerializer(flags, many=True)
        return Response(serializer.data)


class FlagUpdateView(APIView):
    def patch(self, request, pk):
        flag = get_object_or_404(Flag, pk=pk)

        status_value = request.data.get('status')

        if status_value not in ['pending', 'relevant', 'irrelevant']:
            return Response({"error": "Invalid status"}, status=400)

        flag.status = status_value
        flag.last_reviewed_at = timezone.now()
        flag.save()

        return Response({"message": "Updated"})