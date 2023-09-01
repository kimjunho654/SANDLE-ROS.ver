import rospy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from std_msgs.msg import Bool

# Create your views here.
def main(request):
    return render(request,'main.html')
def goods(request):
    try:
        with open('open.py', 'r') as file:
            code = file.read()
            exec(code)
        return render(request, 'goods.html')
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def complete(request):
    try:
        with open('go.py', 'r') as file:
            code = file.read()
            exec(code)
        return render(request, 'complete.html')
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")