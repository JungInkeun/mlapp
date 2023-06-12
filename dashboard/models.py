from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER_CHOICE = (
    (0, 'Female'),
    (1, 'Male'),
)

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(13), MaxValueValidator(19)],null=True)
    height = models.PositiveIntegerField(null=True)
    sex = models.PositiveIntegerField(choices=GENDER_CHOICE, null=True)
    predict = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.predict}'
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_sport_model.joblib')
        self.predict = ml_model.predict([[self.age, self.height, self.sex]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']