from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class ImageData(BaseModel):
    datauri: str
    
class ResultImageBase(BaseModel):
    image_data: bytes


class ResultImageCreate(ResultImageBase):
    pass


class ResultImage(ResultImageBase):
    id: int
    result_id: int

    class Config:
        orm_mode = True


class ClassificationResultBase(BaseModel):
    class_name: str
    batch_id: int
    created_at: datetime
    probability: float = 0.0


class ClassificationResultCreate(ClassificationResultBase):
    pass


class ClassificationResult(ClassificationResultBase):
    id: int
    batch_id: int
    images: List[ResultImage] = []

    class Config:
        orm_mode = True


class BatchBase(BaseModel):
    date: datetime
    batch_name: str
    product_model: str
    department: str
    total_items: int


class BatchCreate(BatchBase):
    pass


class Batch(BatchBase):
    id: int
    classification_results: List[ClassificationResult] = []

    class Config:
        orm_mode = True
