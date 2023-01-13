from django.db import models

class get_user_info_one(models.Model):

    string_email = models.CharField(max_length=50)

    string_phon_number = models.CharField(max_length=12,null=True)

    string_date =models.DateField(null=True,blank=True)

    string_text = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.string_date} {self.string_phon_number} {self.string_email} {self.string_text} '