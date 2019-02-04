from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
# from apps.homepage.urls import urlpatterns as myurls

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    def items(self):
        return ["home", "menu", "menu_images", "about_us", "contact_us", "careers"]

    def location(self, item):
        return reverse(item)
