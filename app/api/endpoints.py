from flask import Blueprint, request, jsonify
from app.services.service_logic import ServiceLogic

api_bp = Blueprint('api', __name__)
service_logic = ServiceLogic()

@api_bp.route('/validate_identity', methods=['POST'])
def validate_identity():
    data = request.json
    if not data or 'identity_data' not in data:
        return jsonify({"error": "El campo 'identity_data' es obligatorio"}), 400

    result = service_logic.validate_identity(data['identity_data'])
    return result

@api_bp.route('/enrollment', methods=['POST'])
def enrollment():
    data = request.json
    if not data or 'user_data' not in data:
        return jsonify({"error": "El campo 'user_data' es obligatorio"}), 400

    result = service_logic.enroll_user(data['user_data'])
    return result

@api_bp.route('/document_management', methods=['POST'])
def document_management():
    data = request.json
    if not data or 'document_data' not in data:
        return jsonify({"error": "El campo 'document_data' es obligatorio"}), 400

    result = service_logic.manage_documents(data['document_data'])
    return result

@api_bp.route('/digital_contracts', methods=['POST'])
def digital_contracts():
    data = request.json
    if not data or 'contract_data' not in data:
        return jsonify({"error": "El campo 'contract_data' es obligatorio"}), 400

    result = service_logic.digital_contracts(data['contract_data'])
    return result

@api_bp.route('/request_status/<request_id>', methods=['GET'])
def request_status(request_id):
    result = service_logic.request_status(request_id)
    return result