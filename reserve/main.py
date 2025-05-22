from fastapi import FastAPI
from reserve.routers.reservations import router as reserve_router
from reserve.routers.tables import router as tables_router

app = FastAPI(
    title='Reserve service API',
    version='1.0.0'
)

for router in (reserve_router, tables_router):
    app.include_router(router)
