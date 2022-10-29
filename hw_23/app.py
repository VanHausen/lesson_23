from flask import request, jsonify, Blueprint, Flask
from jsonschema import ValidationError

from builder import build_query
from models import BatchRequestParams


app = Flask(__name__)

main_bp = Blueprint('main', __name__)

@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.message), 404
    res = None
    for query in params['queries']:
        res = build_query(
        cmd=query['cmd'],
        value=query['value'],
        data=res,
        )
    return jsonify(res)

if __name__ == '__main__':
    app.run(port=8000)