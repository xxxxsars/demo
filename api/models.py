from django.db import models


# Create your models here.
class Predict_log(models.Model):
    production_id = models.CharField(primary_key=True,max_length=20)
    raw_image = models.TextField()
    gray_image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "predict_log"
