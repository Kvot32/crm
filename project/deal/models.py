from django.db import models
from client.models import Contact
from profile.models import Profile


class Deal(models.Model):
    STAGE_CHOICES = (
        ('new', 'Новая'),
        ('pending', 'В ожидании'),
        ('approved', 'Одобрена'),
        ('rejected', 'Отклонена'),
        ('closed', 'Закрыта'),
    )

    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='new')
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='deals_created')
    assigned_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='deals_assigned', blank=True,
                                    null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.stage}'
