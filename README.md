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
> Se debe crear el archivo `.env` si no existe  
> Debe crearse manualmente en la **raíz del proyecto**.

Al crear el archivo `.env` inserta el siguiente contenido de ejemplo:

```env
# Conexión a la base de datos
DATABASE_URL=mysql+pymysql://usuario:password@localhost:3306/gestorreservas

# Variables para autenticación JWT
SECRET_KEY=pon_tu_clave_aqui
ALGORITHM=HS256
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

# 📌 Implementación de Rutas - Gestor de Reservas

se implementaron las rutas para el manejo de los **users**, **rooms** y **reservations**, las cuales estan presentes en la documentacion automatica de FastApi

## 🚀 Rutas de Usuarios

**GET** `/users/ List Users`
- Devuelve la lista de usuarios registrados.  
  
**POST** `/users/ Create`
- Crea nuevos usuarios

**GET** `/users/ Get User`
- Devuelve el usuario con el id digitado en el parametro

**PUT** `/users/ Update`
- Modifica el registro del usuario con el id digitado en el parametro

**DELETE** `/users/ Delete`
- Elimina el usuario con el id digitado en el parametro


## 🚀 Rutas de habitaciones

**GET** `/Rooms/ List Rooms`
- Devuelve la lista de las habitaciones registradas.  
  
**POST** `/Rooms/ Create`
- Crea nuevas habitaciones

**GET** `/Rooms/ Get Rooms`
- Devuelve la habitacion con el id digitado en el parametro

**PUT** `/Rooms/ Update`
- Modifica el registro de la habitacion con el id digitado en el parametro

**DELETE** `/Rooms/ Delete`
- Elimina la habitacion con el id digitado en el parametro


## 🚀 Rutas de habitaciones

**GET** `/Reservation/ List Reservation`
- Devuelve la lista de las reservaciones registradas.  
  
**POST** `/Reservation/ Create`
- Crea nuevas reservaciones

**GET** `/Reservation/ Get Reservation`
- Devuelve la reserva de la habitacion con el id digitado en el parametro

**PUT** `/Reservation/ Update`
- Modifica el registro del la reserva con el id digitado en el parametro

**DELETE** `/Reservation/ Delete`
- Elimina el registro con el id digitado en el parametro

# Guía de Autorización - Sistema de Gestión de Reservas

## Resumen del Sistema de Autorización

Este sistema implementa autorización basada en roles (RBAC) con dos niveles de acceso:

### Roles Disponibles
- **`user`**: Usuario regular del sistema
- **`admin`**: Administrador con acceso completo

## Endpoints y Permisos

### 🔐 Autenticación
- **POST** `/auth/token` - Login para obtener token JWT
- **Requerido**: Credenciales válidas (email/password)

### 👥 Usuarios (`/users`)

#### Usuario Regular (`user`)
- ✅ **GET** `/users/{user_id}` - Ver su propio perfil
- ✅ **PUT** `/users/{user_id}` - Actualizar su propio perfil
- ❌ **GET** `/users/` - Ver todos los usuarios
- ❌ **POST** `/users/` - Crear usuarios
- ❌ **DELETE** `/users/{user_id}` - Eliminar usuarios

#### Administrador (`admin`)
- ✅ **GET** `/users/` - Ver todos los usuarios
- ✅ **GET** `/users/{user_id}` - Ver cualquier usuario
- ✅ **POST** `/users/` - Crear usuarios
- ✅ **PUT** `/users/{user_id}` - Actualizar cualquier usuario
- ✅ **DELETE** `/users/{user_id}` - Eliminar cualquier usuario

### 🏠 Habitaciones (`/Rooms`)

#### Usuario Regular (`user`)
- ✅ **GET** `/Rooms/` - Ver todas las habitaciones
- ✅ **GET** `/Rooms/{room_id}` - Ver habitación específica
- ❌ **POST** `/Rooms/` - Crear habitaciones
- ❌ **PUT** `/Rooms/{room_id}` - Actualizar habitaciones
- ❌ **DELETE** `/Rooms/{room_id}` - Eliminar habitaciones

#### Administrador (`admin`)
- ✅ **GET** `/Rooms/` - Ver todas las habitaciones
- ✅ **GET** `/Rooms/{room_id}` - Ver habitación específica
- ✅ **POST** `/Rooms/` - Crear habitaciones
- ✅ **PUT** `/Rooms/{room_id}` - Actualizar habitaciones
- ✅ **DELETE** `/Rooms/{room_id}` - Eliminar habitaciones

### 📅 Reservas (`/Reservations`)

#### Usuario Regular (`user`)
- ✅ **POST** `/Reservations/` - Crear sus propias reservas
- ✅ **GET** `/Reservations/` - Ver solo sus reservas
- ✅ **GET** `/Reservations/my-reservations/` - Ver sus reservas (endpoint específico)
- ✅ **GET** `/Reservations/{reservation_id}` - Ver sus propias reservas
- ✅ **PUT** `/Reservations/{reservation_id}` - Actualizar sus propias reservas
- ✅ **DELETE** `/Reservations/{reservation_id}` - Eliminar sus propias reservas
- ✅ **DELETE** `/Reservations/{reservation_id}/cancel` - cancelar sus propias reservas

#### Administrador (`admin`)
- ✅ **POST** `/Reservations/` - Crear reservas para cualquier usuario
- ✅ **GET** `/Reservations/` - Ver todas las reservas
- ✅ **GET** `/Reservations/my-reservations/` - Ver sus propias reservas
- ✅ **GET** `/Reservations/{reservation_id}` - Ver cualquier reserva
- ✅ **PUT** `/Reservations/{reservation_id}` - Actualizar cualquier reserva
- ✅ **DELETE** `/Reservations/{reservation_id}` - Eliminar cualquier reserva
- ✅ **DELETE** `/Reservations/{reservation_id}/cancel` - cancelar cualquier  reservas

## Cómo Usar la Autorización

### 1. Obtener Token
```bash
POST /auth/token
Content-Type: application/x-www-form-urlencoded

username=tu_email@ejemplo.com&password=tu_password
```

### Requests
```bash
username: email
password: contraseña
```