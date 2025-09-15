from flask import Blueprint, request, jsonify
import uuid  # Para generar un ID único

contratos_bp = Blueprint('contratos', __name__)

@contratos_bp.route('/contracts', methods=['POST'])
def digital_contracts():
    data = request.json

    # Validar que el campo 'contract_data' esté presente
    if not data or 'contract_data' not in data:
        return jsonify({"error": "El campo 'contract_data' es obligatorio"}), 400

    contract_data = data['contract_data']

    # Simular la creación de un contrato digital
    contract_id = str(uuid.uuid4())  # Generar un ID único para el contrato

    return jsonify({
        "message": "Contrato digital creado exitosamente",
        "contract_id": contract_id,
        "contract_data": contract_data
    }), 201