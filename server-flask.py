# GYM TRACKER - Servidor Python/Flask
# pip install flask flask-cors python-dotenv

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Simular base de datos en memoria
trainings = {}
users = set()

# Configuración
AUTH_TOKEN = os.getenv('AUTH_TOKEN', 'token-secreto-123')

# Middleware de autenticación
def check_auth():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not token or token != AUTH_TOKEN:
        return False
    return True

@app.route('/api/entrenamientos', methods=['POST'])
def sync_training():
    """Recibe entrenamientos desde Gym Tracker"""
    if not check_auth():
        return jsonify({'error': 'Token inválido o ausente'}), 401

    try:
        data = request.get_json()
        user_code = data.get('userCode')
        entrenamiento = data.get('entrenamiento')
        timestamp = data.get('timestamp')

        if not user_code or not entrenamiento:
            return jsonify({'error': 'Datos incompletos'}), 400

        # Registrar usuario
        users.add(user_code)

        # Guardar entrenamiento
        if user_code not in trainings:
            trainings[user_code] = []

        training_record = {
            'id': len(trainings[user_code]) + 1,
            **entrenamiento,
            'sincronizado': timestamp,
            'servidor': datetime.now().isoformat()
        }

        trainings[user_code].append(training_record)

        # Log
        print(f"✓ Entrenamiento sincronizado - {user_code} ({entrenamiento.get('maquina')})")

        return jsonify({
            'success': True,
            'message': 'Entrenamiento sincronizado correctamente',
            'id': len(trainings[user_code]),
            'userCode': user_code
        })

    except Exception as e:
        print(f'Error: {str(e)}')
        return jsonify({'error': str(e)}), 500


@app.route('/api/usuario/<user_code>/entrenamientos', methods=['GET'])
def get_user_trainings(user_code):
    """Obtiene todos los entrenamientos de un usuario"""
    user_trainings = trainings.get(user_code, [])

    return jsonify({
        'userCode': user_code,
        'total': len(user_trainings),
        'entrenamientos': user_trainings
    })


@app.route('/api/usuario/<user_code>/stats', methods=['GET'])
def get_user_stats(user_code):
    """Obtiene estadísticas de un usuario"""
    user_trainings = trainings.get(user_code, [])

    if not user_trainings:
        return jsonify({'userCode': user_code, 'stats': None})

    # Calcular estadísticas
    ejercicios = list(set(t.get('maquina') for t in user_trainings))

    volumen_total = sum(
        sum(s.get('peso', 0) * s.get('reps', 0) for s in t.get('sets', []))
        for t in user_trainings
    )

    stats = {
        'totalSesiones': len(user_trainings),
        'ultimaSesion': user_trainings[-1],
        'ejerciciosUnicos': len(ejercicios),
        'ejercicios': ejercicios,
        'volumenTotal': volumen_total,
        'volumenPromedio': volumen_total / len(user_trainings) if user_trainings else 0
    }

    return jsonify({'userCode': user_code, 'stats': stats})


@app.route('/api/usuario/<user_code>/progreso', methods=['GET'])
def get_user_progress(user_code):
    """Obtiene el progreso de un ejercicio específico"""
    ejercicio = request.args.get('ejercicio')
    user_trainings = trainings.get(user_code, [])

    if not ejercicio:
        return jsonify({'error': 'Especifica un ejercicio'}), 400

    ejercicio_data = [t for t in user_trainings if t.get('maquina') == ejercicio]

    if not ejercicio_data:
        return jsonify({
            'userCode': user_code,
            'ejercicio': ejercicio,
            'data': None,
            'message': 'Sin datos para este ejercicio'
        })

    # Calcular máximo peso por sesión
    max_pesos = []
    for sesion in ejercicio_data:
        max_peso = max(s.get('peso', 0) for s in sesion.get('sets', []))
        max_pesos.append({
            'fecha': sesion.get('fecha'),
            'maxPeso': max_peso,
            'volumen': sum(s.get('peso', 0) * s.get('reps', 0) for s in sesion.get('sets', []))
        })

    return jsonify({
        'userCode': user_code,
        'ejercicio': ejercicio,
        'totalSesiones': len(ejercicio_data),
        'data': max_pesos
    })


@app.route('/health', methods=['GET'])
def health():
    """Verificar salud del servidor"""
    total_trainings = sum(len(v) for v in trainings.values())

    return jsonify({
        'status': 'ok',
        'usuarios': len(users),
        'totalEntrenos': total_trainings,
        'timestamp': datetime.now().isoformat()
    })


@app.route('/dashboard', methods=['GET'])
def dashboard():
    """Página de dashboard"""
    total_trainings = sum(len(v) for v in trainings.values())

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gym Tracker - Dashboard</title>
        <meta charset="UTF-8">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Inter', Arial, sans-serif;
                background: linear-gradient(135deg, #101522 0%, #192235 100%);
                color: #f3f6fc;
                padding: 40px 20px;
                min-height: 100vh;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
            }}
            h1 {{
                font-size: 32px;
                margin-bottom: 40px;
                text-align: center;
            }}
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 40px;
            }}
            .stat-card {{
                background: rgba(25, 34, 53, 0.8);
                backdrop-filter: blur(10px);
                padding: 30px;
                border-radius: 15px;
                border: 1px solid rgba(136, 117, 255, 0.2);
                text-align: center;
            }}
            .stat-label {{
                font-size: 14px;
                color: #9eabc1;
                margin-bottom: 10px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .stat-number {{
                font-size: 48px;
                font-weight: 900;
                color: #8875ff;
                margin-bottom: 10px;
            }}
            .stat-change {{
                font-size: 12px;
                color: #31d69a;
            }}
            .users-list {{
                background: rgba(25, 34, 53, 0.8);
                padding: 30px;
                border-radius: 15px;
                border: 1px solid rgba(136, 117, 255, 0.2);
                backdrop-filter: blur(10px);
            }}
            .users-list h2 {{
                margin-bottom: 20px;
                font-size: 18px;
            }}
            .user-item {{
                padding: 12px;
                background: rgba(16, 26, 43, 0.5);
                margin-bottom: 10px;
                border-radius: 8px;
                font-family: monospace;
                font-size: 12px;
            }}
            .refresh-info {{
                text-align: center;
                margin-top: 20px;
                color: #9eabc1;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>💪 Gym Tracker - Dashboard en Vivo</h1>

            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-label">Usuarios Activos</div>
                    <div class="stat-number" id="usuarios">{len(users)}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Total Entrenamientos</div>
                    <div class="stat-number" id="entrenos">{total_trainings}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Promedio por Usuario</div>
                    <div class="stat-number" id="promedio">{total_trainings // len(users) if len(users) > 0 else 0}</div>
                </div>
            </div>

            <div class="users-list">
                <h2>👥 Usuarios Conectados</h2>
                <div id="users-container">
                    {chr(10).join(f'<div class="user-item">👤 {user}</div>' for user in sorted(users)) if users else '<div class="empty">Sin usuarios registrados</div>'}
                </div>
            </div>

            <div class="refresh-info">
                🔄 Actualizando cada 5 segundos...
            </div>
        </div>

        <script>
            function updateDashboard() {{
                fetch('/health')
                    .then(r => r.json())
                    .then(data => {{
                        document.getElementById('usuarios').textContent = data.usuarios;
                        document.getElementById('entrenos').textContent = data.totalEntrenos;
                        document.getElementById('promedio').textContent =
                            Math.round(data.totalEntrenos / data.usuarios) || 0;
                    }});
            }}

            setInterval(updateDashboard, 5000);
        </script>
    </body>
    </html>
    '''


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint no encontrado',
        'status': 404,
        'message': 'Consulta la documentación en /docs'
    }), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'error': 'Error interno del servidor',
        'status': 500
    }), 500


if __name__ == '__main__':
    print("🚀 Gym Tracker Server - Python/Flask")
    print(f"📊 Dashboard: http://localhost:5000/dashboard")
    print(f"🔒 Auth Token configurado: {AUTH_TOKEN}")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
