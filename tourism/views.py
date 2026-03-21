from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ReviewForm,PhotoForm
from .models import Review , Place, Photo
from django.contrib import messages
def home(request):
    places=Place.objects.all()
    reviews=Review.objects.filter(approved=True).select_related('place','user')

    return render(request,'tourism/index.html',{
        'places':places,
        'reviews':reviews
        })
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

@login_required
def profile(request):

    review_form = ReviewForm()
    photo_form = PhotoForm()

    if request.method == "POST":

        if "review_submit" in request.POST:

            review_form = ReviewForm(request.POST)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.save()

                return redirect("profile")

        elif "photo_submit" in request.POST:

            photo_form = PhotoForm(request.POST, request.FILES)

            if photo_form.is_valid():
                photo = photo_form.save(commit=False)
                photo.user = request.user
                photo.save()

                return redirect("profile")
    user_reviews=Review.objects.filter(user=request.user).order_by("-created_at")
    user_photos=Photo.objects.filter(user=request.user).order_by("-uploaded_at")

    context = {
        "review_form": review_form,
        "photo_form": photo_form,
        "user_reviews":user_reviews,
        "user_photos":user_photos
    }

    return render(request, "tourism/profile.html", context)

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    reviews = Review.objects.filter(
        place=place,
        approved=True
    )
    photos = Photo.objects.filter(
        place=place,
        approved=True
    )


    context={
        'place': place,
        'photos': photos,
        'reviews': reviews,
    }

    return render(request, 'tourism/place_detail.html',context)
def place_description(request,place_id):
    place=get_object_or_404(Place,id=place_id)
    return render(request,'place_description.html',{'place':place})

def gallery(request,place_id):
    place=get_object_or_404(Place,id=place_id)
    photos=Photo.objects.filter(place=place,approved=True)
    
    return render(request,'tourism/gallery.html',{
        'place':place,
        'photos':photos
    })

def reviews(request,place_id):
    place=get_object_or_404(Place,id=place_id)
    reviews=Review.objects.filter(place=place,approved=True)
    
    return render(request,'tourism/reviews.html',{
        'place':place,
        'reviews':reviews
    })

def all_reviews(request):
    reviews=Review.objects.filter(approved=True).select_related('place','user').order_by('-created_at')
    return render(request,'tourism/index.html',{'reviews':reviews})