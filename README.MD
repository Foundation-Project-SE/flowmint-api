# Foundation Project - Backend API

Bienvenido al repositorio oficial del Backend para el proyecto Foundation. Este servicio expone una API RESTful construida con Django y Django REST Framework (DRF), diseñada para ser escalable y modular.

## Tech Stack

* **Lenguaje:** Python 3.10 o superior
* **Framework Web:** Django 5.x 
* **API Toolkit:** Django REST Framework 
* **Seguridad y Configuración:** Python-Decouple y CORS Headers

## Prerrequisitos

Asegúrate de tener instalado en tu máquina: 
* [Python 3.10](https://www.python.org/downloads/) o superior.
* [Git](https://git-scm.com/).

## Instalación y Configuración (Local)

Sigue estos pasos para levantar el entorno de desarrollo:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Foundation-Project-SE/backend.git](https://github.com/Foundation-Project-SE/backend.git)
cd backend
```

### 2.Creación de entorno virtual

## En Windows: 

```bash
python -m venv venv
.\venv\Scripts\activate
```

## En macOS o Linux: 
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalación de dependencias

```bash
pip install -r requirements.txt
```

### 4. Migraciones de Base de Datos

```bash
python manage.py migrate
```

### ▶️ Ejecución

# Para iniciar el servidor:

```bash
python manage.py runserver
```

# Endpoints Disponibles:

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| **GET** | `/health/` | Healthcheck del sistema. Verifica servicio y conexión a BD. |
| **GET** | `/admin/` | Panel de Administración de Django. |