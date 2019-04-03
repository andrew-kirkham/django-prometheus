from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

class TestModel(ExportModelOperationsMixin('testmodel'), models.Model):
    name = models.CharField(max_length=100, unique=True)
