from django.shortcuts import render
from data import forms

def index(request):
    return render(request, 'index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'form.html', {'form':form})    