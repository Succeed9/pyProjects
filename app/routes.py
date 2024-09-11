from flask import Blueprint, jsonify
from app.models import status_studenta

bp = Blueprint('routes', __name__)


@bp.route('/', methods=['GET'])
def get_data():
    data = status_studenta.query.all()
    result = [d.__dict__ for d in data]

    # Убираем служебную информацию
    for item in result:
        item.pop('_sa_instance_state', None)

    return jsonify(result)
    
