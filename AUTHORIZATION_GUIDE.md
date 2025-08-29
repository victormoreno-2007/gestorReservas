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

#### Administrador (`admin`)
- ✅ **POST** `/Reservations/` - Crear reservas para cualquier usuario
- ✅ **GET** `/Reservations/` - Ver todas las reservas
- ✅ **GET** `/Reservations/my-reservations/` - Ver sus propias reservas
- ✅ **GET** `/Reservations/{reservation_id}` - Ver cualquier reserva
- ✅ **PUT** `/Reservations/{reservation_id}` - Actualizar cualquier reserva
- ✅ **DELETE** `/Reservations/{reservation_id}` - Eliminar cualquier reserva

## Cómo Usar la Autorización

### 1. Obtener Token
```bash
POST /auth/token
Content-Type: application/x-www-form-urlencoded

username=tu_email@ejemplo.com&password=tu_password
```

### 2. Usar Token en Requests
```bash
GET /users/me
Authorization: Bearer tu_token_jwt_aqui
```

### 3. Ejemplos de Uso

#### Como Usuario Regular:
```bash
# Ver mis reservas
GET /Reservations/my-reservations/
Authorization: Bearer tu_token

# Crear una reserva para mí
POST /Reservations/
Authorization: Bearer tu_token
{
  "idUsers": 1,  # Debe ser tu ID
  "idRooms": 1,
  "fecha": "2024-01-15",
  "horaInicio": "09:00:00",
  "horaFin": "11:00:00"
}
```

#### Como Administrador:
```bash
# Ver todas las reservas
GET /Reservations/
Authorization: Bearer tu_token_admin

# Crear reserva para otro usuario
POST /Reservations/
Authorization: Bearer tu_token_admin
{
  "idUsers": 2,  # ID de cualquier usuario
  "idRooms": 1,
  "fecha": "2024-01-15",
  "horaInicio": "09:00:00",
  "horaFin": "11:00:00"
}
```

## Códigos de Error

- **401 Unauthorized**: Token inválido o expirado
- **403 Forbidden**: No tienes permisos para esta acción
- **404 Not Found**: Recurso no encontrado

## Seguridad

- Los tokens JWT expiran en 20 minutos
- Las contraseñas se hashean con bcrypt
- Todas las operaciones sensibles requieren autenticación
- Los usuarios solo pueden acceder a sus propios datos (excepto admin)
