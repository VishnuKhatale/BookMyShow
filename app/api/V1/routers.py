from fastapi import APIRouter
from .endpoints import users as UserRouter, city as CityRouter, theater as TheaterRouter
from .endpoints import screen as ScreenRouter, movie as MovieRouter , seat as SeatRouter, show as ShowRouter

Router = APIRouter()
Router.include_router(UserRouter.router, prefix="/users", tags=["Users"])
Router.include_router(CityRouter.router, prefix="/masters", tags=["City Master"])
Router.include_router(TheaterRouter.router, prefix="/masters", tags=["Theater Master"])
Router.include_router(ScreenRouter.router, prefix="/masters", tags=["Screen Master"])
Router.include_router(SeatRouter.router, prefix="/masters", tags=["Seat Master"])
Router.include_router(MovieRouter.router, prefix="/masters", tags=["Movie Master"])
Router.include_router(ShowRouter.router, prefix="/masters", tags=["Show Master"])