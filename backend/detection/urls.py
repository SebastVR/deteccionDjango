# from django.urls import path
# from detection import views

# app_name = "detection"

# urlpatterns = [
#     path(
#         "projects/<int:project_id>/detections/",
#         views.DetectionUploadAPIView.as_view(),
#         name="detection-upload",
#     ),
#     path(
#         "projects/<int:pk>/",
#         views.ProjectDetailAPIView.as_view(),
#         name="project-detail",
#     ),
#     path(
#         "detections/<int:pk>/",
#         views.DetectionDetailAPIView.as_view(),
#         name="detection-detail",
#     ),
#     path(
#         "projects/",
#         views.ProjectListCreateAPIView.as_view(),
#         name="project-list-create",
#     ),
#     path(
#         "detections/",
#         views.DetectionListCreateAPIView.as_view(),
#         name="detection-list-create",
#     ),
#     path(
#         "projects/<int:project_id>/detections/upload/",
#         views.DetectionUploadAPIView.as_view(),
#         name="detection-upload",
#     ),
# ]
