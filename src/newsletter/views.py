from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm,SignUpForm


def home(request):
    title = 'Sign Up'
    form = SignUpForm(request.POST or None)

    context = {"title": title,
               "form": form,
               }

    if form.is_valid():

        instance = form.save(commit=False)

        full_name = form.cleaned_data.get('full_name')
        if not full_name:

            instance.full_name = full_name

        instance.save()
        context = {

            "title": 'thank you for visiting;'
            }

    return render(request, "newsletter/home.html", context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')

        subject = 'site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'myotheremail@email.com']
        contact_message = '''
        %s: %s via %s ''' % (form_full_name, form_message, form_email)

        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
        )

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'newsletter/forms.html', context)
def booking_create(request):

    title = 'Book an environmental tour'
    form = BookingForm(request.POST or None)

    context={'title':title,
             'form':form
             }


    return render(request,'booking/booking_form.html',context)


