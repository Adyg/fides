from django.db import models
from django.utils import timezone


class Breakpoint(models.Model):
    width = models.IntegerField(default=375)
    height = models.IntegerField(default=812)

    def __str__(self):

        return "{}x{}".format(self.width, self.height)


class Project(models.Model):
    WIZARD_STEPS = (
        ('BSD', 'Basic Site Details'),
        ('SS', 'Scraping Started'),
        ('S', 'Scraped'),
        ('AP', 'Add Pages'),
        ('PVA', 'Pre-Visual Assesment'),
        ('BID', 'Building Initial Dataset')
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    breakpoint = models.ManyToManyField(Breakpoint)
    created_at = models.DateTimeField(default=timezone.now)
    wizard_step = models.CharField(max_length=10, choices=WIZARD_STEPS, default='BSD')
    codename = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):

        return "{} ({})".format(self.name, self.url)

    @classmethod
    def get_project_for_scraping(cls):
        project = cls.objects.filter(wizard_step='BSD')[:1]
        if project: 
            return project[0]

        return False


    def is_scraped(self):

        return self.wizard_step in ['S', 'AP', 'PVA', 'BID']


    def mark_scraping_started(self):
        self.wizard_step = 'SS'
        self.save()


    def mark_scraping_finished(self):
        self.wizard_step = 'S'
        self.save()


    def bulk_add_pages(self, urls):
        if isinstance(urls, str):
            urls = urls.split('\n')

        for url in urls:
            self.add_page(url)

    def add_page(self, url):
        ProjectPage.create(self, url)


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


class ProjectPagePrevisualAssesment(models.Model):
    url_pattern = models.TextField(blank=False, null=False)
    js_code = models.TextField(blank=False, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    test_original = models.BooleanField(default=True)

    def __str__(self):

        return "{} - {}".format(self.project.name, self.url_pattern)
