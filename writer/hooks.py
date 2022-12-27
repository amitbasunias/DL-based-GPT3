from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from .models import packages, UserAcc
from threadlocals.threadlocals import get_current_request

def show_me_the_money(sender, **kwargs):
    request = get_current_request()
    p_list = packages.objects.all()

    package_values = {}
    for packs in p_list:
        package_values[str(packs.price)] = packs.value

    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != "afikur.rahman44@gmail.com":
            # Not a valid payment
            return

        # Undertake some action depending upon `ipn_obj`.
        current_user = UserAcc.objects.get(email=request.user.email)
        current_user.credit = current_user.credit + package_values[str(ipn_obj.amount)]
        current_user.save()
    else:
        print("")

valid_ipn_received.connect(show_me_the_money)