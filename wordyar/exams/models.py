from django.db import models
from accounts.models import Account
from core.models import BaseModel
from django.utils.translation import gettext as _



q_choice = [("0", "easy"), ("1", "normal"), ("2", "hard"),]
# Create exams models including Exam, Question, Answer.

class Exam(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    false_answer = models.IntegerField()
    true_answer = models.IntegerField()

    def score(self):
        result = (((self.true_answer*3)-self.false_answer)/((self.true_answer+self.false_answer)*3))*100
        return result

    def __str__(self) -> str:
        return f"score: {self.score()}"

    class Meta:
        verbose_name_plural, verbose_name = _("exam"), _("exams")


class Question(BaseModel):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    q_level = models.CharField(choices=q_choice, max_length=1, null=True, default=None)
