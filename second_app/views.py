from django.shortcuts import render
from second_app.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, "forms/index.html")

def user(request):
    
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Error form invalid')

    return render(request, 'forms/users.html', {'form': form})