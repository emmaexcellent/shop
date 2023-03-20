from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Avg,Count
from django.http import JsonResponse
from main.models import *
from .models import *
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

	related = Product.objects.filter(category = p.category_id).exclude(id=p.id)	
	trend = Product.objects.order_by('-topic_views')[:4]	
	review = Review.objects.filter(product=p, rating='5')[:1]

	if Review.objects.filter(product=p).count() > 0:	
		p.avg_ratings = Review.objects.filter(product=p).aggregate(Avg('rating'))['rating__avg']
		p.save()
	
	return render(request, 'product.html',{'p':p,'related':related,'trend':trend,'form':form, 'review':review})	

def listsub_cat(request):
	cat_id = request.GET.get('id')
	sub_cat = SubCategory.objects.filter(category_id= cat_id)
	return render(request,'add-subcat.html', {'sub_cat':sub_cat})			


