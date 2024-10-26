from fastapi import FastAPI
from app.users import view
from app.database import engine, Base

# Создаем все таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем маршруты
app.include_router(view.router)
