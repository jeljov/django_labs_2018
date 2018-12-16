from django.db import models
from django.utils import timezone
from datetime import date

class Audiobook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    narrator = models.CharField(max_length=200, default="unknown")
    length = models.IntegerField(default=0)
    date_released = models.DateField(verbose_name="date of release")

    def __str__(self):
        audiobook_str = "title: " + self.title
        audiobook_str += "\nauthor: " + self.author
        audiobook_str += "\nnarrator: " + self.narrator
        audiobook_str += "\nlength: " + self.pprint_length()
        audiobook_str += "\ndate of release: " + self.pprint_date_released()
        return audiobook_str

    def pprint_length(self):
        hour, min = divmod(self.length, 60)
        return "{}h {}m".format(hour, min)

    def pprint_date_released(self):
        return date.strftime(self.date_released, "%y-%m-%d")


class Review(models.Model):
    comment = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    for_audiobook = models.ForeignKey(to=Audiobook, on_delete=models.CASCADE)

    def __str__(self):
        review_str = "comment: " + self.comment
        review_str += "\nrating: {} stars".format(self.rating)
        review_str += "\nposted on: " + self.format_datetime(self.timestamp)
        return review_str

    @staticmethod
    def format_datetime(a_date):
        to_tz = timezone.get_default_timezone()
        return a_date.astimezone(to_tz).strftime("%y-%m-%d %H:%M")