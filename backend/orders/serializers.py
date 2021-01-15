from rest_framework.serializers import (Serializer,
										ModelSerializer,
										SerializerMethodField,
										ValidationError)

from .models import (Product, Order)

from utils.mailer import Mailer
from .validators import HasNumbers

class ProductSerializer(ModelSerializer):
	discount = SerializerMethodField()
	discount_rate = SerializerMethodField()
	total = SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			'public_id',
			'name',
			'image',
			'price',
			'tax',
			'discount',
			'discount_rate',
			'total'
		]

		read_only_fields = ['discount', 'discount_rate', 'total']

	def get_discount(self, obj):
		return self.context.get("discount", 0)

	def get_discount_rate(self, obj):
		return self.context.get("discount_rate", 0)

	def get_total(self, obj):
		return self.context.get("total", 0)


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
				context={**validate_data, "created_at": order.created_at},
				to=[order.email])

		return order

	def validate_first_name(self, value):
		return HasNumbers.validate(value)

	def validate_last_name(self, value):
		return HasNumbers.validate(value)

