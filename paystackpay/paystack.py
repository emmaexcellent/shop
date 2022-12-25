from django.conf import settings
import requests


class PayStack:
	PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
	base_url = 'https://api.paystack.co'

	def verify_payment(self, ref, *args, **kwargs):
		path = f'/transaction/verify/{ref}'.format(ref)

		headers = {
			"Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
			'Content-Type': 'application/json',
		}
		url = "{}{}".format(self.base_url, path)

		response = requests.get(url, headers=headers)

		response_data = response.json()

		if response.status_code == 200:
			response_data ==response.json()
			return response_data['status'], response_data['data']
			
		response_data = response.json()
		return response_data["status"], response_data["message"]
