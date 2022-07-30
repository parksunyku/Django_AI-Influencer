from django.urls import path
from .views import UploadFeed, Profile, Main, UploadReply, ToggleLike, ToggleBookmark, FeedControl

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('reply', UploadReply.as_view()),
    path('like', ToggleLike.as_view()),
    path('bookmark', ToggleBookmark.as_view()),
    path('profile/<str:nickname>', Profile.as_view()),
    path('main', Main.as_view()),
    path('delete', FeedControl.as_view()),
    # path('delete', Feed.as_view()),
]
