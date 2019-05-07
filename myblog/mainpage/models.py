from django.db import models

# 이 파일은 장고와 연동되는 DB를 다루는 부분

class Post(models.Model):
    title= models.CharField(max_length=100)
    date=models.DateField(auto_now_add=False)
    body=models.TextField()


    def __str__(self):
        return self.title


