# 🏢 Gestor de Reservas de Salas de Coworking

Proyecto con **Python + FastAPI** para gestionar usuarios, salas y reservas de un coworking.  
Incluye autenticación con JWT, validaciones de negocio y reportes básicos.  

---

## 📦 Requisitos previos

Antes de comenzar, debes tener instalado:

- [Python 3.12+](https://www.python.org/downloads/)  
- [XAMPP](https://www.apachefriends.org/es/index.html) (para la base de datos MySQL/MariaDB)  
- `pip` (gestor de paquetes de Python)  

---

## ⚙️ Instalación del entorno

### 1. Crear y activar el entorno virtual
```bash
python -m venv venv
# En Windows (PowerShell):
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
````

### 2. Instalar las dependencias necesarias
   pip install -r requirements.txt


## 🗄️  base de datos (MySQL)

 **no necesitas crear la base manualmente** antes de importarlo.

### 1) Encender MySQL
- Si usas **XAMPP**, abre el panel y enciende el módulo **MySQL**.

---

### 2) Importar la base de datos

#### Opción A: **Terminal**
1. Abre una terminal (o **XAMPP Shell** en Windows).
2. Ejecuta el import (te pedirá la contraseña si tu usuario la tiene):
   ```bash
   mysql -u root -p < docsFlowEstructura.sql
- Si tu usuario root no tiene contraseña:
   ```bash
   mysql -u root < docsFlowEstructura.sql

#### Opción B: **phpMyAdmin**
1. Abre (http://localhost/phpmyadmin/).
2. Ejecuta el import (te pedirá la contraseña si tu usuario la tiene):
   ```bash
   mysql -u root -p < docsFlowEstructura.sql
- Si tu usuario root no tiene contraseña:
  ```bash
   mysql -u root < docsFlowEstructura.sql
