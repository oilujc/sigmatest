from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (Product, Order)
from .serializers import (ProductSerializer, OrderSerializer)
from utils.mailer import Mailer
import datetime

class OrderViewset(viewsets.ModelViewSet):

	serializer_class = OrderSerializer

	def get_queryset(self):
		return Order.objects.all()

	def create(self, request):
		try:
			product = request.data['product']
			product['public_id'] = product.pop('id')
			product = Product.objects.get(public_id=product.get('public_id'))
		except Product.DoesNotExist:
			product = Product.objects.create(**product)
		except KeyError:
			return Response({'product':['Este campo es requerido.']}, status=status.HTTP_400_BAD_REQUEST)

		tax = product.tax
		discount = 0

		if product.public_id == 1:
			if datetime.datetime.now().hour % 2 == 0:
				discount = product.price * 0.20

		elif product.public_id == 2:
			tax = 0

		total = product.price + tax - discount

		print(product.price, tax, discount)

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(product=product, total=total)

		headers = self.get_success_headers(serializer.data)

		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
