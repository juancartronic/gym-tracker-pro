# 📤 Cómo Subir tu Proyecto a GitHub

Tu repositorio local está listo. Ahora sigue estos pasos para subirlo a GitHub:

## Paso 1: Crear Repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Inicia sesión con tu cuenta (o crea una si no tienes)
3. Haz clic en el **+** (arriba a la derecha) → **New repository**
4. Rellena:
   - **Repository name**: `gym-tracker-pro`
   - **Description**: `Entrenador personal inteligente con sincronización en la nube`
   - **Public** o **Private** (a tu elección)
   - NO marques "Initialize this repository..."
5. Haz clic en **Create repository**

## Paso 2: Conectar tu Repositorio Local

Después de crear el repo, GitHub te mostrará comandos. Copia exactamente esto en tu terminal:

```bash
# Ir a tu carpeta del proyecto
cd c:/Users/Juanka/Desktop/gym-tracker-pro

# Agregar URL remota de GitHub
# Reemplaza TU_USUARIO por tu usuario de GitHub
git remote add origin https://github.com/TU_USUARIO/gym-tracker-pro.git

# (Alternativa con SSH si ya configuraste):
# git remote add origin git@github.com:TU_USUARIO/gym-tracker-pro.git

# Cambiar rama principal a 'main' (opcional, pero recomendado)
git branch -M main

# Subir el código
git push -u origin main
```

## Paso 3: Autenticación

### Opción A: Personal Access Token (Recomendado)

1. Ve a GitHub Settings → **Developer settings** → **Personal access tokens**
2. Haz clic en **Generate new token**
3. Dale nombre: `gym-tracker-cli`
4. Marca: `repo` (full control of private repositories)
5. Haz clic en **Generate token**
6. **COPIA el token** (aparece solo una vez)
7. En la terminal, Git pedirá contraseña. **Pega el token**

### Opción B: SSH (Más seguro)

Si ya tienes SSH configurado:
```bash
# Verificar si tienes SSH
ls ~/.ssh/

# Si no tienes, generar:
ssh-keygen -t ed25519 -C "tu-email@example.com"

# Copiar la clave pública a GitHub
# Settings → SSH and GPG keys → New SSH key
cat ~/.ssh/id_ed25519.pub  # Copiar esto
```

## Paso 4: Verificar que está en GitHub

```bash
# Ver URL remota
git remote -v

# Debería mostrar:
# origin  https://github.com/TU_USUARIO/gym-tracker-pro.git (fetch)
# origin  https://github.com/TU_USUARIO/gym-tracker-pro.git (push)
```

## Paso 5: Hacer Cambios Futuros

```bash
# Hacer cambios locales
# Editar archivos...

# Ver qué cambió
git status

# Agregar cambios
git add .

# Crear commit
git commit -m "Descripción del cambio"

# Subir a GitHub
git push origin main
```

---

## 📋 Estructura de Carpetas en GitHub

Tu repositorio lucirá así:

```
gym-tracker-pro/
├── README.md                      ← GitHub lo muestra automáticamente
├── LICENSE
├── .gitignore
├── .env.example
├── index.html           ← Tu app principal
├── server-express.js              ← Servidor Node.js
├── server-flask.py                ← Servidor Python
├── package.json
├── requirements.txt
├── GYM_TRACKER_PRO_v2_GUIA.md
└── README_INSTALACION.md
```

---

## 🔗 URL de tu Repositorio

Una vez subido, tu repositorio estará en:

```
https://github.com/TU_USUARIO/gym-tracker-pro
```

Ejemplo:
```
https://github.com/juanka/gym-tracker-pro
```

---

## 💡 Tips Útiles

### Ver commits en GitHub
```bash
git log --oneline
```

### Cambiar descripción del proyecto
En GitHub:
1. Ve a Settings (engranaje)
2. Edita "About"
3. Agrega descripción, website, topics

### Colaborar con otros
1. Ve a Settings → Collaborators
2. Agrega usuarios (necesitan cuenta GitHub)
3. Ellos pueden hacer `git push` directamente

### Crear branches para features
```bash
# Crear rama para un feature nuevo
git checkout -b feature/nueva-caracteristica

# Hacer cambios...
git add .
git commit -m "Add nueva caracteristica"

# Subir la rama
git push origin feature/nueva-caracteristica

# En GitHub, abrir Pull Request
# Review → Merge a main
```

---

## 🔐 Seguridad

### IMPORTANTE: Nunca commitees secrets
```bash
# Asegúrate de que .gitignore incluye:
.env          # ← Este archivo NUNCA debe estar en GitHub

# Si accidentalmente subiste .env:
git rm --cached .env
git commit -m "Remove .env"
git push
```

### Cambiar token si lo subiste por error
1. Ve a GitHub → Settings → Developer settings → Personal access tokens
2. Haz clic en "Delete"
3. Genera uno nuevo

---

## 📱 Compartir tu Proyecto

Una vez en GitHub, puedes compartir el link:

```
👍 GitHub: https://github.com/TU_USUARIO/gym-tracker-pro
📥 Clonar: git clone https://github.com/TU_USUARIO/gym-tracker-pro.git
⭐ No olvides dar una estrella si te gusta!
```

---

## ❓ Troubleshooting

### "fatal: 'origin' does not appear to be a 'git' repository"
```bash
# Asegúrate que estás en la carpeta correcta
cd c:/Users/Juanka/Desktop/gym-tracker-pro

# Verifica que existe .git
ls -la .git
```

### "Permission denied"
```bash
# Si usas SSH, verifica:
ssh -T git@github.com

# Si usas HTTPS, recrea el token
```

### "Cannot push to GitHub"
```bash
# Actualizar referencia remota
git remote -v

# Si está mal, corregir:
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/gym-tracker-pro.git
```

---

## 🎉 ¡Listo!

Tu proyecto está en GitHub y listo para:
- ✅ Compartir con otros
- ✅ Colaborar en equipo
- ✅ Desplegar automáticamente
- ✅ Mantener historial de cambios
- ✅ Recibir contribuciones

---

**¿Necesitas ayuda?** → Consulta [GitHub Docs](https://docs.github.com)
