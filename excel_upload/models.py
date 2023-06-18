from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from regression.constants import WEATHER_CHOICE, SEASON_CHOICE, WORKINGDAY_CHOICE
import pandas as pd
from regression.utils import predict_bike_count
import joblib
# Create your models here.

class BikeDataExcel(models.Model):
    season = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)], 
                                         choices=SEASON_CHOICE)
    workingday = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], 
                                             choices=WORKINGDAY_CHOICE)
    weather = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)], 
                                          choices=WEATHER_CHOICE)
    month = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    predict_count = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.season}-({self.predict_count})EA'

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/reg_best_model.pkl')
        self.predict_count = predict_bike_count(model=ml_model, 
                                                season_value=self.season,
                                                workingday_value=self.workingday,
                                                weather_value=self.weather,
                                                month_value=self.month)
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-date']