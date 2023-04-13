from .cart import Cart



def cart(request):
    total_amt=0
    if request.session:
        if 'cartdata' in request.session:
            for p_id,item in request.session['cartdata'].items():
                total_amt+=int(item['qty'])*float(item['price'])
            return {'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt}
        else:
            return {'cart_data':'','totalitems':0,'total_amt':total_amt}  
     
