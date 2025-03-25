from ..models import Tag

class TagService():
    def get_tags(self):
        tags = Tag.objects.all()
        return tags
