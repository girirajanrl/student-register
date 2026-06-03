from django.shortcuts import render, redirect,get_object_or_404

from .models import StudentIntern,Payment



from .forms import StudentInternForm, PaymentForm

from .forms import modeform,Durationform,Domainform
"""

#add category

def add_mode(request):

    form=modeform()

    if request.method=='POST': #snd the data

        form=modeform(request.POST)

        if form.is_valid():

            form.save()

    return render(request,'internship/add_mode.html',{'form':form})


def add_duration(request):

    form =Durationform()

    if request.method=="POST":
        
        form=Durationform(request.POST)

        if form.is_valid():

            form.save()

    return render(request,'internship/add_duration.html',{'form':form})


def add_domain(request):

    form=Domainform()

    if request.method=='POST':

        form=Domainform(request.POST)

        if form.is_valid():

            form.save()

    return render(request,'internship/add_domain.html',{'form':form})



"""

def project_register(request):

    form = StudentInternForm()

    if request.method == "POST":

        form = StudentInternForm(request.POST)

        if form.is_valid():

            project = form.save()

            return redirect('internship:payment_page', project.id)

    return render(request, 'internship/add_internship.html', {'form': form})



def payment_page(request, project_id):
    project = get_object_or_404(StudentIntern, id=project_id)

    form = PaymentForm()

    if request.method == "POST":

        form = PaymentForm(request.POST, request.FILES)

        if form.is_valid():
            payment = form.save(commit=False)
            payment.intern = project

            payment_mode = form.cleaned_data['payment_mode']  #get payment_mode value

            if payment_mode == "online":
                payment.save()
                return redirect('internship:razorpay_payment', payment.id)

            elif payment_mode == "offline":
                payment.save()
                return redirect('internship:offline_payment', payment.id)

    return render(request, 'internship/payment.html', {
        'form': form
    })


def razorpay_payment(request, payment_id):

    payment = get_object_or_404(Payment, id=payment_id)

    return render(request, 'internship/razorpay_payment.html', {
        'payment': payment
    })


def offline_payment(request, payment_id):

    payment = get_object_or_404(Payment, id=payment_id)

    return render(request, 'internship/offline_payment.html',{
        'payment': payment
    })
















