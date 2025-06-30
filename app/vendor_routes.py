from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal
from fastapi import Query
from typing import Optional, List
import logging
from sqlalchemy import or_

# Настройка логирования
logger = logging.getLogger(__name__)


router = APIRouter()

# Получение сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /vendors — регистрация нового продавца
@router.post("/vendors", response_model=schemas.VendorOut)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Vendor).filter(models.Vendor.email == vendor.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Vendor with this email already exists")
    new_vendor = models.Vendor(**vendor.dict())
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    logger.info(f"Создан продавец: {new_vendor.name} ({new_vendor.email})")

    return new_vendor

# GET /vendors — получение списка продавцов с пагинацией и поиском
@router.get("/vendors", response_model=List[schemas.Vendor])
def get_all_vendors(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Vendor)

    if search:
        query = query.filter(
            or_(
                models.Vendor.name.ilike(f"%{search}%"),
                models.Vendor.email.ilike(f"%{search}%"),
                models.Vendor.company.ilike(f"%{search}%")
            )
        )

    vendors = query.offset(offset).limit(limit).all()
    logger.info(f"Получены продавцы (limit={limit}, offset={offset}, search='{search}')")
    return vendors

# Получение одного продавца по ID
@router.get("/vendors/{vendor_id}", response_model=schemas.VendorOut)
def get_vendor(vendor_id: int, db: Session = Depends(get_db)):
    vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    
    logger.info(f"Получен продавец ID={vendor_id}")

    return vendor

# Обновление информации о продавце
@router.put("/vendors/{vendor_id}", response_model=schemas.VendorOut)
def update_vendor(vendor_id: int, updated_vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    
    # Проверка уникальности email при обновлении
    email_exists = db.query(models.Vendor).filter(models.Vendor.email == updated_vendor.email, models.Vendor.id != vendor_id).first()
    if email_exists:
        raise HTTPException(status_code=400, detail="Another vendor with this email already exists")
    
    vendor.name = updated_vendor.name
    vendor.email = updated_vendor.email
    vendor.company = updated_vendor.company

    db.commit()
    db.refresh(vendor)

    logger.info(f"Обновлён продавец ID={vendor_id}")

    return vendor

# Удаление продавца
@router.delete("/vendors/{vendor_id}")
def delete_vendor(vendor_id: int, db: Session = Depends(get_db)):
    vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    
    db.delete(vendor)
    db.commit()

    logger.info(f"Удалён продавец ID={vendor_id}")

    return {"detail": "Vendor deleted successfully"}
