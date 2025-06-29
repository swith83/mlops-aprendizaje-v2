# 📘 Lección 01: Inicio del proyecto y uso de Git en WSL2

## 🗂️ Proyecto
**Nombre del repositorio:** `mlops-aprendizaje-v2`

Este repositorio nace como una forma de documentar mi proceso de aprendizaje en temas relacionados con MLOps e Inteligencia Artificial. Aquí se irá construyendo una bitácora técnica y práctica.

---

## 🛠️ Configuración inicial

### Entorno:
- ✅ **WSL2 instalado** (Linux Ubuntu)
- ✅ **Entorno virtual activado**: `source ~/mlops-venv/bin/activate`
- ✅ **Docker activo**: `sudo service docker start`
- ✅ **Carpeta del proyecto**: `~/mlops-project`

### Comandos usados frecuentemente:
```bash
source ~/mlops-venv/bin/activate
sudo service docker start
cd ~/mlops-project


🔐 GitHub y errores con secretos
Hoy aprendí:

Cómo subir un proyecto con Git desde WSL2 a GitHub.

Cómo evitar que se suban tokens o contraseñas.

Qué hacer si un push falla por contener secretos (como un token personal).

Cómo borrar el historial sensible de Git (con rebase, reset, etc).

Que GitHub detecta automáticamente si subes contraseñas o tokens y bloquea el push por seguridad.



🧹 Limpieza del historial Git
Tuve que:

Usar git rebase -i HEAD~X para editar los últimos commits.

Editar el archivo con nano y eliminar líneas donde estaban los tokens.

Volver a hacer el commit limpio.

Forzar el push con git push --force.

Después de varios intentos, ¡todo funcionó!

✅ Resultado final
🔐 Repositorio limpio y seguro: mlops-aprendizaje-v2

📁 Bitácora guardada en Markdown (.md)

😅 Mucho aprendizaje sobre Git, errores comunes y cómo solucionarlos

💡 Reflexión
Hoy aprendí que subir cosas a GitHub no es solo copiar y pegar. Se necesita responsabilidad, organización y saber qué se está subiendo. Me siento más seguro para trabajar en futuros proyectos. ¡Esto apenas comienza!
