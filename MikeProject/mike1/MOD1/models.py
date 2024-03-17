from django.db import models
# from django.contrib.auth.models import AbstractUser

class user(models.Model):
    """
    Represents a user in the Mikey's Sacco application.
    """
    person_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    national_id_or_passport = models.CharField(max_length=50, blank=True)
    occupation = models.CharField(max_length=100, blank=True)

    # Financial information (linked to separate models)
    account_number = models.CharField(max_length=20, blank=True)  # Foreign key to Account model

    # Membership and account details (linked to separate models)
    membership_status = models.CharField(max_length=20, choices=[
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('PENDING', 'Pending'),
    ], default='PENDING')

    def get_full_name(self):
        return f'{self.username} {self.middle_name}'

    class Meta:
        db_table = 'users'  # Optional: Custom table name

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"
