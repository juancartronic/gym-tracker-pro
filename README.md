# 💪 Gym Tracker PRO v2.0

**Tu entrenador personal inteligente en la nube**

Una aplicación web completa para registrar entrenamientos, recibir recomendaciones personalizadas basadas en IA y sincronizar datos automáticamente.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Node.js](https://img.shields.io/badge/Node.js-14%2B-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

---

## 🎯 Características Principales

### 📱 Aplicación Web
- ✅ Funciona en cualquier navegador (Chrome, Firefox, Safari, Edge)
- ✅ Diseño responsive para móvil y escritorio
- ✅ Funciona sin internet (PWA con Service Worker)
- ✅ Datos guardados localmente en el navegador

### 🤖 IA Inteligente
- ✅ Recomendaciones personalizadas por sesión
- ✅ Cálculo automático de 1RM
- ✅ Análisis de tendencias
- ✅ 3 niveles de análisis: Básico, Avanzado, Experto

### 🔄 Sincronización en la Nube
- ✅ Webhooks para enviar datos automáticamente
- ✅ API personal para tu código de usuario
- ✅ Soporte para Google Fit y Apple HealthKit
- ✅ Respaldo seguro de entrenamientos

### 📊 Análisis y Reportes
- ✅ Gráficas de progreso en tiempo real
- ✅ Distribución de grupos musculares
- ✅ Récords personales automáticos
- ✅ Exportar datos a JSON/CSV

---

## 🚀 Inicio Rápido

### Opción 1: Sin servidor (Local)
```bash
# Solo necesitas un navegador
# Abre index.html en tu navegador
# ¡Listo! Funciona completamente offline
```

### Opción 2: Con sincronización (Node.js)
```bash
# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env
# Edita .env y cambia AUTH_TOKEN

# Iniciar servidor
npm start

# Servidor disponible en http://localhost:3000
```

### Opción 3: Con sincronización (Python)
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env y cambia AUTH_TOKEN

# Iniciar servidor
python server-flask.py

# Servidor disponible en http://localhost:5000
```

---

## 📁 Estructura del Proyecto

```
gym-tracker-pro/
├── index.html          # Aplicación principal
├── server-express.js              # Servidor Node.js
├── server-flask.py                # Servidor Python
├── package.json                   # Dependencias Node.js
├── requirements.txt               # Dependencias Python
├── .env.example                   # Variables de entorno (ejemplo)
├── .gitignore                     # Archivos a ignorar en Git
├── README.md                      # Este archivo
├── README_INSTALACION.md          # Guía de instalación detallada
├── GYM_TRACKER_PRO_v2_GUIA.md    # Guía de características
└── .git/                          # Repositorio Git
```

---

## 💡 Casos de Uso

### 1. Registrar entrenamientos
- Ingresa ejercicio, peso, repeticiones y series
- La app calcula automáticamente volumen y recomendaciones
- Obtén feedback inteligente del IA

### 2. Sincronizar con servidores
- Configura webhook para enviar datos automáticamente
- Respalda tus entrenamientos en la nube
- Accede desde múltiples dispositivos

### 3. Integración con wearables
- Conecta con Google Fit o Apple HealthKit
- Los datos se sincronmizan automáticamente
- Análisis completo de tu actividad

### 4. Dashboard en tiempo real
- Visualiza estadísticas de tus usuarios
- Monitorea progreso en vivo
- Exporta reportes

---

## 🔧 Configuración

### Variables de Entorno
```env
# Token de autenticación (CAMBIAR en producción)
AUTH_TOKEN=token-muy-secreto-123

# Puerto (Node.js)
NODE_PORT=3000

# Puerto (Python)
FLASK_PORT=5000

# Entorno
FLASK_ENV=development
```

### Webhook Configuration
En la aplicación, ve a "🔄 Nube" e ingresa:
- **URL**: `http://localhost:3000/api/entrenamientos` (Node) o `http://localhost:5000/api/entrenamientos` (Python)
- **Token**: El valor de `AUTH_TOKEN` de tu `.env`

---

## 📊 Endpoints de la API

### POST `/api/entrenamientos`
Sincroniza un entrenamiento
```bash
curl -X POST "http://localhost:3000/api/entrenamientos" \
  -H "Authorization: Bearer token-secreto" \
  -H "Content-Type: application/json" \
  -d '{
    "userCode": "USER_ABC123",
    "entrenamiento": {
      "fecha": "2026-11-08",
      "maquina": "Leg Press",
      "sets": [{"peso": 60, "reps": 10}]
    }
  }'
```

### GET `/api/usuario/{userCode}/stats`
Obtiene estadísticas del usuario
```bash
curl -H "Authorization: Bearer token-secreto" \
  "http://localhost:3000/api/usuario/USER_ABC123/stats"
```

### GET `/health`
Verifica salud del servidor
```bash
curl "http://localhost:3000/health"
```

Ver más endpoints en `README_INSTALACION.md`

---

## 🌐 Desplegar en la Nube

### Heroku (Node.js)
```bash
heroku login
heroku create gym-tracker-app
heroku config:set AUTH_TOKEN=token-secreto
git push heroku main
```

### Render (Express)
1. Conecta tu repo de GitHub
2. Render detectará automáticamente que es Node.js
3. Configura variables de entorno
4. ¡Deploy automático!

### Railway (Python)
1. Conecta tu repo de GitHub
2. Railway detectará Python automáticamente
3. Configura variables de entorno
4. ¡Deploy automático!

### Google Cloud
```bash
gcloud app deploy
```

---

## 📱 Instalar como App

### Android (Chrome)
1. Abre `index.html` en Chrome
2. Toca ⋮ (menú) → "Instalar app"
3. Elige un nombre
4. ¡Listo!

### iPhone (Safari)
1. Abre `index.html` en Safari
2. Toca Compartir → "Añadir a Inicio"
3. Elige un nombre
4. ¡Listo!

---

## 🧪 Pruebas

### Probar sincronización
```bash
# Ir a la pestaña "🔄 Nube"
# Ingresar URL del webhook
# Hacer clic en "🧪 Probar conexión"
```

### Ver dashboard
```bash
# Node.js: http://localhost:3000/dashboard
# Python: http://localhost:5000/dashboard
```

### Verificar logs
```bash
# Terminal donde ejecutas el servidor
# Verás todos los entrenamientos sincronizados
```

---

## 🔒 Seguridad

- ✅ Token-based authentication
- ✅ CORS configurado
- ✅ Datos guardados localmente (no en la nube sin consentimiento)
- ✅ HTTPS recomendado para producción
- ✅ Variables de entorno para secrets

### En Producción
1. Cambiar `AUTH_TOKEN` a algo seguro
2. Usar HTTPS
3. Implementar base de datos
4. Configurar Rate Limiting
5. Auditar logs regularmente

---

## 📚 Documentación Completa

- `GYM_TRACKER_PRO_v2_GUIA.md` - Guía de características
- `README_INSTALACION.md` - Instalación y troubleshooting
- Comentarios en el código (server-express.js, server-flask.py)

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📋 Roadmap

- [ ] Dashboard de administrador
- [ ] Integración con más wearables
- [ ] Base de datos SQL/NoSQL
- [ ] Autenticación con OAuth
- [ ] Notificaciones push
- [ ] Comunidad de usuarios
- [ ] Planes de entrenamiento personalizados

---

## 📄 Licencia

MIT License - Ver `LICENSE` para detalles

---

## 💬 FAQ

**P: ¿Los datos se guardan en la nube automáticamente?**
A: No, se guardan localmente en tu navegador. Solo se envían a un servidor si configuras un webhook.

**P: ¿Funciona sin internet?**
A: Sí, gracias al Service Worker. Se sincroniza cuando vuelves a conectar.

**P: ¿Puedo usar solo la app sin servidor?**
A: Sí, abre `index.html` en tu navegador. Todo funciona localmente.

**P: ¿Cómo cambio el token de autenticación?**
A: Edita `.env` y cambia `AUTH_TOKEN=` a tu valor deseado.

**P: ¿Qué pasa si pierdo mis datos?**
A: Si no configuraste sincronización, los datos se guardan en el caché del navegador. Haz respaldos exportando JSON.

---

## 📞 Soporte

- 📖 Lee la documentación
- 🐛 Reporta bugs en Issues
- 💡 Sugiere features en Discussions
- 📧 Email: gym-tracker@example.com

---

**Versión**: 2.0.0  
**Última actualización**: 2026-11-08  
**Autor**: Gym Tracker Team 💪

---

Hecho con ❤️ para atletas que se toman en serio su progreso.
