from dataclasses import field
from gettext import gettext
from django import forms
from .models import Sites
import gettext
from django.contrib import messages
_ = gettext.gettext

class CheckForm(forms.Form):
    domain_form = forms.CharField(label=_('Domain'))

    def clean(self):
        domain_name = self.cleaned_data.get('domain_form')
        site = Sites.objects.filter(domain=domain_name).first()
        if str(site) == domain_name:
            if site.is_scam == True:
                raise forms.ValidationError(_(f'{domain_name} является поддельным сайтом'))
        elif site is None:
            raise forms.ValidationError(_(f'{domain_name} не занесен в базу данных, и скорее всего является поддельным'))
    



#class CheckForm(forms.ModelForm):
#
#    domain_form = forms.CharField(label='Domain')
#
#    if not Sites.objects.filter(domain=domain_form):
#        raise forms.ValidationError(_("Введеный домен обладает 100% гадкостью"))
#
#    class Meta:
#        model = Sites
#        fields = ['domain']       