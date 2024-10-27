from fastapi import FastAPI
from app.users import view as user_router
from app.articles import view as article_router
from app.user_interactions import view as user_interactions_router
# from app.database import engine, Base

# Создаем все таблицы
# Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем маршруты
app.include_router(user_router.router)
app.include_router(article_router.router)
app.include_router(user_interactions_router.router, prefix="/api", tags=["interactions"])
