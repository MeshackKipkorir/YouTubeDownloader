from django.shortcuts import render
from .forms import YouTubeLinks
import pytube,sys
from pytube import YouTube
# Create your views here.
def indexView(request):
    video_url = ""
    video_title = ""
    form = YouTubeLinks()
    if request.method == "POST":
        form = YouTubeLinks(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['link']
            form = YouTubeLinks(request.POST)
    #creating YouTube object from the link
    video = YouTube(video_url)
    #video title
    video_title = video.title
    #length of the video in seconds
    video_length = video.length
    #thumbail
    video_thumbnail = video.thumbnail_url
    #video id
    video_id = video.video_id

    context = {
        "type":"mp4",
        "form":form,
        "video_title":video_title,
        "video_length":video_length,
        "video_thumbail":video_thumbnail,
        "video_id":video_id
    }
    return render(request,'index.html',context)
