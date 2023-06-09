
from django.shortcuts import render
from django.template.loader import render_to_string
from upload_media.models import UploadMedia
from user.models import UserMail
from .forms import TicketForm
from .models import Ticket
from .utils import send_email


def home(request):
    tickets = Ticket.objects.all().order_by('-created_at')[:10]
    return render(request, 'home.html', {'tickets':tickets})


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST, files=request.FILES,)
        if form.is_valid():
            images = request.FILES.getlist('image')
            ticket = form.save(commit=False)
            ticket.save()
            for image in images:
                s = UploadMedia.objects.create(file=image)
                ticket.image.add(s)
            ticket.save()
            user_emails = UserMail.objects.all().order_by('-id')
            mail_list = [user_email.mail for user_email in user_emails]
            subject = f'New ticket has been created: {ticket.name}'
            message = render_to_string('create_ticket_mail.html', {'ticket':ticket})
            arr=[]
            for product in ticket.image.all():
                if product.file:
                    arr.append(product.file.path)
            ticket_data = {

                "image": arr,
            }
            send_email(ticket_data, subject=subject, body=message, email=mail_list,)
            return render(request, 'confirm_create_ticket.html',{})
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

