..Mi Proyecto MLOps en WSL

## 🛠️ Configuración Inicial

### Instalación de WSL y Ubuntu
```bash

wsl --install -d Ubuntu
sudo apt update && sudo apt upgrade -y


###Configuración de Python

sudo apt install python3 python3-pip python3-venv -y
python3 -m venv ~/mlops-venv
source ~/mlops-venv/bin/activate


###Instalación de Docker en WSL

sudo apt install docker.io -y
sudo usermod -aG docker \$USER
newgrp docker
sudo service docker start

###Dependencias Instaladas

pip install mlflow scikit-learn wandb pandas numpy docker

###Proyectos Realizados

##'Hola Mundo' con MLflow

#Script: script/train.py

import mlflow
from sklearn.linear_model import LinearRegression
X = [[1], [2], [3]]
y = [2, 4, 6]
with mlflow.start_run():
    model = LinearRegression().fit(X, y)
    mlflow.sklearn.log_model(model, "model")

#Ejecucion:


python3 scripts/train.py
mlflow ui --host 0.0.0.0 --gunicorn-opts "--timeout 120"


###2.Solucion a Errores

##'WORKER TIMEOUT' En MLflow

mlflow ui --host 0.0.0.0 --gunicorn-opts "--timeout 120"


###Estructura del Proyecto


mlops-project/
├── data/
├── scripts/
│   ├── train.py
│   └── train_with_wandb.py
├── mlruns/
└── README.md


###COMANDOS PARA INICIAR EL ENTORNO

# Cada vez que reinicies:
source ~/mlops-venv/bin/activate
sudo service docker start
cd ~/mlops-project





