from flask import Blueprint, jsonify
from app.models import ChoData

bp = Blueprint('routes', __name__)

@bp.route('/data', methods=['GET'])
def get_data():
    data = ChoData.query.all()
    result = [{'name': d.name, 'value': d.value, 'timestamp': d.timestamp} for d in data]
    return jsonify(result)