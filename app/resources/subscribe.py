from flask import Response
from flask_restful import Resource, request
from models import *
import re

class Subscribe(Resource):
    def post(self):
        email = request.form.get('email')
        emailRegexp = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"

        if not email:
            return {'message': 'Не передан email', 'code': 'empty_email'}, 400

        if not re.search(emailRegexp, email):
            return {'message': 'Некорректный email', 'code': 'empty_email'}, 400

        subscriber = MailingList.find_first({ 'email': email })
        if (subscriber):
            return {'message': 'Вы уже подписаны', 'code': 'already_exist'}, 400

        subscriber = MailingList(email)
        subscriber.save()

        return Response(status=200)
