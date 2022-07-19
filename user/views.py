from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # TODO 회원가입
        pass


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # TODO 로그인
        pass
