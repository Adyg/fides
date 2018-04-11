from django.db import models
from django.utils import timezone


class Breakpoint(models.Model):
    width = models.IntegerField(default=375)
    height = models.IntegerField(default=812)

    def __str__(self):

        return "{}x{}".format(self.width, self.height)


class Project(models.Model):
    STATUS_CHOICES = (
        ('U', 'Unscraped'),
        ('S', 'Scraped'),
    )    

    name = models.CharField(max_length=100, blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    breakpoint = models.ManyToManyField(Breakpoint)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='U')
    codename = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):

        return "{} ({})".format(self.name, self.url)

    @classmethod
    def get_project_for_scraping(cls):
        project = cls.objects.filter(status='U')[:1]
        if project: 
            return project[0]

        return False


class ProjectPage(models.Model):
    url = models.URLField(blank=False, null=False, unique=True)
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):

        return "{}".format(self.url)

    @classmethod
    def create(cls, project, url):
        page = False

        try:
            page = cls.objects.create(project=project, url=url)
        except:
            pass

        if page:
            print(page.url)
            return True

        return False


