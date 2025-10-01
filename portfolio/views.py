from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_me_view(request):
    return render(request, 'portfolio/about_me.html')

def contact_view(request):
    if request.method == 'POST': #means the form is not empty
        #to send the email
        form = ContactForm(request.POST)
        #collect the data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #build the full email
            message_body = (
                f'You have a new email from your portfolio \n'
                f'Name: {name}\n'
                f'Email: {email}\n\n'
                f'Message:\n{message}'

            )
            #try to send the email
            try:
                send_mail(
                    "Email from portfolio", #subject
                    message_body, #message body --> the user typed
                    email, #from email:The user email
                    ['wilb1841@gmail.com']# To :Where you want to recieve the email
                )
                #after sending the email
                #form = ContactForm()
                return render(request, 'portfolio/contact.html', {'form':form})
            except Exception as e:
                    print(f'Error: {e}')
                    return render(request, 'portfolio/contact.html', {'form':form,})
        else:
            print("data" + name, email, message)
    else:
        form = ContactForm()
        return render(request, 'portfolio/contact.html', {'form':form})           
                
    

def experience_view(request):
    return render(request, 'portfolio/experience.html')

def projects_view(request):
    return render(request, 'portfolio/projects.html')
