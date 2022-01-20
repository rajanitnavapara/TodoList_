from django.shortcuts import render
from django_email_verification import send_email

# # Create your views here.
# def sendEmail(request):
#     if request.method == 'POST':
#         password = request.POST['password']
#         username = request.POST['username']
#         email = request.POST['email']
#         user = request.user
#         send_email(user)
#         return render(request,'EmailVerification/confirm_template.html')

from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate,get_user_model
# from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage,send_mail 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):  
    # save form in the memory not in database  
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username):
            return render(request,'sign_up.html',{'msg': 'username already exist.'})
        user = get_user_model().objects.create(username=username,password=password,email=email)
        # user = request.user
        user.is_active = False  
        user.save()  
        # to get the domain of the current site  
        current_site = get_current_site(request)  
        mail_subject = 'Activation link has been sent to your email id'  
        message = render_to_string('EmailVerification/acc_active_email.html', {  
            'user': user,  
            'domain': current_site.domain,  
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
            'token':account_activation_token.make_token(user),  
        })  
        to_email = email
        from_email = 'rajanitnavapara7777@gmail.com'
        # email = EmailMessage(  
        #             mail_subject, message, to=[to_email]  
        # )  
        # email.send()  
        send_mail(mail_subject, message, from_email,[email], fail_silently=False,)
        return HttpResponse('Please confirm your email address to complete the registration. <a href="/auth">Click here</a> to SignIn</p>')  

# return render(request, 'signup.html', {'form': form})  


def activate(request, uidb64, token):  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. <a href="/auth">Click here</a> to SignIn.')  
    else:  
        return HttpResponse('Activation link is invalid!')  
    
    