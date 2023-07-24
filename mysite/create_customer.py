import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from pagination.models import Customer
for i in range(1,1000,1):
    Customer.objects.create(name='Alfreds Futterkista', country ='Germany')
    Customer.objects.create(name='Ana Trujillo y Helados', country ='Mexico')
    Customer.objects.create(name='Ha Noi', country ='Vietnam')
    Customer.objects.create(name='Tokyo', country ='Japan')
    Customer.objects.create(name='WangDong', country ='China')
    Customer.objects.create(name='Bang Kok', country ='ThaiLand')
    Customer.objects.create(name='Bon app', country ='France')
    Customer.objects.create(name='Chicago', country ='America')
    Customer.objects.create(name='Manchester', country ='England')
    Customer.objects.create(name='Mascova', country ='Russia')
    Customer.objects.create(name='Seoul', country ='Korean')