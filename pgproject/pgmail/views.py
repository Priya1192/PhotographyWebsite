from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
# from pgproject.pgproject.settings import EMAIL_HOST_USER


def display(request):
    if request.method == "POST":
        if request.POST.get("pname") and request.POST.get("pphone") and request.POST.get("pemail") and request.POST.get("pcomment"):
            name = request.POST["pname"]
            phone = request.POST["pphone"]
            email = request.POST["pemail"]
            comment = request.POST["pcomment"]

            subject = "Greetings from Clean Photography!"

            message = f"Hi {name},\n\n\t\tWe are happy that you are interested in our service.\n"
            message = message + f"\nWe will call you at your given number {phone}\n"
            message = message + f"Your enquiry : {comment}\n\n"
            message = message + "With Regards,\nClean Photography\n(+91) 9898989898."

            send_mail(subject,message,'zeva.connect@gmail.com',[email,])
            return render(request,'pgmail/mail.html')
