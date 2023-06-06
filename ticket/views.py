from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from upload_media.models import UploadMedia
from .forms import TicketForm
from django.conf import settings


def home(request):
    return render(request, 'home.html', {})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST, files=request.FILES,)
        print(request.POST['name'])
        print(request.POST['description'])
        if form.is_valid():
            images = request.FILES.getlist('image')
            for image in images:
                UploadMedia.objects.create(file=image)
            ticket = form.save()
            admin_email = settings.ADMINS[0][1]
            print(admin_email)
            subject = f'New ticket has been created: {ticket.name}'
            message = f'Ticket {ticket.name} has been created.\n\nDescription:\n{ticket.description}'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])
            return redirect('ticket:home')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})
