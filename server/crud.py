from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

import app_models, schemas


# Batch CRUD functions

def get_batch(db: Session, batch_id: int) -> Optional[app_models.Batch]:
    return db.query(app_models.Batch).filter(app_models.Batch.id == batch_id).first()

def get_batches(db: Session, skip: int = 0, limit: int = 100) -> List[app_models.Batch]:
    return db.query(app_models.Batch).offset(skip).limit(limit).all()

def create_batch(db: Session, batch: schemas.BatchCreate) -> app_models.Batch:
    db_batch = app_models.Batch(**batch.dict())
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch


# ClassificationResult CRUD functions

def get_classification_result(db: Session, classification_result_id: int) -> Optional[app_models.ClassificationResult]:
    return db.query(app_models.ClassificationResult).filter(app_models.ClassificationResult.id == classification_result_id).first()

def get_classification_results(db: Session, batch_id: Optional[int] = None, skip: int = 0, limit: int = 100) -> List[app_models.ClassificationResult]:
    query = db.query(app_models.ClassificationResult)
    if batch_id:
        query = query.filter(app_models.ClassificationResult.batch_id == batch_id)
    return query.offset(skip).limit(limit).all()

def create_classification_result(db: Session, classification_result: schemas.ClassificationResultCreate) -> app_models.ClassificationResult:
    db_classification_result = app_models.ClassificationResult(**classification_result.dict())
    db.add(db_classification_result)
    db.commit()
    db.refresh(db_classification_result)
    return db_classification_result

def create_result_image(db: Session, result_image: schemas.ResultImageCreate, result_id: int) -> app_models.ResultImage:
    db_result_image = app_models.ResultImage(**result_image.dict(), result_id=result_id)
    db.add(db_result_image)
    db.commit()
    db.refresh(db_result_image)
    return db_result_image


def get_result_image(db: Session, result_image_id: int):
    return db.query(app_models.ResultImage).filter(app_models.ResultImage.id == result_image_id).first()


def get_result_images(db: Session, skip: int = 0, limit: int = 100):
    return db.query(app_models.ResultImage).offset(skip).limit(limit).all()
    
    
def delete_result_image(db: Session, result_image_id: int):
    result_image = db.query(app_models.ResultImage).filter(app_models.ResultImage.id == result_image_id).first()
    db.delete(result_image)
    db.commit()
    return result_image