from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    curse=models.CharField(max_length=30,blank=True,null=True)
    first_mark=models.FloatField(blank=True,null=True)
    second_mark=models.FloatField(blank=True,null=True)
    third_mark=models.FloatField(blank=True,null=True)
    homework=models.FloatField(blank=True,null=True)
    average_mark=models.FloatField(blank=True,null=True)
    comments=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name