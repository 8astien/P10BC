from rest_framework.serializers import ModelSerializer
from api.models import Project, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'created_at',
            'author',
            'contributors',
            'name',
            'description',
            'type'
        ]


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'created_at',
            'author',
            'contributor',
            'project',
            'name',
            'description',
            'status',
            'priority',
            'tag'
        ]


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'created_at',
            'author',
            'description',
            'project',
            'issue'
        ]
