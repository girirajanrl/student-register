
from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from training.models import StudentTraining, Payment

from .forms import AdminLoginForm


from .forms import AddPaymentForm

from django.db.models import Sum




@login_required
def admin_dashboard(request):

    total_students = StudentTraining.objects.count()

    total_payments = Payment.objects.count()

    return render(request, 'adminpanel/register_list/training_list.html', {
        'total_students': total_students,
        'total_payments': total_payments
    })

@login_required
def training_list(request):

    list_training= StudentTraining.objects.all()

    return render(request, 'adminpanel/register_list/training_list.html', {
        'list_training':list_training
    })






@login_required
def add_payment(request, project_id):

    project = get_object_or_404(
        StudentTraining,
        id=project_id
    )

    payments = Payment.objects.filter(
        project=project
    )

    if request.method == "POST":

        form = AddPaymentForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            form.save()

            return redirect(
                "student_detail",
                id=project.id
            )

    else:
        form = AddPaymentForm(
            instance=project
        )

    total_paid = payments.aggregate(
        total=Sum("paid_amount")
    )["total"] or 0

    total_amount = project.project_amount or 0

    pending_amount = total_amount - total_paid

    context = {
        "form": form,
        "project": project,
        "payments": payments,
        "total_amount": total_amount,
        "total_paid": total_paid,
        "pending_amount": pending_amount
    }

    return render(
        request,
        "adminpanel/add_payment.html",
        context
    )


@login_required
def student_detail(request, id):  # get to keep id  via url

    student = StudentTraining.objects.get(id=id)

    payments = student.payments.all()  #reference 

    members = student.members.all()

    return render(request,'adminpanel/student_detail.html',{
        'student': student,
        'payments': payments,
        'members': members
    })

