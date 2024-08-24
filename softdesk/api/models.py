from django.db import models
from django.conf import settings

from authentication.models import User


class Project(models.Model):

    BACK_END = "BACK_END"
    FRONT_END = "FRONT_END"
    IOS = "IOS"
    ANDROID = "ANDROID"

    TYPE_CHOICES = (
        (BACK_END, "Back-end"),
        (FRONT_END, "Front-end"),
        (IOS, "iOS"),
        (ANDROID, "Android"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_projects'
    )
    contributors = models.ManyToManyField(User, related_name='projects')
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)

    def __str__(self):
        return f"Project: {self.name} by {self.author.username}"


class Issue(models.Model):

    # Status
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    # Priority
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    # Tag
    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"

    STATUS_CHOICES = (
        (TO_DO, 'To do'),
        (IN_PROGRESS, 'In progress'),
        (FINISHED, 'Finished')
    )
    PRIORITY_CHOICES = (
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High")
    )
    TAG_CHOICES = (
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (TASK, "Task")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    # Créateur
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_issues",
        null=True
    )
    # Contributeur à qui est assigné l'issue
    contributor = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="attributed_issues",
        null=True,
        # blank=True
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=TO_DO
    )
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=30, choices=TAG_CHOICES)

    def __str__(self):
        return f"Issue: {self.name} (Status: {self.status})"


class Comment(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    description = models.TextField(max_length=2048)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.issue.name}"
