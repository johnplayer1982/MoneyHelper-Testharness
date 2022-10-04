from django.db import models
from django.urls import reverse

class Tool(models.Model):

    slug = models.SlugField(default="")
    tool_title = models.CharField(max_length=255, blank=False)
    tool_iframe_url = models.CharField(max_length=255, blank=False)
    tool_iframe_class = models.CharField(max_length=255, blank=True)
    tool_iframe_id = models.CharField(max_length=255, blank=True)
    tool_supporting_script_source = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse("tool_detail", kwargs={"slug": self.slug})
