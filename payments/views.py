from django.http import JsonResponse, HttpResponse
from payments.models import Copun, Factor, Transaction
from random import randint

def my_copun(request, email):
    try:
        copuns = Copun.objects.filter(users__email=email) 
        data = [
            {
                "code": copun.code,
                "exp": copun.expire_date
            }
            for copun in copuns
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def start_trans(request, dargah, fac_id):
    try:
        my_factor = Factor.objects.get(order_id=fac_id)
        gen_id = randint(1000000, 9999999)
        my_trans = Transaction.objects.create(dargah=dargah, trans_id=gen_id, copun=None, factor=my_factor)
        return JsonResponse({
            "dargah": my_trans.dargah,
            "trans_id": my_trans.trans_id,
            "copun": my_trans.copun.code if my_trans.copun else None,
            "factor_id": my_trans.factor.order_id
        })
    except Factor.DoesNotExist:
        return JsonResponse({"error": "Factor not found"}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def add_copun(request, transID, email, code):
    try:
        copun = Copun.objects.get(code=code)
        if copun.users.filter(email=email).exists():  
            my_trans = Transaction.objects.get(trans_id=transID)
            my_trans.copun = copun
            my_trans.save()
            return HttpResponse("Copun added successfully")
        return HttpResponse("Email is wrong", status=400)
    except Copun.DoesNotExist:
        return HttpResponse("Invalid copun", status=404)
    except Transaction.DoesNotExist:
        return HttpResponse("Transaction not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=400)
