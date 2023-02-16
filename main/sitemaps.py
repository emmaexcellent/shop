from django.contrib.sitemaps import Sitemap
from product.models import *
from vendor.models import *
from .models import *


class ProductSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.5
	protocol = 'http'

	def items(self):
		return Product.objects.all()

	def lastmod(self, obj):
		return obj.date	


class CategorySitemap(Sitemap):
	changefreq = "daily"
	priority = 0.5
	protocol = 'http'

	def items(self):
		return Category.objects.all()

class VendorSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.5
	protocol = 'http'

	def items(self):
		return Vendor.objects.all()
