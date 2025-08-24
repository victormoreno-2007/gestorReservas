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


## 🗄️ Conexión a la Base de Datos

se utilizó **SQLAlchemy** para conectarse a la base de datos **MySQL**.  
La configuración de la conexión se gestiona mediante variables de entorno definidas en el archivo `.env`.

---

### ⚙️ Configuración del archivo `.env`
> Se debe crear el archivo .env si no existe  
> Se debe crearlo manualmente en la **raíz del proyecto**.

Al crear el llamado `.env` innserta el siguiente contenido:

```env
DATABASE_URL=mysql+pymysql://usuario:password@localhost:3306/gestorreservas
```

## 🏗️ Modelos y Schemas

se implementaron los modelos que representan las tablas de la base de datos:

- **Users** → Tabla `users`
- **Rooms** → Tabla `rooms`
- **Reservations** → Tabla `reservation`

Estos modelos definen la estructura de cada tabla.

## 📌 CRUD del Sistema de Reservas

Este módulo implementa las operaciones CRUD (**Crear, Leer, Actualizar y Eliminar**) para las entidades principales del sistema:

- 👤 **Usuarios**
- 🏢 **Salas**
- 📅 **Reservas**


### 📍 Endpoints

- **POST**  → Crear registro
- **GET**  → Obtener lista de registros
- **GET**  → Obtener un registro 
- **PUT**  → Actualizar registro
- **DELETE**  → Eliminar  registro
