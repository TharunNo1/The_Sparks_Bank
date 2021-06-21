from django.shortcuts import render
from .models import Customer, Trans
from django.contrib import messages
from django import forms
import datetime
from django.core.exceptions import ValidationError

transfers = []
cus1 = Customer()
cus1.id = 347421
cus1.name = "Madhan"
cus1.balance = 50000

cus2 = Customer()
cus2.id = 347422
cus2.name = "Sachin"
cus2.balance = 70000

cus3 = Customer()
cus3.id = 347423
cus3.name = "Ajith"
cus3.balance = 40000
        
cus4 = Customer()
cus4.id = 347424
cus4.name = "Rakesh"
cus4.balance = 45000

cus5 = Customer()
cus5.id = 347425
cus5.name = "Naveen"
cus5.balance = 35000

cus6 = Customer()
cus6.id = 347426
cus6.name = "Praveen"
cus6.balance = 75000

cus7 = Customer()
cus7.id = 347427
cus7.name = "Naveena"
cus7.balance = 60000

cus8 = Customer()
cus8.id = 347428
cus8.name = "Mavsi Aadhavan"
cus8.balance = 65000

cus9 = Customer()
cus9.id = 347429
cus9.name = "Jack"
cus9.balance = 95000

cus10 = Customer()
cus10.id = 347430
cus10.name = "John"
cus10.balance = 25000

def transfer(request):
    cuss = [ cus1, cus2, cus3, cus4, cus5, cus6, cus7, cus8, cus9, cus10]
    transForm = TransForm()
    if request.method == "POST":
        form = TransForm(request.POST)
        if form.is_valid():
            data = Trans()
            data.sender = form.cleaned_data['sender']
            data.receiver = form.cleaned_data['receiver']
            data.amount = form.cleaned_data['amount']
            data.datetime = datetime.datetime.now()
            min_bal = True
            same_cuss = False
            if data.sender == data.receiver:
                messages.warning(request, "Money cannot be transferred to the sender itself")
                same_cuss = True
            
            if not same_cuss:
                for cus in cuss:
                    if cus.name == data.sender:
                        if cus.balance < data.amount + 1000:
                            min_bal = False
                            messages.error(request, "Low Balance, So Transaction failed")
                            data.status = "Failed"
                            break
                        else:
                            messages.success(request, "Transaction Successful" )
                            data.status = "Successful"
                        cus.balance -= data.amount
                transfers.append(data)
                for cus in cuss:
                    if cus.name == data.receiver and min_bal==True:
                        cus.balance += data.amount     
            
    return render(
        request, 
        "transfer.html", 
        {
            'customers': cuss,
            'transfers': transfers,
            'form': transForm,
            })

class TransForm(forms.Form):
    cus_names = [
        ('Madhan','Madhan'),
        ('Sachin','Sachin'),
        ('Ajith','Ajith'),
        ('Rakesh','Rakesh'),
        ('Naveen','Naveen'),
        ('Praveen','Praveen'),
        ('Naveena','Naveena'),
        ('Mavsi Aadhavan','Mavsi Aadhavan'),
        ('Jack','Jack'),
        ('John','John')
    ]
    sender = forms.ChoiceField(required=True, choices=cus_names)
    receiver = forms.ChoiceField(required=True, choices=cus_names)
    amount = forms.IntegerField()