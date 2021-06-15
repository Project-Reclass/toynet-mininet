from marshmallow import Schema, fields, ValidationError
from flask_restful import abort
from flask_apispec import marshal_with, MethodResource
from flask import request
from util.error import XMLParseError, TypeCheckError
from toynet.toynet import ToyNet


#Schema definitions
class MiniFlaskTopoPostReq(Schema):
    topology = fields.Str(required=True)


class State():
    toynet_instance = None

    @staticmethod
    def getInstance():
        return State.toynet_instance

    @staticmethod
    def setInstance(instance:ToyNet):
        State.toynet_instance=instance

class MiniFlaskTopo(MethodResource):
    def post(self):
        try:
            req = MiniFlaskTopoPostReq().load(request.form)
        except ValidationError as e:
            abort(400, message='topology not provided')

        try:
            if State.getInstance() is None:
                State.setInstance(ToyNet(filecontent=req['topology']))
                State.getInstance().start()
            else:
                State.getInstance().restart(new_topology=req['topology'])
        except (XMLParseError, TypeCheckError):
            abort(400, message=f'failed to parse XML topology {State.getInstance()}') 
        
        return {
        }, 200
