# 💪 GYM TRACKER PRO v2.0 - Guía Completa

## 🎯 Nuevas Características

### 1. **🔄 Sincronización en la Nube (Webhooks)**
Tu aplicación ahora puede enviar automáticamente tus entrenamientos a un servidor remoto.

#### Cómo funciona:
- **Accede a la pestaña "🔄 Nube"**
- Ingresa la URL de tu webhook (ej: `https://tuservidor.com/api/entrenamientos`)
- (Opcional) Agrega un token de autenticación
- Activa "Sincronizar automáticamente al guardar"
- Prueba la conexión con el botón "🧪 Probar conexión"

#### Formato de datos enviados:
```json
{
  "timestamp": "2026-11-07T10:30:45.123Z",
  "userCode": "USER_ABC123XYZ",
  "entrenamiento": {
    "fecha": "2026-11-07",
    "maquina": "Leg Press",
    "muscle": "Cuádriceps",
    "sets": [
      {"peso": 60, "reps": 10, "rir": 2},
      {"peso": 60, "reps": 10, "rir": 2}
    ]
  }
}
```

---

### 2. **📱 API Personal para tu Móvil**
Tu código único te permite agregar entrenamientos desde cualquier app.

#### Tu código de usuario:
```
USER_XXXXXXXXX  (Generado automáticamente)
```

#### Ejemplo de petición desde tu móvil:
```bash
curl -X POST "http://tu-app.com/api/train/USER_XXXXXXXXX" \
  -H "Content-Type: application/json" \
  -d '{
    "maquina": "Leg Press",
    "muscle": "Cuádriceps",
    "sets": [
      {"peso": 60, "reps": 10, "rir": 2}
    ]
  }'
```

---

### 3. **⚙️ Integraciones con Wearables**
Conecta tu aplicación con:
- ✓ **Google Fit** - Sincroniza datos de ejercicio automáticamente
- ✓ **Apple HealthKit** - Comparte datos con la app Salud de Apple

#### Cómo activar:
1. Ve a "🔄 Nube"
2. Marca las integraciones que deseas
3. Autoriza el acceso la primera vez
4. Los datos se sincronizarán automáticamente

---

### 4. **🤖 IA Inteligente & Recomendaciones Personalizadas**
Tu entrenador personal basado en IA que se adapta a tu estilo.

#### Niveles de análisis:
- **Básico**: Recomendaciones simples de peso
- **Avanzado**: Análisis de tendencias y volumen (RECOMENDADO)
- **Experto**: Calcula 1RM y predice cargas óptimas

#### Estilos de entrenamiento:
- **HIIT** (Alta intensidad) - Máximo peso, mínimas repeticiones
- **Moderada** - Equilibrio entre fuerza y volumen (RECOMENDADO)
- **Bajo volumen** - Mantén peso, suma series

#### Cómo funciona:
La IA analiza automáticamente:
- Tu tendencia de volumen (últimas 5 sesiones)
- Distribución de repeticiones
- Esfuerzo percibido (RIR)
- Tu preferencia de intensidad

**Resultado**: Recomendaciones personalizadas cada vez que registres un ejercicio

---

### 5. **📱 Optimizado para Móvil (PWA)**
Ahora funciona perfectamente en tu teléfono:
- ✓ Diseño responsive para pantallas pequeñas
- ✓ Botones más grandes y fáciles de tocar
- ✓ Funciona sin internet (Service Worker)
- ✓ Instálalo como app en tu móvil
- ✓ Acceso rápido desde la pantalla principal

#### Para instalar como app:
**Android:**
1. Abre en Chrome
2. Toca ⋮ → "Instalar app"
3. Elige un nombre

**iPhone:**
1. Abre en Safari
2. Toca compartir → "Añadir a Inicio"
3. Elige un nombre

---

## 🚀 Casos de Uso

### Caso 1: Sincronizar con tu servidor personal
```
1. Crea un servidor Node.js/Python que reciba:
   POST /api/entrenamientos
   Authorization: Bearer tu-token-secreto
   
2. Configura el webhook en tu app:
   URL: https://tuservidor.com/api/entrenamientos
   Token: tu-token-secreto
   
3. ¡Listo! Tus entrenamientos se envían automáticamente
```

### Caso 2: Integración con Google Sheets
```
1. Usa Google Apps Script para recibir webhooks
2. Los datos se guardan automáticamente en una hoja
3. Crea gráficos y análisis en Google Sheets
```

### Caso 3: Dashboard en vivo
```
1. Sincroniza con una base de datos en la nube
2. Crea un dashboard en tiempo real
3. Monitorea tu progreso desde cualquier dispositivo
```

---

## 🔧 Configuración Avanzada

### Webhook con autenticación
```bash
curl -X POST "https://tuservidor.com/api/entrenamientos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -d '{...}'
```

### Respuesta esperada del servidor
Tu servidor debe devolver:
```json
{
  "success": true,
  "message": "Entrenamiento sincronizado",
  "id": "123456"
}
```

---

## 📊 Análisis y Reportes

### Datos que puedes exportar:
- **JSON**: Para respaldo completo y sincronización
- **CSV**: Para análisis en Excel/Sheets

### Cálculos automáticos:
- **1RM estimado**: Usando la fórmula de Brzycki
- **Volumen**: Peso × Repeticiones × Series
- **Tendencia**: Cambio porcentual en volumen
- **Récords personales**: Máximo peso por ejercicio

---

## 📝 Preguntas Frecuentes

**P: ¿Mis datos se guardan localmente?**
R: Sí, tu navegador guarda todo. También se sincroniza a tu servidor si lo configuras.

**P: ¿Funciona sin internet?**
R: Sí, gracias al Service Worker. Una vez cargada, funciona offline.

**P: ¿Puedo acceder a mis datos desde otro dispositivo?**
R: Sí, configura un webhook para sincronizar a un servidor central.

**P: ¿Cómo hago respaldos?**
R: Ve a "⚙️ Herramientas" y exporta como JSON o CSV.

**P: ¿La IA me dirá cuánto peso levantar?**
R: La IA da recomendaciones basadas en ciencia, pero tú decides. Respeta siempre tu técnica.

---

## 🛠️ Desarrollo de tu servidor de sincronización

### Ejemplo Node.js/Express:
```javascript
app.post('/api/entrenamientos', (req, res) => {
  const { userCode, entrenamiento, timestamp } = req.body;
  
  // Guardar en BD
  await db.entrenamientos.insert({
    userId: userCode,
    fecha: entrenamiento.fecha,
    maquina: entrenamiento.maquina,
    sets: entrenamiento.sets,
    sincronizado: timestamp
  });
  
  res.json({ success: true, message: 'Sincronizado' });
});
```

### Ejemplo Python/Flask:
```python
@app.route('/api/entrenamientos', methods=['POST'])
def sync_training():
    data = request.get_json()
    user_code = data['userCode']
    training = data['entrenamiento']
    
    # Guardar en BD
    db.trainings.insert_one({
        'user': user_code,
        'date': training['fecha'],
        'exercise': training['maquina'],
        'sets': training['sets']
    })
    
    return {'success': True}
```

---

## 🎓 Tips para máximo progreso

1. **Registra el RIR** (Reps in Reserve): Ayuda a la IA a saber tu esfuerzo real
2. **Usa el temporizador**: Mantén consistencia en tiempos de descanso
3. **Revisa tendencias**: Ve a "📈 Progreso" para ver tu evolución
4. **Personaliza IA**: Elige tu nivel preferido en "🔄 Nube"
5. **Sincroniza regularmente**: Así tienes respaldo en la nube

---

**Versión**: 2.0  
**Última actualización**: 2026-11-07  
**Autor**: Tu Entrenador Personal IA 💪
