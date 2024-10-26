from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения к базе данных.
# Замените на ваши данные для доступа к базе данных.
DATABASE_URL = "postgresql+psycopg2://user:password@hostname/database_name"

# Создание движка для взаимодействия с базой данных.
engine = create_engine(DATABASE_URL)

# Создание сессии для работы с базой данных.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс, от которого будут наследоваться все модели.
Base = declarative_base()
