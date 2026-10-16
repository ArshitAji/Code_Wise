from django.db import models

# Create your models here.
class QuestionDb(models.Model):
    title=models.CharField(max_length=200)
    LANGUAGE_CHOICES=(
        ("python","Python"),
        ("java","Java"),
        ("c++","C++"),
        ("c","C")
    )
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="python")
    DIFFICULTY_CHOICES=(
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )
    difficulty_level=models.CharField(max_length=200,choices=DIFFICULTY_CHOICES,default="easy")
    topic=models.CharField(max_length=200)
    published_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    sample_input=models.TextField(null=True)
    sample_output=models.TextField(null=True)

