from sqlalchemy import BLOB, TEXT, Column, Integer, LargeBinary, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base

class Batch(Base):
    __tablename__ = "Batch"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    batch_name = Column(String(255), index=True)
    product_model = Column(String(255), index=True)
    department = Column(String(255), index=True)
    total_items = Column(Integer)

    classification_results = relationship("ClassificationResult", back_populates="batch")


class ClassificationResult(Base):
    __tablename__ = "ClassificationResult"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(10), index=True)
    batch_id = Column(Integer, ForeignKey("Batch.id"))
    created_at = Column(DateTime)
    probability = Column(Float(5, 4), nullable=False, default=0.0, server_default='0.0')

    batch = relationship("Batch", back_populates="classification_results")
    images = relationship("ResultImage", back_populates="result")


class ResultImage(Base):
    __tablename__ = "result_images"

    id = Column(Integer, primary_key=True, index=True)
    image_data = Column(BLOB)
    result_id = Column(Integer, ForeignKey("ClassificationResult.id"))

    result = relationship("ClassificationResult", back_populates="images")
