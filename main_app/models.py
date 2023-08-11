from django.db import models
from django.urls import reverse
from datetime import date

BATHS = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening'),
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})
  
class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(finch):
        return f'{finch.name} ({finch.type})'

    def get_absolute_url(finch):
        return reverse('detail', kwargs={'finch_id': finch.id})
    
    def bathed_for_today(finch):
        return finch.bathing_set.filter(date=date.today()).count() >= len(BATHS)
    
class Bathing(models.Model):
    date = models.DateField('bathing date')
    bath = models.CharField(
        max_length=1,
        choices=BATHS,
        default=BATHS[0][0]
    )
    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.get_bath_display()} on {self.date}'    
    
    class Meta:
        ordering = ['-date']