
from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from register_projects.models import StudentProject, Payment

from .forms import AdminLoginForm


from .forms import AddPaymentForm

from django.db.models import Sum



def admin_login(request):

    form = AdminLoginForm()

    if request.method == "POST":

        form = AdminLoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('adminpanel:admin_dashboard')

    return render(request, 'adminpanel/login.html', {
        'form': form
    })


@login_required
def admin_dashboard(request):

    total_students = StudentProject.objects.count()

    total_payments = Payment.objects.count()

    return render(request, 'adminpanel/admin_dashboard.html', {
        'total_students': total_students,
        'total_payments': total_payments
    })

@login_required
def projects_list(request):

    total_students = StudentProject.objects.count()

    total_payments = Payment.objects.count()

    students = StudentProject.objects.all()

    return render(request, 'adminpanel/register_list/projects_list.html', {
        'students': students,'total_students': total_students,
        'total_payments': total_payments
    })






@login_required
def add_payment(request, project_id):

    project = get_object_or_404(
        StudentProject,
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

    student = StudentProject.objects.get(id=id)

    payments = student.payments.all()  #reference 

    members = student.members.all()

    return render(request,'adminpanel/student_detail.html',{
        'student': student,
        'payments': payments,
        'members': members
    })

