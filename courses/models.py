from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(verbose_name='категория', max_length=30)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(verbose_name='курс', max_length=30)
    description = models.TextField(verbose_name='описание курса', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_category')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='course_teacher')
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title


class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(verbose_name='название материала', max_length=30)
    type = models.CharField(verbose_name='тип материала', max_length=30)
    url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

