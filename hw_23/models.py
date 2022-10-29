from marshmallow import ValidationError, fields, Schema, validates_schema

VALID_CMD = ('filter', 'map', 'unique', 'sort', 'limit')

class RequestParams(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values):
        if values['cmd1'] not in VALID_CMD:
            raise ValidationError('cmd1 содержит невалидное значение')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)