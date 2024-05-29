import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from data_base.database import create_tables

from api import users_router, products_router, orders_router

app = FastAPI(
    summary="Разработка серверной части веб-сервиса для онлайн-аптеки"
)

app.include_router(users_router.router)
app.include_router(products_router.router)
app.include_router(orders_router.router)

create_tables()


@app.get("/", summary="Получить основную страницу")
def main():
    return FileResponse("assets/index.html")


if __name__ == "__main__":
    uvicorn.run(app)
