from django.shortcuts import render
from .models import Author, Store, Publisher, Book
from django.views.generic import ListView
from django.http import HttpResponse
from django.views import View


def my_views(request):
    if request.method == "GET":
        author = Author.objects.all()
        context = {"author": author}
        return render(request, "aggregation/book_list.html", context=context)
    else:
        return HttpResponse("<h1>Error Find 404</h1>")


class MyView(View):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        return HttpResponse("""<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>Скрипты</title>
  <style>
   #msg { 
    display: none;
    position: absolute;
    width: 280px;
    top: 200px;
    left: 50%;
    margin-left: -150px; 
    background: #fc0;
    padding: 10px;
   }
  </style>
  <script>
   function textMsg(msg) {
    document.getElementById('text').innerHTML = msg;
    document.getElementById('msg').style.display = 'block';
   }
   function closeMsg() {
    document.getElementById('msg').style.display = 'none';
   }
  </script>
 </head>
 <body>
  <div id="msg">
   <div id="text"></div>
   <div id="close"><a href="javascript:closeMsg()">[Закрыть]</a></div>
  </div>
  <p>Нажмите на <a href="#" onclick="textMsg('Спасибо, что нажали на ссылку!')">  
    ссылку для открытия сообщения</a>.</p>
 </body>
</html>""")


class BookList(ListView):
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("pubdate")
        response = HttpResponse(
            headers={'Last-Modified': last_book.pubdate.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response
# Create your views here.
