from flask import Blueprint, request, jsonify, render_template

enrolamiento_bp = Blueprint('enrolamiento', __name__)

@enrolamiento_bp.route('/enrollment', methods=['POST'])
def enrollment():
    data = request.json
    # Implementar lógica de enrolamiento
    return jsonify({"message": "Enrolamiento exitoso", "data": data}), 201

@enrolamiento_bp.route('/enrollment-form', methods=['GET'])
def enrollment_form():
    return render_template('enrollment_form.html')