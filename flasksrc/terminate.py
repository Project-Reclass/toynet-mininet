from marshmallow import Schema, fields, ValidationError
from flask_restful import abort
from flask_apispec import marshal_with, MethodResource, use_kwargs
from toynet.toynet import ToyNet
from toynet.state import State


#Schema definitions
class MiniFlaskTerminatePostReq(Schema):
    terminate = fields.Bool(required=True)


class MiniFlaskTerminatePostResp(Schema):
    terminated = fields.Bool()


class MiniFlaskTerminate(MethodResource):
    @use_kwargs(MiniFlaskTerminatePostReq)
    @marshal_with(MiniFlaskTerminatePostResp)
    def post(self, **kwargs):
        try:
            req = MiniFlaskTerminatePostReq().load(kwargs)
        except ValidationError as e: #no required fields- shouldn't get thrown
            abort(400, message='invalid terminate request')
        
        res = False

        try:
            if req['terminate']:
                State.getInstance().stop()
                State.setInstance(None)
                res = True
        except Exception as e:
            abort(500, message='terminate request failed')

        return {
            'terminated': res
        }, 200