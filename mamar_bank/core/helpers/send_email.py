from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_transaction_email(user, amount, mail_subject, template_name, other_account):
    message = render_to_string(
        template_name, {"user": user, "amount": amount, "other_account": other_account}
    )

    send_email = EmailMultiAlternatives(mail_subject, "", to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()
