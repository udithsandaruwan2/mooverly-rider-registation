import uuid
from django.db import models
import os


class Application(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    
    VERIFICATION_TYPE_CHOICES = [
        ('Passport', 'Passport'),
        ('Driving License', 'Driving License'),
        ('National ID', 'National ID'),
        
    ]
    
    WORKING_TYPE = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time')
    ]

    # Personal Details
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    nic = models.CharField(max_length=12, blank=True, null=True)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10, 
        choices=GENDER_CHOICES, 
        blank=True, 
        null=True, 

    )
    mobile_number_1 = models.CharField(
        max_length=15, 
        blank=True, null=True
    )
    mobile_number_2 = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
    )
    whatsapp_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 

    )

    # Address
    address_line_1 = models.CharField(max_length=200, blank=True, null=True)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    address_line_3 = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    working_type = models.CharField(max_length=50,choices=WORKING_TYPE, blank=True, null=True)
    possible_working_hours = models.CharField(max_length=50, blank=True, null=True)

    # Verification
    verification_type = models.CharField(
        max_length=50, 
        choices=VERIFICATION_TYPE_CHOICES, 
        blank=True, 
        null=True
    )
    verification_document_number = models.CharField(max_length=100, blank=True, null=True)

    def upload_to_front(instance, filename):
        folder_name = instance.verification_document_number or instance.uuid
        return os.path.join(f'documents/{folder_name}/front_side/', filename)

    def upload_to_back(instance, filename):
        folder_name = instance.verification_document_number or instance.uuid
        return os.path.join(f'documents/{folder_name}/back_side/', filename)

    front_side_document = models.ImageField(upload_to=upload_to_front, blank=True, null=True)
    back_side_document = models.ImageField(upload_to=upload_to_back, blank=True, null=True)
    
    def upload_to_video(instance, filename):
        folder_name = instance.verification_document_number or instance.uuid
        return os.path.join(f'documents/{folder_name}/videos/', filename)

    video = models.FileField(upload_to=upload_to_video, blank=True, null=True)

    # Meta Fields
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return str(self.uuid)
