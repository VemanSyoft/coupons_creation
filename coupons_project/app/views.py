from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializers import CouponSerializer
from .models import Coupon,CheckoutItem
from datetime import datetime
from .helper import get_current_date_time,format_date


class CouponAPI(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    http_method_names = ["post", "get", "delete", "put", "head", "options"]

    def create(self,request,*args, **kwargs):
        try:
            try:
                Coupon.objects.get(code=request.data["code"],discount=request.data["discount"]
                ,status=request.data["status"])
                return Response({f"Coupon already exist"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as err:
                pass

            coupon = Coupon(
                code=request.data["code"],
                service=request.data["service"],
                start_data=request.data["start_data"],
                end_data=request.data["end_data"],
                discount=request.data["discount"],
                limit=request.data["limit"],
                used=request.data["used"],
                status=request.data["status"],
            )
            coupon.save()
            return Response(self.serializer_class(coupon).data, status=status.HTTP_201_CREATED)
        except Exception as err:
            print("ERROR :",err)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            coupon_list = Coupon.objects.filter(status=True)
            serializer = CouponSerializer(coupon_list,many=True) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            print("ERROR :",err)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            coupon_obj = Coupon.objects.get(
                id=kwargs["pk"], status=True
            )
            serializer = self.serializer_class(coupon_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            print("ERROR :",err)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            coupon_obj = Coupon.objects.get(
                id=kwargs["pk"], status=True
            )
            coupon_obj.status = False
            coupon_obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            print("ERROR :",err)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckoutCart(viewsets.ModelViewSet):
    http_method_names = ["post", "head", "options"]

    def create(self,request,*args, **kwargs):
        try:
            currency = request.data["currency"],
            amont = request.data["amont"]
            coupon_obj = Coupon.objects.get(code=request.data["code"],status=True)  
            current_date_time = get_current_date_time()
            coupon_start_date = format_date(coupon_obj.start_data)
            coupon_end_date = format_date(coupon_obj.end_data)
            if  current_date_time>=coupon_start_date and current_date_time<=coupon_end_date:
                if coupon_obj.limit>=coupon_obj.used: #one more condition comes here that If user already redeamed the coupon
                    quotient = 1 / coupon_obj.discount
                    discounted_price = quotient*100
                    #Call payment function here
                    return Response({f"discounted price is:{discounted_price}"},status=status.HTTP_200_OK)
                else:
                    Response({f"Coupon limit reached"},status=status.HTTP_400_BAD_REQUEST)
            else:
                Response({f"Coupon expired"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print("ERROR :",err)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


