from django.db import models
from django.urls import reverse

class Tool(models.Model):

    slug = models.SlugField(default="")
    tool_title = models.CharField(max_length=255, blank=False)
    tool_iframe_url = models.CharField(max_length=255, blank=False)

    def get_absolute_url(self):
        return reverse("tool_detail", kwargs={"slug": self.slug})
