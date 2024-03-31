from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table,delete_table
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_table()
    print('Приложение запущено')
    # await delete_table()
    # print('База данных очищена')
    yield
    print('Приложение выключено')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
