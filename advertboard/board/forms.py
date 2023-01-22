from django import forms
from .models import Advertisment, Responses, User, CATEGORY
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



class AdsForm(forms.ModelForm):
    head = forms.CharField(min_length=5, max_length=255, label='Заголовок')

    class Meta:
        model = Advertisment
        fields = [
            'head',
            'content_upload',
            'category'
        ]
        labels = {'category': ('Категория материала'), 'content_upload':('Контент')}

    def clean(self):

        cleaned_data = super().clean()
        text = cleaned_data.get("head")
        head = cleaned_data.get("content")

        if head == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class ResponseForm(forms.ModelForm):

    class Meta:
        model = Responses
        fields = [
            'text',
        ]
        labels = {'text':''}


UCHOISE = User.objects.all().values_list('id','username')
MCHOISE = (('1','Рассылка объявлений'), ('2','Рассылка информационных сообщений'))

class MailForm(forms.Form):
    mailing = forms.ChoiceField(choices=MCHOISE)
    head = forms.CharField(min_length=5, required=False)
    text = RichTextUploadingFormField(required=False)
    category = forms.MultipleChoiceField(choices=CATEGORY,required=False)
    user = forms.MultipleChoiceField(choices=UCHOISE, required=False)
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-select','style':'max-width:10%'}), required=False)

    def send_email(self):
        #сначала получаем список пользователей (если он пустой, то выбираем всех пользователей)
        if self.cleaned_data['user']:
            user = self.cleaned_data['user']
        else:
            user = User.objects.all().values('id')
            user = [str(i['id']) for i in user] #получаем id как список

        #генерирую спиков email пользователей для отправки
        useremail = [str(i['email']) for i in User.objects.filter(pk__in=user).values('email')]

        #если выбран тип рассылка объявление
        if self.cleaned_data['mailing'] == '1':
            #берет значения выбранных категорий (если не указано, то выбираются все)
            if self.cleaned_data['category']:
                category = self.cleaned_data['category']
            else:
                category = Advertisment.objects.all().values_list('category')
            #берет значения даты (если не указано, то будет рассылка за неделю)
            if self.cleaned_data['date']:
                date = self.cleaned_data['date']
            else:
                date = datetime.now() - timedelta(days=7)

            ads = Advertisment.objects.filter(category__in=category, time_update__gt=date) #получаем объявления по указанным параметрам

            #генерирую html страницу для письма
            html_content = render_to_string('mailing_ads.html',
                                        {'ads': ads, 'date': date} )


        #если выбран тип рассылки информационное сообщение
        elif self.cleaned_data['mailing'] == '2':
            html_content = render_to_string('mailing_info.html',{'text': self.cleaned_data['text'], 'head':self.cleaned_data['head'] } )


        msg = EmailMultiAlternatives(
            subject=f'Уведомление о рассылке',
            body=f'Новая рассылка',
            from_email='test1@sch1935.site',
            to=useremail,
        )
        msg.attach_alternative(html_content, "text/html")

        msg.send()

        return True
