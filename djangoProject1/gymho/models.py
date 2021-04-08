from django.db import models



# class Execise(models.Model):
#     ExeciseID = models.IntegerField()
#     name = models.CharField(max_length=25)
#     rep_recommend = models.CharField(max_length=10)
#     Active = models.BooleanField(default=True)


class Exercise(models.Model):
    exerciseid = models.IntegerField(db_column='ExerciseID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=25, blank=True, null=True)
    rep_recommend = models.CharField(db_column='Rep recommend', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activate = models.BooleanField(db_column='Activate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Exercise'
