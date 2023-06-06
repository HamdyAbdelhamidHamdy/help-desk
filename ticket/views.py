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


        if form.is_valid():
            images = request.FILES.getlist('image')
            print(images)

            ticket = form.save(commit=False)
            ticket.save()
            for image in images:
                s=UploadMedia.objects.create(file=image)
                ticket.image.add(s)
            ticket.save()
            admin_email = settings.ADMINS[0][1]
            print(admin_email)
            subject = f'New ticket has been created: {ticket.name}'
            message = f'Ticket {ticket.name} has been created.\n\nDescription:\n{ticket.description}'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])
            return redirect('ticket:create-ticket')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})
