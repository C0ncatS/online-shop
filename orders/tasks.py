from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from celery import shared_task

from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order_id}"
    from_email = None
    to_email = [order.email]
    text_content = render_to_string("emails/order_created.txt", {"order": order})
    html_content = render_to_string("emails/order_created.html", {"order": order})
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send()
    return True
