from fastapi import FastAPI
from app.routes.users.UsersRoutes import router as users_router
from app.routes.rooms.RoomsRoutes import router as rooms_router
from app.routes.reservations.ReservationsRoutes import router as reservation_router
from app import auth


app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(rooms_router, prefix="/Rooms", tags=["Rooms"])
app.include_router(reservation_router, prefix="/Reservations", tags=["Reservations"])
app.include_router(auth.router)