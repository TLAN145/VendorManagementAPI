from fastapi import FastAPI
from app import models, database
from app.vendor_routes import router as vendor_router
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


app = FastAPI(title="Vendor Management API")

# Создание таблиц
models.Base.metadata.create_all(bind=database.engine)

# Подключение маршрутов
app.include_router(vendor_router)
