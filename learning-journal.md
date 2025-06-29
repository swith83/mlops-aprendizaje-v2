
# 📘 Bitácora de Aprendizaje: Proyecto MLOps Personal

---

## 🧠 Propósito de este documento

Este archivo es mi guía personal para recordar:
- Cómo configuré todo el entorno de desarrollo (WSL2, Docker, entorno virtual).
- Cómo subir y mantener mi proyecto en GitHub.
- Qué comandos uso a diario.
- Qué aprendí cada día.
- Soluciones a problemas que me ocurrieron.
- Tokens, contraseñas y configuraciones importantes (opcionales, cifradas).

---

## 🔐 Accesos importantes

**GitHub Token Personal (PAT):**  
💬 *[E:\APRENDIZAJE AUTONOMO IA MLOps]*  
🛑 *No lo publiques nunca si haces este archivo público.*

---

## 🖥️ Instalación y configuración del entorno

### 1. Instalación de WSL2

- Ejecuté en PowerShell (modo administrador):
  ```bash
  wsl --install -d Ubunt


Reinicié el equipo y abrí Ubuntu.

2. Creación del entorno virtual
Entré a mi carpeta de proyecto:

cd ~
mkdir mlops-project
cd mlops-project
python3 -m venv ~/mlops-venv
source ~/mlops-venv/bin/activate


3. Instalación de Docker en Ubuntu WSL2
Instalé Docker con los siguientes comandos:

sudo apt update
sudo apt install docker.io
sudo service docker start

Para que Docker se inicie: sudo service docker start



🧩 Comandos que ejecuto al iniciar mi entorno
Cada vez que prendo el PC y quiero trabajar en mi proyecto, ejecuto:


source ~/mlops-venv/bin/activate
sudo service docker start
cd ~/mlops-project



🗂️ Proyecto Git y GitHub
Inicializar proyecto con Git:

git init
git add .
git commit -m "Primer commit: agrego archivos iniciales del proyecto MLOps"


Conectar a GitHub:

git remote add origin https://github.com/swith83/mlops-aprendizaje.git
git branch -M main
git push -u origin main


Si GitHub pide usuario y contraseña:
Usuario: swith83

Contraseña: (E:\APRENDIZAJE AUTONOMO IA MLOps)


🐙 Problemas comunes que resolví
❌ git push falla con contraseña → Solución: usar Personal Access Token (PAT)

❌ Repository not found → Solución: revisar que la URL tenga bien mi usuario: swith83

✅ Guardar acceso con:git config --global credential.helper store



📅 Día 1 – Primer avance
Instalé Ubuntu con WSL2 y Docker.

Creé entorno virtual y carpeta del proyecto.

Inicialicé repositorio local con Git.

Subí el proyecto completo a GitHub.

Aprendí a usar el token en lugar de la contraseña.

Empecé esta bitácora para no olvidar el proceso.



🔜 Próximos pasos
Organizar carpetas del proyecto (scripts/, Docker/, etc.)

Crear estructura base del README.md

Empezar con Docker para modelos IA simples

## ✅ ¿Cómo guardarlo?

En tu terminal:

```bash
nano learning-journal.md


Pega todo lo de arriba, y guarda con:

Ctrl + O, Enter

Ctrl + X

Luego súbelo a GitHub:

git add learning-journal.md
git commit -m "Agrego bitácora de aprendizaje con pasos y comandos"
git push

































