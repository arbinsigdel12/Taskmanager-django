from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)   #cascade le sab delete garxa taile null rakh arko manxe lai task dina
    title=models.CharField(max_length=200,null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)# auto now add le created task ko time show garxa

    def __str__(self):
        return self.title
    
    class Meta:# Meta le ordering garxa aka sort
        ordering=['complete']