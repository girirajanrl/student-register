from django.db import models

from django.db.models import Sum


class StudentProject(models.Model):

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('partial', 'Partial'),
        ('completed', 'Completed'),
    )

    project_title=models.CharField(max_length=500,null=True,blank=True)

    college_name = models.CharField(max_length=150)
     
    project_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    department = models.CharField(max_length=100)

    domain = models.CharField(max_length=100)

    reference_no=models.CharField(max_length=100)

    

    team_members = models.PositiveIntegerField(default=1)

    

    
    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
     
    @property
    def total_paid(self):

        total = self.payments.aggregate(
            total=Sum('paid_amount')
        )['total']

        return total or 0

    @property
    def pending_balance(self):

        return (self.project_amount or 0) - self.total_paid
    
    def __str__(self):
        return self.project_title
    
    @property
    def payment_status(self):

        if self.total_paid == 0:
            return "Pending"

        elif self.total_paid < self.project_amount:
            return "Partial"

        else:
            return "Completed"


class TeamMember(models.Model):
    
    project = models.ForeignKey(
        StudentProject,
        on_delete=models.CASCADE,
        related_name="members"
    )

    member_name = models.CharField(max_length=100)

    member_contact = models.CharField(max_length=15)

    member_email = models.EmailField()

    



    def __str__(self):
        return self.member_name


class Payment(models.Model):
    PAYMENT_MODE = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )

    VERIFY_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    project = models.ForeignKey(
        StudentProject,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    


    paid_amount =models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)



    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_MODE
    )

    transaction_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    payment_proof = models.FileField(
        upload_to='payment_proof/',
        blank=True,
        null=True
    )

    verify_status = models.CharField(
        max_length=20,
        choices=VERIFY_STATUS,
        default='pending'
    )
 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name