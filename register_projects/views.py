from django.shortcuts import render, redirect, get_object_or_404

from django.forms import modelformset_factory

from .models import StudentProject, TeamMember,Payment

from .forms import StudentProjectForm, PaymentForm

from django.db.models import Sum


def project_register(request):

    form = StudentProjectForm()

    if request.method == "POST":

        form = StudentProjectForm(request.POST)

        if form.is_valid():

            project = form.save()

            return redirect('projects:team_members', project.id)  # pass id to team member

    return render(request, 'projects/register.html', {'form': form})


def team_members(request, project_id):

    project = get_object_or_404(StudentProject, id=project_id)

    TeamFormSet = modelformset_factory(

        TeamMember,
        fields=(
            'member_name',
            'member_contact',
            'member_email',
          
        ),
        extra=project.team_members
    )

    formset = TeamFormSet(queryset=TeamMember.objects.none())

    if request.method == "POST":

        formset = TeamFormSet(request.POST)

        if formset.is_valid():

            members = formset.save(commit=False)

            for member in members:

                member.project = project

                member.save()

            return redirect('projects:payment_page', project.id)  #pass the id payment

    return render(request, 'projects/team_members.html', {
        'formset': formset
    })

from django.db.models import Sum

def payment_page(request, project_id):

    project = get_object_or_404(
        StudentProject,
        id=project_id
    )

    form = PaymentForm()

    if request.method == "POST":

        form = PaymentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            payment = form.save(commit=False)

            payment.project = project

            total_amount = project.project_amount or 0

            total_paid = Payment.objects.filter(
                project=project
            ).aggregate(
                total=Sum("paid_amount")
            )["total"] or 0

            current_paid = payment.paid_amount or 0

            payment.pending_amount = (
                total_amount - (
                    total_paid + current_paid
                )
            )

            payment_mode = form.cleaned_data[
                "payment_mode"
            ]

            payment.save()

            if payment_mode == "online":
                return redirect(
                    "projects:razorpay_payment",
                    payment.id
                )

            elif payment_mode == "offline":
                return redirect(
                    "projects:offline_payment",
                    payment.id
                )

    return render(
        request,
        "projects/payment.html",
        {
            "form": form
        }
    )

def razorpay_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)

    members = TeamMember.objects.filter(project=payment.project)

    return render(request, 'projects/razorpay_payment.html', {
        'payment': payment, 
        'members': members
    })

def offline_payment(request, payment_id):

    payment = get_object_or_404(Payment, id=payment_id)

    return render(request, 'projects/offline_payment.html',{
        'payment': payment
    })


def home_page(request):

    return render(request,'projects/home_page.html')
