from django.shortcuts import render
from authentication.models import userProfile
from django.http import HttpResponse ,HttpRequest

# Create your views here.
def login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        Username = userProfile.objects.values('username')
        Password = userProfile.objects.values('user_password')

        user_name = [user['username'] for user in Username]
        user_password = [p['user_password'] for p in Password]

        for u_name, u_password in zip(user_name, user_password):
            if (username == u_name):
                if(password == u_password):  
                    return render(request,'index.html')
                else:
                    print("wrong info") 
                    error = "Password does not matched!!"
                    return render(request,'login.html',{'error':error})       
                    
    return render(request,'login.html')

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact=request.POST.get('contact')
        email=request.POST.get('email_Address')
        address=request.POST.get('home_Address')
        image=request.POST.get('image_upload')
        status=request.POST.get('status')

        user=userProfile()

        user.username = username
        user.user_password = password
        user.user_contact=contact
        user.user_email=email
        user.user_address=address
        user.user_profile=image
        user.user_status =  status

        user.save()
        # process your data
        print("Your form data...")
        print(username)
        print(password)
        print(status)
        print(username)
        print(password)
        print(email)
        print(email)
        print(contact)
        print(status)
        return render(request,'login.html')

    return render(request,'signup.html')

# send email with verification link
def verify_email(request):
    # so we can reference the user model as User instead of CustomUser
    user = userProfile()
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.username
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('user/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return render('verify-email-done')
        else:
            return render('signup')
    return render(request, 'user/verify_email.html')
# Add below existing imports
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages

# so we can reference the user model as User instead of CustomUser
# user = userProfile()

# send email with verification link
# def verify_email(request):
#     if request.method == "POST":
#         if request.user.email_is_verified != True:
#             current_site = get_current_site(request)
#             user = request.username
#             email = request.user.email
#             subject = "Verify Email"
#             message = render_to_string('user/verify_email_message.html', {
#                 'request': request,
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             email = EmailMessage(
#                 subject, message, to=[email]
#             )
#             email.content_subtype = 'html'
#             email.send()
#             return render('verify-email-done')
#         else:
#             return render('signup')
#     return render(request, 'user/verify_email.html')