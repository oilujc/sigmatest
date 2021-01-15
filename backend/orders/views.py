import datetime
import requests
from rest_framework import status, views, viewsets
from rest_framework.response import Response
from utils.mailer import Mailer
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer
from django.utils import timezone


def validateProductId(product):
	tax = product.tax
	discount = 0
	discount_rate = 0

	# Validacion de product id para calculo de tax y descuento
	if product.public_id == 1:
		if datetime.datetime.now().hour % 2 != 0:
			discount_rate = 0.20
			discount = product.price * discount_rate

	elif product.public_id == 2:
		tax = 0

	total = product.price + tax - discount

	return tax, discount, discount_rate, total


class ProductView(views.APIView):
	def get(self, request, format=None):

		req = requests.get("http://sigmatest.sigmastorage.online/")
		if req.status_code == 200:
			data = req.json()

			# Validacion de producto, se verifica si existe el producto en la peticion,
			# si existe se evalua si se encuentra almacenado en la db, si no, se registra el producto
			try:
				product = Product.objects.get(public_id=data.get('id'))
			except Product.DoesNotExist:
				data['public_id'] = data.pop('id')
				product = Product.objects.create(**data)

			tax, discount, discount_rate, total = validateProductId(
				product)

			serializer = ProductSerializer(
				product, context={'discount': discount, 'discount_rate': discount_rate, 'total': total})
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response({"error": "Request failed"}, status=status.HTTP_400_BAD_REQUEST)


class OrderViewset(viewsets.ModelViewSet):

	serializer_class = OrderSerializer

	def get_queryset(self):
		return Order.objects.all()

	def create(self, request):

		try:
			product = request.data['product']
			product = Product.objects.get(public_id=product.get('public_id'))
		except Product.DoesNotExist:
			return Response({'product': ['Producto invalido.']}, status=status.HTTP_400_BAD_REQUEST)
		except KeyError:
			return Response({'product': ['Este campo es requerido.']}, status=status.HTTP_400_BAD_REQUEST)

		tax, discount, discount_rate, total = validateProductId(product)

		print(total, tax, discount, product.price, product.public_id,
			  datetime.datetime.now().hour, timezone.now())

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(product=product, total=total)

		headers = self.get_success_headers(serializer.data)

		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
