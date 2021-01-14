from rest_framework.serializers import (Serializer,
										ModelSerializer,
										SerializerMethodField,
										ValidationError)

from .models import (Product, Order)

from utils.mailer import Mailer
from .validators import HasNumbers

class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = [
			'public_id',
			'name',
			'image',
			'price',
			'tax',
		]


class OrderSerializer(ModelSerializer):
	product = ProductSerializer(read_only=True)

	class Meta:
		model = Order
		fields = [
			'id',
			'first_name',
			'last_name',
			'email',
			'card_number',
			'total',
			'product',
			'created_at',
		]

		read_only_fields = ['total', 'created_at']

	def create(self, validate_data):

		order = super(OrderSerializer, self).create(validate_data)

		Mailer().sender(subject=f'Nueva orden: {order.pk}',
				template_name='order_success',
				context=validate_data,
				to=[order.email])

		return order

	def validate_first_name(self, value):
		return HasNumbers.validate(value)

	def validate_last_name(self, value):
		return HasNumbers.validate(value)

