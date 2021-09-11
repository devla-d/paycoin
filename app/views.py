from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import  messages
from django.http import JsonResponse
from django.contrib.auth  import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from .models import Account,Transaction,Buycoin

from .forms import RegistrationForm,LoginForm,VerifypaymentForm,UserChangeForm,ProfileForm,ProfileInfoForm




def home_view(request):
    return render(request, 'index.html')

def helpdesk_view(request):
    return render(request, 'helpdesk.html')

def contact_view(request):
    return render(request, 'contact.html')


def faq_view(request):
    return render(request, 'faq.html')

def about_us_view(request):
    return render(request, 'about.html')

def team_view(request):
    return render(request, 'team.html')

def carer_view(request):
    return render(request, 'career.html')

def wallet_view(request):
    return render(request, 'wallet.html')

def price_view(request):
    return render(request, 'price.html')


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required
def history_view(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'history.html',{'transactions':transactions})

@login_required
def sell_coin_view(request):
    if request.POST:
        user = request.user
        if user.coin_balance > 0:
            messages.success(request, f'Coin sold!')
            return redirect('sell_coin')
        else:
            messages.success(request, f'Insufficient Funds!')
            return redirect('sell_coin')
    return render(request, 'sell_coin.html')


def amount_in_coin(coin,amount):
    one_btc = 0.000021
    one_eth = 999
    return amount * 10

@login_required
def buy_coin_view(request):
    if request.method == 'POST':
        user = request.user
        coin = request.POST.get('coin')
        amount = int(request.POST.get('amount'))
        if amount > 0:
            buycoin = Buycoin.objects.create(
                user=user,
                coin = coin,
                amount_in_usd=amount,
                amount_in_coin = amount_in_coin(coin,amount),
                payment_method = "bank transfer"
            )
            Transaction.objects.create(
                user=user,
                coin = coin,
                amount_in_usd=amount,
                amount_in_coin = amount_in_coin(coin,amount),
                transac_type = 'deposite',
                status = 'processing'
            )
            return redirect(f"/verify-payment/?bcuri={buycoin.uri}")
        else:
            return redirect('buy_coin')
    return render(request, 'buy_coin.html')

@login_required
def verify_payment_view(request):
    if request.POST:
        uri = request.POST.get('payuri')
        try:
            buycoin = Buycoin.objects.get(uri=uri)
            form = VerifypaymentForm(request.POST, request.FILES, instance=buycoin)
            if form.is_valid():
                pay = form.save(commit=False)
                pay.verified = True
                pay.save()
                messages.success(request, f'Payment verifield!')
                return redirect('buy_coin')
        except:
            redirect('buy_coin')
    else:
        uri   =  request.GET.get('bcuri')
        if uri:
            try:
                buycoin = Buycoin.objects.get(uri=uri)
                form = VerifypaymentForm()
                return render(request, 'verify_payment.html',{"buycoin":buycoin, 'form':form})
            except:
                redirect('buy_coin')
        else:
            return redirect('buy_coin')





@login_required
def account_view(request):
    return render(request, 'account.html')

    
@login_required
def account_setting_view(request):
    context = {
        'p_form' : ProfileForm(),
        'p_info_form': ProfileInfoForm()
    }
    return render(request, 'settings.html',context)


@login_required
def user_paswordchange_view(request):
    if request.POST:
        user = request.user
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.info(request, f'Passwords don\'t match')
            return redirect('settings')

        if not user.check_password(password1):
            messages.info(request, f'Old password don\'t match')
            return redirect('settings')
        else:
            user.set_password(password1)
            user.save()
            messages.info(request, f'Password Change')
            return redirect('settings')





@login_required
def profile_info_view(request):
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, f'Account Updated')
            return redirect('settings')
    else:
        return redirect('settings')  
              
@login_required
def user_profile_info_view(request):
    if request.POST:
        form = ProfileInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, f'Account Updated')
            return redirect('settings')
    else:
        return redirect('settings') 




#authenticaticion """
def login_view(request):
    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request,user)
                if destination:
                    return redirect(destination)
                return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form":form})



def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect







def logout_view(request):
    user = request.user
    logout(request)
    return redirect('login')






def register_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created !')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html',{"form":form})