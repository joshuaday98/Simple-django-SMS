from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from twilio.rest import TwilioRestClient



def post_page(request):
    form = NameForm()
    if request.method == 'POST':
        data = request.POST
        account_sid = "AC86189c370a1fcca6c3dd11c2fa15ee04"
        auth_token = "1769e4656916ec050cdbe4e58d17e6c1"
        client = TwilioRestClient(account_sid, auth_token)
        number = data.get('number', '0')
        text = data.get('message_text', '0')

        message = client.messages.create(to=number, from_='+14243512633', body= text)
        print("Sent to {}".format(number))

    return render(request, 'home.html', {'form': form})
