from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text


class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice A, choice B
    choice = models.CharField(max_length=1, default='A')
    choice_text = models.CharField(max_length=300)
    voters = models.ManyToManyField(User)

    def __str__(self):
        return self.choice_text


