from django.db import models
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    stock_quan = models.DecimalField(decimal_places=0, max_digits=5)
    desc = models.TextField()
    posted_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.posted_date = timezone.now()
        self.save()

    # name 필드를 반환하는 메서드
    # 코드가 없다면 Post Object라고 나옴
    def __str__(self):
        return self.name

