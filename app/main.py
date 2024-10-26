from fastapi import FastAPI
from users.router import router as users_router
from articles.router import router as articles_router
from tags.router import router as tags_router
from user_interactions.router import router as interactions_router

app = FastAPI()

app.include_router(users_router, prefix="/api/users")
app.include_router(articles_router, prefix="/api/articles")
app.include_router(interactions_router, prefix="/api/interactions")
app.include_router(tags_router, prefix="/api/tags")