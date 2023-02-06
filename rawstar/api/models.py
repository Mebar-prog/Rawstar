from django.db import models

# Create your models here.
class Contestent(models.Model):
  image = models.ImageField(upload_to='singers/',blank=True,null=True)
  name = models.CharField(max_length=100,verbose_name='name')
  voterid = models.IntegerField(verbose_name='voterid')
  dzongkhag = models.CharField(max_length=100,verbose_name='dzongkhag')

  def __str__(self):
    return self.name

class AmountReceived(models.Model):
    contestent_id = models.ForeignKey(Contestent, on_delete=models.CASCADE,verbose_name='contestent_id')
    jrnlno = models.IntegerField(verbose_name='jrnlno',unique=True)
    amount = models.IntegerField(verbose_name='amount')
    date = models.CharField(max_length=100,verbose_name='date')

    def __str__(self):
      return self.contestent_id.name

    





