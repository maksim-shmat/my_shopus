""" Docs """

from django import forms
#from django.utils.translation import gettext_lazy as _

class CouponApplyForm(forms.Form):
    """ docs """
    code = forms.CharField(label=('Coupon'))
