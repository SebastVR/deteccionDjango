# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.views import APIView
# from .models import Project, Detection
# from .serializers import ProjectSerializer, DetectionSerializer
# from utils.detection import process_image
# from django.shortcuts import get_object_or_404
# import logging

# logger = logging.getLogger(__name__)


# class DetectionUploadAPIView(APIView):
#     def post(self, request, project_id):
#         project = get_object_or_404(Project, id=project_id)
#         file = request.FILES.get("file")
#         if not file:
#             return Response(
#                 {"detail": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             detection = process_image(file, project)
#             serializer = DetectionSerializer(detection)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             logger.error(f"Error during detection upload: {e}")
#             return Response(
#                 {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )


# class ProjectListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


# class ProjectDetailAPIView(generics.RetrieveAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


# class DetectionListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Detection.objects.all()
#     serializer_class = DetectionSerializer


# class DetectionDetailAPIView(generics.RetrieveAPIView):
#     queryset = Detection.objects.all()
#     serializer_class = DetectionSerializer


# class DetectionUploadAPIView(APIView):
#     def post(self, request, project_id):
#         project = get_object_or_404(Project, id=project_id)
#         file = request.FILES["file"]
#         detection = process_image(file, project)
#         serializer = DetectionSerializer(detection)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
