from django.db import models


class Exercise(models.Model):
    ExerciseID = models.IntegerField()
    name = models.CharField(max_length=25)
    rep_recommend = models.CharField(max_length=10)
    Active = models.BooleanField(default=True)

# class Exercise(models.Model):
#     ExerciseID = models.IntegerField(db_column='ExerciseID', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(max_length=25, blank=True, null=True)
#     Reprecommend = models.CharField(db_column='Reprecommend', max_length=10, blank=True, null=True)
#     # Field name made lowercase. Field renamed to remove unsuitable characters.
#     Activate = models.BooleanField(db_column='Activate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Exercise'
