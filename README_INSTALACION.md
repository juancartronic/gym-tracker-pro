# 🚀 GYM TRACKER PRO v2.0 - Guía de Instalación y Uso

## 📋 Contenidos

- `index.html` - Aplicación principal (funciona en navegador)
- `server-express.js` - Servidor Node.js/Express para sincronización
- `server-flask.py` - Servidor Python/Flask para sincronización
- `GYM_TRACKER_PRO_v2_GUIA.md` - Guía completa de características

---

## 🎯 Opción 1: Usar sin servidor (Local)

### Requisitos
- Navegador moderno (Chrome, Firefox, Safari, Edge)

### Instalación
1. Descarga `index.html`
2. Abre el archivo en tu navegador
3. ¡Listo! Funciona completamente offline

### Ventajas
- ✓ Funciona sin internet
- ✓ Datos guardados localmente (seguro)
- ✓ Sin instalación

### Desventajas
- ✗ No sincroniza entre dispositivos
- ✗ Datos perdidos si limpias el caché

---

## 🚀 Opción 2: Sincronización con Servidor (Node.js)

### Requisitos
- Node.js 14+ ([descargar](https://nodejs.org))
- npm o yarn

### Instalación

#### 1. Preparar carpeta
```bash
mkdir gym-tracker-server
cd gym-tracker-server
```

#### 2. Inicializar Node
```bash
npm init -y
npm install express cors dotenv
```

#### 3. Crear archivo `.env`
```bash
AUTH_TOKEN=token-muy-secreto-123
PORT=3000
```

#### 4. Copiar `server-express.js`
```bash
# Copiar el archivo server-express.js a esta carpeta
cp ../server-express.js ./
```

#### 5. Iniciar servidor
```bash
node server-express.js
```

Deberías ver:
```
🚀 Gym Tracker Server corriendo en puerto 3000
📊 Dashboard: http://localhost:3000/dashboard
```

### Configurar en la app (Gym Tracker)

1. Abre `index.html`
2. Ve a la pestaña "🔄 Nube"
3. Ingresa:
   - **URL del webhook**: `http://localhost:3000/api/entrenamientos`
   - **Token**: `token-muy-secreto-123`
4. Haz clic en "✓ Configurar webhook"
5. Prueba con "🧪 Probar conexión"

---

## 🐍 Opción 3: Sincronización con Servidor (Python/Flask)

### Requisitos
- Python 3.8+ ([descargar](https://www.python.org))
- pip

### Instalación

#### 1. Preparar carpeta
```bash
mkdir gym-tracker-server
cd gym-tracker-server
```

#### 2. Crear entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar dependencias
```bash
pip install flask flask-cors python-dotenv
```

#### 4. Crear archivo `.env`
```bash
AUTH_TOKEN=token-muy-secreto-123
FLASK_ENV=development
```

#### 5. Copiar `server-flask.py`
```bash
# Copiar el archivo server-flask.py a esta carpeta
```

#### 6. Iniciar servidor
```bash
python server-flask.py
```

Deberías ver:
```
🚀 Gym Tracker Server - Python/Flask
📊 Dashboard: http://localhost:5000/dashboard
```

### Configurar en la app (Gym Tracker)

1. Abre `index.html`
2. Ve a la pestaña "🔄 Nube"
3. Ingresa:
   - **URL del webhook**: `http://localhost:5000/api/entrenamientos`
   - **Token**: `token-muy-secreto-123`
4. Haz clic en "✓ Configurar webhook"
5. Prueba con "🧪 Probar conexión"

---

## ☁️ Desplegar en la Nube

### Opción A: Heroku (Express)

```bash
# Instalar Heroku CLI
# Crear cuenta en heroku.com

# Iniciar sesión
heroku login

# Crear app
heroku create mi-gym-tracker

# Configurar variables de entorno
heroku config:set AUTH_TOKEN=token-muy-secreto-123 -a mi-gym-tracker

# Desplegar
git push heroku main

# Ver logs
heroku logs --tail
```

Tu servidor estará en: `https://mi-gym-tracker.herokuapp.com/api/entrenamientos`

### Opción B: Render (Express)

1. Sube tu código a GitHub
2. Ve a [render.com](https://render.com)
3. Crea nuevo "Web Service"
4. Conecta tu repo
5. Configura:
   - Build: `npm install`
   - Start: `node server-express.js`
   - Environment Variables: `AUTH_TOKEN=...`

### Opción C: Railway (Python)

1. Ve a [railway.app](https://railway.app)
2. Crea nuevo proyecto
3. Conecta tu repo
4. Railway detectará Python automáticamente
5. Configura variables de entorno

### Opción D: Google Cloud (Ambos)

```bash
# Instalar Google Cloud SDK
gcloud auth login

# Desplegar Node.js
gcloud app deploy

# Desplegar Python
gcloud app deploy
```

---

## 🧪 Pruebas

### Probar sincronización desde terminal

#### Con Node.js
```bash
curl -X POST "http://localhost:3000/api/entrenamientos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token-muy-secreto-123" \
  -d '{
    "userCode": "USER_TEST123",
    "timestamp": "2026-11-07T10:00:00Z",
    "entrenamiento": {
      "fecha": "2026-11-07",
      "maquina": "Leg Press",
      "muscle": "Cuádriceps",
      "sets": [
        {"peso": 60, "reps": 10, "rir": 2},
        {"peso": 60, "reps": 10, "rir": 2}
      ]
    }
  }'
```

#### Con Python
```bash
curl -X POST "http://localhost:5000/api/entrenamientos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token-muy-secreto-123" \
  -d '{
    "userCode": "USER_TEST123",
    "timestamp": "2026-11-07T10:00:00Z",
    "entrenamiento": {
      "fecha": "2026-11-07",
      "maquina": "Leg Press",
      "muscle": "Cuádriceps",
      "sets": [
        {"peso": 60, "reps": 10, "rir": 2}
      ]
    }
  }'
```

### Ver dashboard
```bash
# Node.js
http://localhost:3000/dashboard

# Python
http://localhost:5000/dashboard
```

---

## 📊 Endpoints del Servidor

### Node.js y Python (Idénticos)

#### POST `/api/entrenamientos`
Sincroniza un entrenamiento
```json
{
  "userCode": "USER_ABC123",
  "timestamp": "2026-11-07T10:00:00Z",
  "entrenamiento": {
    "fecha": "2026-11-07",
    "maquina": "Leg Press",
    "muscle": "Cuádriceps",
    "sets": [{"peso": 60, "reps": 10, "rir": 2}]
  }
}
```

#### GET `/api/usuario/{userCode}/entrenamientos`
Obtiene todos los entrenamientos de un usuario
```bash
curl "http://localhost:3000/api/usuario/USER_ABC123/entrenamientos"
```

#### GET `/api/usuario/{userCode}/stats`
Obtiene estadísticas del usuario
```bash
curl "http://localhost:3000/api/usuario/USER_ABC123/stats"
```

#### GET `/api/usuario/{userCode}/progreso?ejercicio=Leg%20Press`
Obtiene progreso de un ejercicio específico
```bash
curl "http://localhost:3000/api/usuario/USER_ABC123/progreso?ejercicio=Leg%20Press"
```

#### GET `/health`
Verifica salud del servidor
```bash
curl "http://localhost:3000/health"
```

---

## 🔧 Troubleshooting

### "Connection refused"
- ¿El servidor está corriendo?
- ¿Es el puerto correcto? (3000 para Node, 5000 para Python)
- ¿Firewall permite la conexión?

### "Token inválido"
- Verifica que el token en `.env` coincida con el de la app
- Token debe incluir "Bearer " en el header

### Datos no se sincronizan
1. Verifica la URL del webhook
2. Haz clic en "🧪 Probar conexión"
3. Revisa la consola del navegador (F12)
4. Revisa logs del servidor

### CORS error
- Los servidores ya incluyen `cors` habilitado
- Si usas dominio personalizado, actualiza ALLOWED_ORIGINS

---

## 🛡️ Seguridad en Producción

### Cambiar token
```bash
AUTH_TOKEN=tu-token-super-secreto-y-largo-123-456
```

### Usar HTTPS
```bash
# Obtener certificado gratuito con Let's Encrypt
certbot certonly --standalone -d tu-dominio.com
```

### Variables de entorno
```bash
# NUNCA commits secrets a Git
echo ".env" >> .gitignore

# Usar en servidor:
export AUTH_TOKEN="token-secreto"
export DATABASE_URL="postgresql://..."
```

### Base de datos
Para producción, reemplaza el almacenamiento en memoria:

#### MongoDB
```javascript
// server-express.js
const mongoose = require('mongoose');
mongoose.connect(process.env.MONGODB_URL);

const trainingSchema = new mongoose.Schema({
  userCode: String,
  entrenamiento: Object,
  timestamp: Date
});
```

#### PostgreSQL
```python
# server-flask.py
import psycopg2
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
```

---

## 📱 Usar en Móvil

### URL local (dentro de la red)
Si tu PC tiene IP `192.168.1.100`:
```
http://192.168.1.100:3000/api/entrenamientos
```

### URL pública (desde cualquier lugar)
Usa ngrok para exponer tu servidor local:
```bash
ngrok http 3000
# Obtendrás URL como: https://abc123.ngrok.io/api/entrenamientos
```

O despliega en la nube (Heroku, Render, Railway, etc.)

---

## 📞 Soporte

- Documentación: Ver `GYM_TRACKER_PRO_v2_GUIA.md`
- Código: Todos los archivos están comentados
- GitHub Issues: Reporte problemas

---

**Versión**: 2.0  
**Última actualización**: 2026-11-07  
**Autor**: Tu Entrenador Personal IA 💪
