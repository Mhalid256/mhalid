from django.db import migrations,models

class Migration(migrations.Migration):
    initial = True
    dependences = [

    ]

    Operations = [
       migrations.CreateModel(
           name ='Author',
           fields = [
               ('id', models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
               ('name',models.CharField(max_length=50)),
               ('contact',models.CharField(max_length=10)),
               ('email' ,models.Emailfield(max_length=254)),
               ('birth_date',models.DateField()),
               ('no_of_articles',models.IntegerField()),
               
           ],
       ),
       
   ] 