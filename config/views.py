from django.shortcuts import render
from rest_framework.views import APIView


def index(request):
    return render(request, 'index.html')


class Sub(APIView):
    def get(self, request):
        print("겟으로 호출")
        return render(request, 'jinstagram/main.html')

    def post(self, request):
        print("포스트로 호출")
        return render(request, 'jinstagram/main.html')
