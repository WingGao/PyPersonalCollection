from django.db import models


class CTag(models.Model):
    name = models.CharField(max_length=250, unique=True, db_index=True)

    def to_dict(self):
        return {'tid': self.id, 'name': self.name}


class CItem(models.Model):
    MANGA = 'MA'
    ANIME = 'AM'
    AV = 'AV'
    TYPE_CHOICES = (
        (MANGA, 'manga'),
        (ANIME, 'anime'),
        (AV, 'av'),
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    title = models.CharField(max_length=250, db_index=True)
    author = models.CharField(max_length=250, null=True)
    img = models.URLField()
    score = models.IntegerField()
    url = models.URLField(unique=True)
    tags = models.ManyToManyField(CTag)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'img': self.img,
                'score': self.score, 'url': self.url, 'tags': [i.id for i in self.tags.all()],
                'type': self.get_type_display()}

def get_item_type(tname):
    for i in CItem.TYPE_CHOICES:
        if i[1] == tname:
            return i[0]
    return None


def objs_to_list(objs):
    return [i.to_dict() for i in objs]


def get_tags_by_id(ids):
    return [CTag.objects.get(id=i) for i in ids]