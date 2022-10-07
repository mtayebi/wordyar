from django.shortcuts import render
from django.views import View


# Create view for home page
class home(View):

    def get(self, request):
        return render(request, "core/home.html")
