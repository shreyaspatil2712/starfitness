from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from .forms import TrainerForm
from .forms import LoginForm
from .models import Trainer
from .models import Booking
from .models import LoginData
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q



from django.shortcuts import render, redirect
from .models import Customer, Trainer, Booking
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def book_sessions(request):
    if request.method == 'POST':
        # Get the selected trainer's username from the form
        trainer_username = request.POST['trainer_username']
        
        # Get the selected date and time from the form
        date = request.POST['date']
        time = request.POST['time']
        
        # Get the logged-in customer
        customer =request.user.username
        
        # Get the selected trainer
        trainer =  trainer_username
        
        # Create a new booking
        booking = Booking.objects.create(
            customer=customer,
            trainer=trainer,
            date=date,
            time=time
        )
        print('00000000000000000000000000000000000000000')

        print(customer)
        print(trainer)
        
        # Save the booking
        booking.save()
        
        # Redirect to the history page
        return redirect('history_page')
    
    # Get all trainers
    trainers = Trainer.objects.all()
    
    # Get the search query from the form
    search_query = request.GET.get('search_query', '')
    
    # Filter trainers based on the search query
    if search_query:
        trainers = trainers.filter(Q(username__icontains=search_query) | Q(speciality__icontains=search_query))
    
    return render(request, 'book_sessions.html', {'trainers': trainers, 'search_query': search_query})


def landing_page(request):
    return render(request, 'landing_page.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import LoginData, Customer, Trainer

def  customer_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        # Create a new User object
        user = User.objects.create_user(username=username, password=password)

        # Create a new Customer object
        customer = Customer.objects.create(
            username=username,
            full_name=full_name,
            dob=dob,
            gender=gender,
            email=email,
            phone_number=phone_number
        )

        # Save the User and Customer objects
        user.save()
        customer.save()

        # Redirect to the login page
        return redirect('login_page')

    return render(request, 'customer_signup.html')



def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            auth_login(request, user)
            if Customer.objects.filter(username=username).exists():
                return redirect('book_sessions')
            elif Trainer.objects.filter(username=username).exists():
                return redirect('trainer_page')
        else:
            # Invalid credentials
            return render(request, 'login_page.html', {'error': 'Invalid username or password'})

    return render(request, 'login_page.html')

def user_logout(request):
    # Logout the user
    logout(request)
    return redirect('landing_page')


def trainer_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        speciality = request.POST['speciality']
        hourly_rate = request.POST['hourly_rate']
        print(hourly_rate)
        print(full_name)
        

        # Create a new User object
        user = User.objects.create_user(username=username, password=password)

       
        trainer = Trainer.objects.create(
            username=username,
            full_name=full_name,
            dob=dob,
            gender=gender,
            email=email,
            phone_number=phone_number,
            hourly_rate = hourly_rate,
            speciality = speciality
            
        )

        # Save the User and Customer objects
        user.save()
        trainer.save()

        # Redirect to the login page
        return redirect('login_page')

    return render(request, 'trainer_signup.html')







@login_required
def history_page(request):
    bookings = Booking.objects.filter(Q(customer=request.user.username) | Q(trainer=request.user.username))
    return render(request, 'history_page.html', {'bookings': bookings})

@login_required
def trainer_page(request):
    # Get the logged-in trainer
    user_name  = request.user.username
    
    # Retrieve the booking history associated with the trainer
    booking_history = Booking.objects.filter(trainer=user_name)
    
    # Pass the booking history to the template
    print(0000000000000000000000000000000)
    print(user_name)
    return render(request, 'trainer_page.html', {'booking_history': booking_history})


@login_required
def profile_page(request):
    # Get the logged-in user
    user = request.user

    # Check if the user is a customer or a trainer
    if Customer.objects.filter(username=user.username).exists():
        # User is a customer
        user_type = 'customer'
        user_details = Customer.objects.get(username=user.username)
        form = CustomerForm(instance=user_details)

        if request.method == 'POST':
            form = CustomerForm(request.POST, request.FILES, instance=user_details) if user_type == 'customer' else TrainerForm(request.POST, request.FILES, instance=user_details)
            if form.is_valid():
                form.save()
                return redirect('profile_page')
        return render(request, 'customer_profile_page.html', {'user_type': user_type, 'user_details': user_details, 'form': form})
        
    elif Trainer.objects.filter(username=user.username).exists():
        # User is a trainer
        user_type = 'trainer'
        user_details = Trainer.objects.get(username=user.username)
        form = TrainerForm(instance=user_details)

        if request.method == 'POST':
            form = CustomerForm(request.POST, request.FILES, instance=user_details) if user_type == 'customer' else TrainerForm(request.POST, request.FILES, instance=user_details)
            if form.is_valid():
                form.save()
                return redirect('profile_page')
        return render(request, 'trainer_profile_page.html', {'user_type': user_type, 'user_details': user_details, 'form': form})
    
    else:
        # User is neither a customer nor a trainer
        return redirect('landing_page')
    


def video_call(request, customer_username, trainer_username):
    # Concatenate the usernames to create the meeting link
    meeting_link = f"{customer_username}-{trainer_username}"

    return render(request, 'video_call.html', {'meeting_link': meeting_link})


