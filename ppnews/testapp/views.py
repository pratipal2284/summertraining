from django.shortcuts import render
def index(request):
    return render(request,"testapp/index.html")

def politics(request):
    head_msg="Politics info"
    msg1="Narendra modi won 2019 election"
    msg2="Narendra modi won 301 seats"
    msg3="Mayawati & Akhilesh is over"
    data={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,"testapp/news.html",context=data)
# Create your views here.

def sports(request):
    return render(request,"testapp/news.html")

def movies(request):
    return render(request,"testapp/news.html")
