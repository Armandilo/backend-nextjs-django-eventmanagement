import uuid

from django.conf import settings
from django.db import models
from useraccount.models import User
# Create your models here.

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    eventmode = models.CharField(max_length=255)
    streetaddress = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/event')

    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'
