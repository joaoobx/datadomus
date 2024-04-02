from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from example.serializer import ItemSerializer

from .models import Example


class ExampleListView(ListView):
    model = Example

def listAll(request):
    model = Example
    serializer = ItemSerializer(model.objects.all(), many =True)
    return JsonResponse(serializer.data, safe =False)

class ExampleCreateView(CreateView):
    model = Example
    fields = ["title", "deadline"]
    success_url = reverse_lazy("example_list")

class ExampleUpdateView(UpdateView):
    model = Example
    fields = ["title", "deadline"]
    success_url = reverse_lazy("example_list")

class ExampleDeleteView(DeleteView):
    model = Example
    success_url = reverse_lazy("example_list")

class ExampleCompleteView(View):
    def get(self, request, pk):
        example = get_object_or_404(Example, pk=pk)
        example.mark_has_complete()
        return redirect("example_list")
