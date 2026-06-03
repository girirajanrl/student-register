from django.shortcuts import render, redirect,get_object_or_404

from .models import StudentTraining,Payment



from .forms import StudentTrainingForm, PaymentForm

from .forms import modeform,Durationform,Domainform


def add_mode(request):

    form=modeform()

    if request.method=='POST':

        form=modeform(request.POST)

        if form.is_valid():

            form.save()

    return render(request,'training/add_mode.html',{'form':form})


def add_duration(request):

    form =Durationform()

    if request.method=="POST":
        
        form=Durationform(request.POST)

        if form.is_valid():

            form.save()

    return render(request,'training/add_duration.html',{'form':form})


def add_domain(request):

    form=Domainform()

    if request.method=='POST':

        form=Domainform(request.POST)

        if form.is_valid():

            form.save()

    return render(request,'training/add_domain.html',{'form':form})




def project_register(request):

    form = StudentTrainingForm()

    if request.method == "POST":

        form = StudentTrainingForm(request.POST)

        if form.is_valid():

            project = form.save()

            return redirect('training:payment_page', project.id)

    return render(request, 'training/add_training.html', {'form': form})




def payment_page(request, project_id):
    project = get_object_or_404(StudentTraining, id=project_id)

    form = PaymentForm()

    if request.method == "POST":

        form = PaymentForm(request.POST, request.FILES)

        if form.is_valid():
            payment = form.save(commit=False)
            payment.training = project

            payment_mode = form.cleaned_data['payment_mode']

            if payment_mode == "online":
                payment.save()
                return redirect('training:razorpay_payment', payment.id)

            elif payment_mode == "offline":
                payment.save()
                return redirect('training:offline_payment', payment.id)

    return render(request, 'training/payment.html', {
        'form': form
    })


def razorpay_payment(request, payment_id):

    payment = get_object_or_404(Payment, id=payment_id)

    return render(request, 'training/razorpay_payment.html', {
        'payment': payment
    })


def offline_payment(request, payment_id):

    payment = get_object_or_404(Payment, id=payment_id)

    return render(request, 'training/offline_payment.html',{
        'payment': payment
    })
















