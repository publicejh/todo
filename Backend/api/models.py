from django.db import models
from django.conf import settings
import datetime


class Todo(models.Model):
    STATUS_TYPE = (
        (0, '발의'),
        (1, '진행'),
        (2, '완료'),
    )

    PRIORITY_TYPE = (
        (0, '매우 중요'),
        (1, '중요'),
        (2, '보통'),
        (3, '사소'),
        (4, '매우 사소'),
    )

    todo_title = models.CharField(max_length=45, verbose_name='TODO 제목')
    todo_content = models.TextField(verbose_name='TODO 내용')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='기한')
    status = models.IntegerField(choices=STATUS_TYPE, default=STATUS_TYPE[0][0], verbose_name='상태')
    priority = models.IntegerField(choices=PRIORITY_TYPE, verbose_name='중요도')
    is_deleted = models.BooleanField(default=False, verbose_name='삭제 여부')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='작성 시간')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='수정 시간')

    def __str__(self):
        return self.todo_title

    def priority_name(self):
        return self.PRIORITY_TYPE[self.priority][1]

    def deadline_str(self):
        if self.deadline:
            return self.deadline.strftime('%m/%d/%Y %I:%M %p')
        else:
            return ''

    @classmethod
    def get_overdue(cls):
        return cls.objects.filter(is_deleted=False, status__in=[0, 1], deadline__lt=datetime.datetime.now())
