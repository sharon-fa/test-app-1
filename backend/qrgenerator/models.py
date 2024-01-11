from django.db import models

# Create your models here.
class QRCodeData(models.Model):
    data_text = models.TextField()
    qr_code_image = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return self.data_text