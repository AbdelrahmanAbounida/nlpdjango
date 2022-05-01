from statistics import mode
from django.db import models

# Create your models here.

class Choices(models.Model):

    LANG_CHOICES = [
         ( "eng",'English'),
         ( "bg",'Bulgarian'),
         ( "de",'German'),
         ( "fr",'French'),
         ( "es",'Spanish'),
    ]
    MOD_CHOICES = [
        ( "en_core_web_lg","spaCy's English Large"),
        ( "gpt-j",'GPT-J'),
        ( "fast-gpt-j",'Fast GPT-J'),
        ("fr_core_news_lg","spaCy's French Large"),
        ("bart-large-cnn","Bart-Large-CNN"),
        ("roberta-base-squad2","Roberta Base Squad 2"),

    ]

    api_tocken = models.CharField(max_length=200)
    language = models.CharField(max_length=100, choices=LANG_CHOICES, default='English')
    model = models.CharField(max_length=100, choices=MOD_CHOICES, default='Bart-Large-CNN')
    use_gpu = models.BooleanField(null=True,default=False)
    inpt_string = models.TextField(default='')
    question = models.TextField(default='')