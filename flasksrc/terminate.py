from marshmallow import Schema, fields, ValidationError
from flask_restful import abort
from flask_apispec import marshal_with, MethodResource
from flask import request
from toynet.toynet import ToyNet
import docker


#Schema definitions
class MiniFlaskTerminatePostReq(Schema):
    terminate = fields.Bool()


class MiniFlaskTerminate(MethodResource):
    def post(self):
        try:
            req = MiniFlaskTerminatePostReq().load(request.form)
        except ValidationError as e: #no required fields- shouldn't get thrown
            abort(400, message='invalid terminate request')

        try:
            client = docker.from_env()
            print(client.containers.list())
            container = client.containers.list()[0]
            container.stop()
        except Error as e:
            pass
