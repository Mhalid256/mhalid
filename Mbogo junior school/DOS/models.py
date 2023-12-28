from django.db import models

# Create your models here.
class student(models.Model):
    GENDER_CHOICES=[("M","Male"),("F","Female"),]
    CLASS_CHOICES=[("P1","P.1"),("P2","P.2"),("P3","P.3"),("P4","P.4"),("P5","P.5"),("P6","P.6"),("P7","P.7"),]
    STREAM_CHOICES=[("EAST","A"),("WEST","B"),]
    TERM_CHOICES=[("1","ONE"),("2","TWO"),("3","THREE"),]
    std_No=models.PositiveIntegerField()
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=4,choices=GENDER_CHOICES)
    std_class=models.CharField(max_length=10,choices=CLASS_CHOICES)
    stream=models.CharField(max_length=20,choices=STREAM_CHOICES)
    term=models.CharField(max_length=20,choices=TERM_CHOICES)
    theme=models.ImageField(null=True,blank=True,upload_to="images/")
    
class reportcard(models.Model):
    SUBJECT_CHOICES=[("MATH","MATHEMATICS"),("ENG","ENGLISH"),("SCIE","SCIENCE"),("SST","SOCIAL STUDIES"),]
    std_No=models.ForeignKey(student, on_delete=models.CASCADE)
    subject=models.CharField(max_length=50,choices=SUBJECT_CHOICES)
    BOT=models.PositiveIntegerField()
    MOT=models.PositiveIntegerField()
    EOT=models.PositiveIntegerField()
    score=models.PositiveIntegerField()
    grade=models.CharField(max_length=30)
    comment=models.CharField(max_length=200)
    initials=models.CharField(max_length=20)
    totalmarks=models.PositiveIntegerField()
    averagemarks=models.PositiveIntegerField()
        
class position(models.Model):
    CLASS_CHOICES=[("P1","P.1"),("P2","P.2"),("P3","P.3"),("P4","P.4"),("P5","P.5"),("P6","P.6"),("P7","P.7"),]
    STREAM_CHOICES=[("EAST","A"),("WEST","B"),]
    DIVISION_CHOICES=[("1","DIV1"),("2","DIV2"),("3","DIV3"),("4","DIV4"),("U","UNGRADED"),]
    std_No=models.ForeignKey(student, on_delete=models.CASCADE)
    std_class=models.CharField(max_length=20,choices=CLASS_CHOICES)
    stream=models.CharField(max_length=30,choices=STREAM_CHOICES)
    aggregates=models.CharField(max_length=30)
    division=models.CharField(max_length=50,choices=DIVISION_CHOICES)
            
class grading(models.Model):
    grade=models.CharField(max_length=20)
    range=models.CharField(max_length=50)
            
        
        
        
        
        
    
   