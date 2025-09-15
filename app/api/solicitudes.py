from flask import Blueprint, jsonify

solicitudes_bp = Blueprint('solicitudes', __name__)

@solicitudes_bp.route('/request_status/<request_id>', methods=['GET'])
def request_status(request_id):
    # Implementar lógica para obtener el estado de solicitudes
    return jsonify({"request_id": request_id, "status": "Estado de la solicitud"}), 200