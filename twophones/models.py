from django.db import models
from django.utils import timezone

class ThingEntry(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    thing_of_which_i_have_two = models.CharField(max_length=100)
    reason_one = models.CharField(max_length=200)
    reason_two = models.CharField(max_length=200)
    submitted_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def submit(self):
        self.submitted_date = timezone.now()
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.thing_of_which_i_have_two

    def put_it_all_together(self):
        return "I got two " + self.thing_of_which_i_have_two + " one for " + self.reason_one + " and one for " + \
               self.reason_two