from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .beta import *

from django.http import JsonResponse, HttpResponse
import json, string, random
from paypal.standard.forms import PayPalPaymentsForm
from verify_email.email_handler import send_verification_email

from .beta import *
from .creativity import *
from .utone import *
from .functions import *
import openai
from .predicting_outputs import *
import writer.editnts as editnts
from .editnts import *
from .main import *
from .data import *
from .evaluator import *
from .label_edits import edit2sent

import sys
sys.path.append('writer')

from .checkpoint import Checkpoint

from .data_preprocess import *

OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY
from .forms import NewUserForm
from .models import packages, notes, UserAcc, dataset

# Create your views here.


def home(request):

    template_name = "home.html"


    return render(request,'home.html')
@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dash.html')

@login_required(login_url='/login/')
def package(request):


    return render(request, 'package.html',)


def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/login/')
def history(request):
    view_note = notes.objects.filter(owner=request.user)

    return render(request, 'history.html', { 'view_note': view_note,})

def notes_view(request,notes_id):
    edit_note = notes.objects.get(id=notes_id)
    print(edit_note.text)

    return render(request, "notes.html",{ 'edit_note': edit_note,})


def loginview(request):

    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == "POST":

        form_class = AuthenticationForm(request.POST, request.POST)
        if form_class.is_valid():
            username = form_class.cleaned_data['username']
            password = form_class.cleaned_data['password']

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('/dashboard')
        else:
            print("login invalid")
            print("Error Message: ", form_class.error_messages)
            first_error = next(iter(form_class.error_messages.items()))
            return render(request,'login.html',{ 'first_error': first_error, })
            
    #if request.method == 'POST':
        #email = request.POST.get('email')
        #password = request.POST.get('password')
        #return redirect('/dashboard')
    return render(request,'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
        
    if request.method == "POST":
        form = NewUserForm(request.POST)     
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign Up Successful")
            inactive_user = send_verification_email(request, form)
            return redirect("/")
        print(form.errors)
        first_error = next(iter(form.errors.items()))
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return render(request, 'register.html', { 'first_error': first_error, })
    form = NewUserForm()

    return render(request, 'register.html')

@login_required(login_url='/login/')
def write(request):
    if request.method == 'POST':

        details = request.POST.get('details')
        language = request.POST.get('language')
        category = request.POST.get('category')
        print(language + category + details)
        if category == 'headline':
            headprompt = f" write headline using following details: \n\n{details}  \nin {language} "
            blogA = headline(headprompt)
            blogExpandedA = blogA.replace('\n', '<br>')
        elif category == 'blogintro':
            headprompt = f" Expand the topic into a clever and creative blog introduction: \n\n {details} \n in {language} "
            blogA = headline(headprompt)
            blogExpandedA = blogA.replace('\n', '')
        if category == 'blogcon':
            headprompt = f" Expand the topic into a clever and creative blog conclusion:\n\n {details} \n in {language} "
            blogA = headline(headprompt)
            blogExpandedA = blogA.replace('\n', '<br>')
        elif category == 'blogpara':
            headprompt = f" Expand the topic into a clever and witty blog section: \n\n {details} \n in {language} "
            blogA = headline(headprompt)
            blogExpandedA = blogA.replace('\n', '<br>')
        elif category == 'translate':
            headprompt = f" Make a creative story about: \n\n {details} \n in {language} "
            blogA = headline(headprompt)
            blogExpandedA = blogA.replace('\n', '<br>')
        elif category == 'email':
            headprompt = f"Write video description from following details: \n\n {details} \n in {language} "
            blogA = headline(headprompt)
            blogExpandedA = blogA.replace('\n', '<br>')
        elif category == 'business':
            headprompt = f"White a product description about: \n\n {details} \n in {language} "
            blogA = headline(headprompt)
            blogExpandedA = blogA.replace('\n', '<br>')
        print(blogExpandedA)

    return render(request, 'write.html')

def create(request):

    if request.method =='PUT':
        json_req = json.loads(request.body.decode('utf-8'))

        complex = json_req['complex']
        simple = json_req['simple']

        dataset_object = dataset.objects.create(complex_text = complex, simple_text = simple)

        complex_str_list = complex.split('.')
        simple_str_list = simple.split('.')
        complex_str_list.pop()
        simple_str_list.pop()
        while(len(complex_str_list) != len(simple_str_list)):

            if(len(complex_str_list) > len(simple_str_list)):
                complex_str_list.pop()
            elif(len(simple_str_list) > len(complex_str_list)):
                simple_str_list.pop()

        for line in complex_str_list:
            with open("complex", 'a') as file1:
                file1.write(line + "\n")

        for line in simple_str_list:
            with open("simple", 'a') as file2:
                file2.write(line + "\n")


    if request.method =='POST':

        get_result(request)

        #usertile = request.POST.get('usertitle')
        #usertext = request.POST.get('userprompt')
        #usertone = request.POST.get('tone')
        #creativeness = request.POST.get('creativity')
        #qa = request.POST.get('qa')
        #aa = request.POST.get('aa')
        #qb = request.POST.get('qb')
        #num = request.POST.get('num')
        #creatives= hello(creativeness)
        #tone=utone(usertone)
        #print(usertext)
        #print(tone)
        #print(creatives)
        #aioutput= direction(usertile, usertext, tone, creatives, qa, aa, qb, num)
        #print(aioutput)
        #print(type(aioutput))

        #data = { "aioutput": aioutput,}
        #return HttpResponse(json.dumps(data))

        #if request.method =='GET':
            #return JsonResponse(data)
    return render(request, 'indexsec.html')

def get_result(request):
    user_email = request.user.email

    if request.method =='POST':
        json_req = json.loads(request.body.decode('utf-8'))
        print(json_req)
        print(json_req['text'])

        #print("json text: ", request.body.get('text'))
        usertile = json_req['title']
        usertext = json_req['text']
        usertone = json_req['tone']
        creativeness = json_req['creativity']
        qa = json_req['qa']
        aa = json_req['aa']
        qb = json_req['qb']
        num = json_req['num']
        creatives= hello(creativeness)
        tone=utone(usertone)
        aioutput= direction(usertile, usertext, tone, creatives, qa, aa, qb, num)

        clean_string = aioutput.replace('\n',' ')
        clean_string = clean_string.replace('\r','')
        print(aioutput)
        simplified = predict(clean_string)
        print(simplified)

        note_title = aioutput[:15]+"..."
        if aioutput:
            current_user = UserAcc.objects.get(email=user_email)
            if (current_user.credit >= len(aioutput.split())):
                current_user.credit = current_user.credit - len(aioutput.split())
                current_user.save()
            else:
                list_output = aioutput.split()
                list_output = list_output[:current_user.credit]
                aioutput = ' '.join(list_output)
                current_user.credit = current_user.credit - len(aioutput.split())
                current_user.save()
            
            note = notes.objects.create(owner=request.user,title=note_title, text=aioutput)

    data = { "aioutput": aioutput,'simplified':simplified, 'word_length': len(aioutput.split()), }


    return JsonResponse(data, safe=False)

def checkout(request, packages_id):
    p_list = packages.objects.all()
    paypal_dict = {}

    for pack in p_list:
        if(packages_id==pack.id):
            paypal_dict = {
                "business": 'uniai@mail.com',
                "amount": str(pack.price),
                "currency_code": "USD",
                "item_name": str(pack.name),
                "invoice": "unique-invoice-id",
                "notify_url": "https://www.example.com" + ('paypal-ipn'),
                "return_url": "https://www.example.com/your-return-location/",
                "cancel_return": "https://www.example.com/your-cancel-location/",

    }

    
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form , 'paypal_dict': paypal_dict,}
    return render(request,"payment.html", context)

def package_purchase(request, package_key, packages_id):
        package_values = {
            '1': 50000,
            '2': 150000,
        }

        if(package_key == request.session['key']):
            current_user = UserAcc.objects.get(email=request.user.email)
            current_user.credit = current_user.credit + package_values[packages_id]
            current_user.save()


        return render(request, 'dash.html')

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": 'uniai@mail.com',
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com" + ('paypal-ipn'),
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",

    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request,"payment.html", context)


def password_reset(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = UserAcc.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "email.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                        print("Email Done")
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    else:
        password_reset_form = PasswordResetForm()
    return render(request, "reset.html", {'password_reset_form': password_reset_form,})