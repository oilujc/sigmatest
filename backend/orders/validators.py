from rest_framework import serializers


class HasNumbers:

	@staticmethod
	def validate(value):
		hasNumbers = any(char.isdigit() for char in value)

		if len(value) <= 3:
			raise serializers.ValidationError(
				'Este campo debe contener mas de 3 caracteres')

		elif hasNumbers:
			raise serializers.ValidationError(
				'Este campo no puede contener numeros')

		return value
