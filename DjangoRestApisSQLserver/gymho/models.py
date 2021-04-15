from django.db import models


class Exercise(models.Model):
    ExerciseID = models.IntegerField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=25)
    rep_recommend = models.CharField(max_length=10)
    Activate = models.BooleanField(db_column='Activate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exercise'
