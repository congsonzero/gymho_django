from django.contrib.auth.models import AbstractUser
from django.db import models


class Exercise(models.Model):
    ExerciseID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    rep_recommend = models.CharField(max_length=10)
    Activate = models.BooleanField(db_column='Activate')

    class Meta:
        managed = False
        db_table = 'Exercise'


class Login(AbstractUser):
    last_name = None
    first_name = None
    last_login = None
    date_joined = None
    is_active = True
    is_superuser = None
    Login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=320, unique=True)
    is_staff = models.BooleanField(db_column='admin')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        managed = False
        db_table = 'Login'

    def __str__(self):
        return self.email


class ExerciseProgram(models.Model):
    ExerciseProgramID = models.IntegerField(db_column='ExerciseProgramID', primary_key=True)
    Expect = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Exercise Program'


class Customer(models.Model):
    User_id = models.AutoField(primary_key=True, db_column='UserID')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=128)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()

    # ExerciseProgram = models.OneToOneField(ExerciseProgram, on_delete=models.CASCADE,null =True)

    Login = models.OneToOneField(Login, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'customer'


class Todo(models.Model):
    TodoID = models.IntegerField(primary_key=True, db_column='TodoID')
    User = models.ForeignKey(Customer, db_column='UserID', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Todo'
