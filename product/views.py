from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Avg,Count
from .forms import *

# Create your views here.

def detail(request,id,slug,category_title):
	p = get_object_or_404(Product, pk=id)
	p.topic_views = p.topic_views+1
	p.save()
	form = ReviewAdd()
	if request.method == 'POST':
		review=Review.objects.create(
			user=request.user,
			product=p,
			text=request.POST.get('text'),
			rating=request.POST.get('rating'),
			)

	related = Product.objects.filter(category = p.category_id)	
	trend = Product.objects.order_by('-topic_views')[:4]	

	if Review.objects.filter(product=p).count() > 0:	
		avg_reviews=Review.objects.filter(product=p).aggregate(avg_rating=Avg('rating'))
		return render(request, 'product.html',{'p':p,'avg_reviews':avg_reviews,'related':related,'trend':trend,'form':form})

	else:
	
		return render(request, 'product.html',{'p':p,'related':related,'trend':trend,'form':form})


