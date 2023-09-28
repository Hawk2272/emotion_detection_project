from django.shortcuts import render

# Create your views here.
def camera_input(request):
    return render(request, 'camera.html')

def analyze_emotion(request):
    return render(request, 'analyze_emotion.html')
