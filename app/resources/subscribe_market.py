from flask import Response
from flask_restful import Resource, request
from models import *
import re

class SubscribeMarket(Resource):
    def post(self):
        phone = request.form.get('phone')

        if not phone:
            return {'message': 'Не передан телефон', 'code': 'empty_phone'}, 400

        phone = re.sub(r"\D", '', phone)

        if (len(phone) < 11):
            return {'message': 'Некорректный телефон', 'code': 'wrong_phone'}, 400

        subscriber = BrandsRequests.find_first({ 'phone': phone })

        if (subscriber):
            return {'message': 'Заявка уже оформлена', 'code': 'already_exist'}, 400

        subscriber = BrandsRequests(phone)
        subscriber.save()

        return Response(status=200)
