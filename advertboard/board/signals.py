from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from datetime import datetime
from .models import Responses, User, Advertisment


@receiver(post_save, sender=Responses)
def notify_create_response(sender, instance, created, **kwargs):
    if created:
        html_content = render_to_string('email_create_response.html',
                                        {'instanse': instance} )
        msg = EmailMultiAlternatives(
            subject=f'Уведомление об отклике',
            body=f'Новый отклик',
            from_email='test1@sch1935.site',
            to=[instance.advert.user.email,instance.user.email],
        )
        msg.attach_alternative(html_content, "text/html")

        msg.send()
    else:
        if instance.acceptresponse:
            html_content = render_to_string('email_accept_response.html',
                                        {'instanse': instance} )
            msg = EmailMultiAlternatives(
                subject=f'Отклик принят',
                body=f'Отклик обновлен',
                from_email='test1@sch1935.site',
                to=[instance.user.email],
            )
            msg.attach_alternative(html_content, "text/html")

            msg.send()
