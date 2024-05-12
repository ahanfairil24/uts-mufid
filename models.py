from django.db import models

# Create your models here.
class Tutorial(models.model):
    title = models.CarField(max_length=99)
    comtent = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title 


        from django.db import models

# Create your models here.
class paramuka(models.model):
    title = models.CarField(max_length=99)
    comtent = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title 


        from django.db import models

# Create your models here.
class belajar(models.model):
    title = models.CarField(max_length=99)
    comtent = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title 