// GYM TRACKER - Servidor Node.js/Express
// npm install express cors dotenv

const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(cors());

// Simular base de datos en memoria
const trainings = {};
const users = new Set();

// Middleware de autenticación
const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization?.replace('Bearer ', '');
  if (token && token === process.env.AUTH_TOKEN) {
    next();
  } else {
    res.status(401).json({ error: 'Token inválido o ausente' });
  }
};

// Endpoint para recibir entrenamientos
app.post('/api/entrenamientos', authMiddleware, (req, res) => {
  try {
    const { userCode, entrenamiento, timestamp } = req.body;

    if (!userCode || !entrenamiento) {
      return res.status(400).json({ error: 'Datos incompletos' });
    }

    // Registrar usuario
    users.add(userCode);

    // Guardar entrenamiento
    if (!trainings[userCode]) {
      trainings[userCode] = [];
    }

    trainings[userCode].push({
      id: Date.now(),
      ...entrenamiento,
      sincronizado: timestamp,
      servidor: new Date().toISOString()
    });

    // Log
    console.log(`✓ Entrenamiento sincronizado - ${userCode} (${entrenamiento.maquina})`);

    res.json({
      success: true,
      message: 'Entrenamiento sincronizado correctamente',
      id: trainings[userCode].length,
      userCode
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: error.message });
  }
});

// Endpoint para obtener historial del usuario
app.get('/api/usuario/:userCode/entrenamientos', (req, res) => {
  const { userCode } = req.params;
  const userTrainings = trainings[userCode] || [];

  res.json({
    userCode,
    total: userTrainings.length,
    entrenamientos: userTrainings
  });
});

// Endpoint para estadísticas
app.get('/api/usuario/:userCode/stats', (req, res) => {
  const { userCode } = req.params;
  const userTrainings = trainings[userCode] || [];

  if (userTrainings.length === 0) {
    return res.json({ userCode, stats: null });
  }

  const stats = {
    totalSesiones: userTrainings.length,
    ultimaSesion: userTrainings[userTrainings.length - 1],
    ejercicios: [...new Set(userTrainings.map(t => t.maquina))],
    volumenTotal: userTrainings.reduce((sum, t) => {
      return sum + t.sets.reduce((s, set) => s + (set.peso * set.reps), 0);
    }, 0)
  };

  res.json({ userCode, stats });
});

// Endpoint de salud
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    usuarios: users.size,
    totalEntrenos: Object.values(trainings).reduce((sum, arr) => sum + arr.length, 0)
  });
});

// Servir página de dashboard (opcional)
app.get('/dashboard', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>Gym Tracker - Dashboard</title>
      <style>
        body { font-family: Arial; margin: 20px; background: #101522; color: #f3f6fc; }
        .stat { display: inline-block; margin: 20px; padding: 20px; background: #192235; border-radius: 10px; }
        .stat-number { font-size: 32px; font-weight: bold; color: #8875ff; }
      </style>
    </head>
    <body>
      <h1>💪 Gym Tracker Dashboard</h1>
      <div class="stat">
        <div>Usuarios Activos</div>
        <div class="stat-number">${users.size}</div>
      </div>
      <div class="stat">
        <div>Total Entrenamientos</div>
        <div class="stat-number">${Object.values(trainings).reduce((sum, arr) => sum + arr.length, 0)}</div>
      </div>
      <script>
        setInterval(() => location.reload(), 5000);
      </script>
    </body>
    </html>
  `);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 Gym Tracker Server corriendo en puerto ${PORT}`);
  console.log(`📊 Dashboard: http://localhost:${PORT}/dashboard`);
  console.log(`🔒 Auth Token configurado: ${process.env.AUTH_TOKEN ? 'Sí' : 'No'}`);
});
