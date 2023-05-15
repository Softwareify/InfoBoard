from django import forms


class PageCMSStatusForm(forms.Form):
    changed_page_status = forms.IntegerField()
