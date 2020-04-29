from django.db import models

# Create your models here.    
class Stoppage(models.Model):
    name = models.CharField(max_length=100, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
    
class Bus(models.Model):
    name = models.CharField(max_length=100, default='')
    route_no = models.CharField(max_length=100, default='', blank=True)
    bus_type = models.IntegerField(default=0)   #0 for sitting, 1 for local
    start = models.ForeignKey(Stoppage, on_delete=models.CASCADE, related_name='start')
    stop = models.ForeignKey(Stoppage, on_delete=models.CASCADE, related_name='stop')
    
    def __str__(self):
        return self.name
    
class Next(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    current = models.ForeignKey(Stoppage, on_delete=models.CASCADE, related_name='current')
    next = models.ForeignKey(Stoppage, on_delete=models.CASCADE, related_name='next')
    
    def __str__(self):
        return self.bus.name + ' ' + self.current.name + ' ' + self.next.name
    