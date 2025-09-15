from flask import Blueprint, request, jsonify
import uuid  # Para generar un ID único

documentos_bp = Blueprint('documentos', __name__)

# Simular almacenamiento de documentos
document_storage = []

@documentos_bp.route('/documents', methods=['POST'])
def document_management():
    data = request.json

    # Validar que el campo 'document' esté presente
    if not data or 'document' not in data:
        return jsonify({"error": "El campo 'document' es obligatorio"}), 400

    # Validar que el documento no esté vacío
    document = data['document']
    if not document.strip():
        return jsonify({"error": "El documento no puede estar vacío"}), 400

    # Validar tamaño del documento (mínimo 5 caracteres)
    if len(document) < 5:
        return jsonify({"error": "El documento debe tener al menos 5 caracteres"}), 400

    # Generar un ID único para el documento
    document_id = str(uuid.uuid4())

    # Simular almacenamiento del documento
    document_storage.append({"id": document_id, "content": document})

    return jsonify({
        "message": "Documento gestionado exitosamente",
        "document_id": document_id,
        "document": document
    }), 200