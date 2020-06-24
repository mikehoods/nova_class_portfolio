from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from api.models import Project, Note
from tastypie.authorization import Authorization

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()
        # fields = ['title', 'code']


class NoteResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')

    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        fields = ['title', 'body']
        filtering = {
            'project': ALL_WITH_RELATIONS
        }