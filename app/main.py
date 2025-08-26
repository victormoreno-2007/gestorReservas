from fastapi import FastAPI
from .routes.users.UsersRoutes import router as users_router
from .routes.rooms.RoomsRoutes import router as rooms_router
from .routes.reservations.ReservationsRoutes import router as reservation_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(rooms_router, prefix="/Rooms", tags=["Rooms"])
app.include_router(reservation_router, prefix="/Reservations", tags=["Reservations"])