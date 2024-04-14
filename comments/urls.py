from django.urls import path
from comments import views

urlpatterns = [
    path('<int:pk>/<str:action>/', views.CommentLikeDislikeView.as_view(), name="comment_action")
]