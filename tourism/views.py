# from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ReviewForm
from .models import Review , Place
from django.contrib import messages

# messages.warning(request, "Your submission was rejected by admin.")

# Create your views here.
def home(request):
    places=Place.objects.all()
    return render(request,'tourism/index.html',{'places':places})

def place_detail(request,place_id):
    place=get_object_or_404(Place,id=place_id)
    return render(request,'place_detail.html',{'place':place})
# def anjumala(request):
#     return render(request,'tourism/places/anjumala.html')

# def aranmula(request):
#     return render(request,'tourism/places/aranmula.html')

# def charalkkunnu(request):
#     return render(request,'tourism/places/charalkkunnu.html')

# def chengara(request):
#     return render(request,'tourism/places/chengara.html')

# def chuttippara(request):
#     return render(request,'tourism/places/chuttippara.html')

# def gavi(request,place_id):
    
#     return render(request,'tourism/places/gavi.html')

# def konniadavi(request):
#     return render(request,'tourism/places/konniadavi.html')

# def mannera(request):
#     return render(request,'tourism/places/mannera.html')

# def nilakkal(request):
#     return render(request,'tourism/places/nilakkal.html')

# def orakkanpara(request):
#     return render(request,'tourism/places/orakkanpara.html')

# def pandalam(request):
#     return render(request,'tourism/places/pandalam.html')

# def parumala(request):
#     return render(request,'tourism/places/parumala.html')

# def perunthenaruvi(request):
#     return render(request,'tourism/places/perunthenaruvi.html')

# def sabarimala(request):
#     return render(request,'tourism/places/sabarimala.html')



#Signup / Login page

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()

    # Add Bootstrap classes
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    return render(request, 'tourism/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'tourism/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


#Profile
@login_required
def profile_view(request):
    
    reviews = Review.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Review submitted and waiting for approval.")
    else:
        form = ReviewForm()

    return render(request, 'tourism/profile.html', {
        'form': form,
        'reviews': reviews
    })


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    approved_reviews = Review.objects.filter(
        place=place,
        status='approved'
    )

    gallery_photos = approved_reviews.exclude(image='').exclude(image=None)
    text_reviews=approved_reviews.exclude(content='').exclude(content=None)

    context={
        'place': place,
        'gallery_photos': gallery_photos,
        'text_reviews': text_reviews,
    }

    return render(request, 'tourism/place_detail.html',context)


def place_description(request,place_id):
    place=get_object_or_404(Place,id=place_id)
    return render(request,'place_description.html',{'place':place})