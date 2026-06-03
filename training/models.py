from django.db import models


from internship.models import Duration_add,Domain,Intership_mode


class StudentTraining(models.Model):

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('partial', 'Partial'),
        ('completed', 'Completed'),
    )

    name=models.CharField(max_length=30,null=True,blank=True)

    contact_No=models.CharField(max_length=60,null=True,blank=True)

    whatsapp_no=models.CharField(max_length=60,null=True,blank=True)

    email=models.CharField(max_length=90,null=True,blank=True)
    

    

    college_name=models.CharField(max_length=150,null=True,blank=True)

    degree = models.CharField(max_length=150,null=True,blank=True) 

    department_name = models.CharField(max_length=15,null=True,blank=True)  

    

    
    
    created_at = models.DateTimeField(auto_now_add=True)


    

    join_date=models.DateField(null=True,blank=True)

    end_date=models.DateField(null=True,blank=True)

    duration=models.ForeignKey(Duration_add,on_delete=models.CASCADE,null=True,blank=True)

    domain=models.ForeignKey(Domain,on_delete=models.CASCADE,null=True,blank=True)

    intership_mode=models.ForeignKey(Intership_mode,on_delete=models.CASCADE,null=True,blank=True)

    referenceid=models.CharField(max_length=60,null=True,blank=True)

    


    

   

   

    Training_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def total_paid(self):

        return sum(payment.amount for payment in self.payments.all())

    def pending_amount(self):

        if self.project_amount:
            return self.project_amount - self.total_paid()
        return 0

    def __str__(self):
        return self.name



    


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

    training = models.ForeignKey(
        StudentTraining,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

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





