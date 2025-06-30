from pydantic import BaseModel, EmailStr
from typing import Optional

class VendorBase(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None

class VendorOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    company: Optional[str] = None

    class Config:
        from_attributes = True


class VendorCreate(VendorBase):
    pass

class VendorUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    company: Optional[str] = None

class Vendor(VendorBase):
    id: int

    class Config:
        from_attributes = True
