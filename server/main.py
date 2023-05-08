import base64
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
import uuid
from ai_model.ai_model import AIModel
import crud
from database import SessionLocal, engine
from image_utils.image_utils import ImageUtils
import app_models
import schemas
from fastapi.middleware.cors import CORSMiddleware
app_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS
origins = ["http://localhost", "http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:3000", "http://127.0.0.1:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/save_image/")
# async def save_image(image_data: schemas.ImageData):
#     # Generate a unique file name if it doesn't exist
#     file_name = f"{uuid.uuid4()}.png"
#     save_path = f"images/{file_name}"

#     # Save the image to disk
#     save_base64_image(image_data.datauri, save_path)

#     return {"message": "Image saved successfully."}


@app.post("/evaluate_pwb/")
async def evaluate_pwb(image_data: schemas.ImageData):

    # Save the image to disk
    image = ImageUtils.read_base64_image(image_data.datauri)
    ai_model = AIModel()
    result = ai_model.classify(image)
    evaluation = ai_model.evaluate(result)

    return {"result": evaluation}


@app.post("/batch/", response_model=schemas.Batch)
def create_batch(batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    db_batch = crud.create_batch(db=db, batch=batch)
    return db_batch


@app.post("/classification_result/", response_model=schemas.ClassificationResult)
def create_classification_result(classification_result: schemas.ClassificationResultCreate, db: Session = Depends(get_db)):
    db_classification_result = crud.create_classification_result(
        db=db, classification_result=classification_result)
    return db_classification_result


@app.get("/batch/{batch_id}", response_model=schemas.Batch)
def read_batch(batch_id: int, db: Session = Depends(get_db)):
    db_batch = crud.get_batch(db, batch_id=batch_id)
    if db_batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return db_batch


@app.get("/classification_result/{result_id}", response_model=schemas.ClassificationResult)
def read_classification_result(result_id: int, db: Session = Depends(get_db)):
    db_classification_result = crud.get_classification_result(
        db, result_id=result_id)
    if db_classification_result is None:
        raise HTTPException(
            status_code=404, detail="Classification Result not found")
    return db_classification_result


@app.get("/batch/", response_model=list[schemas.Batch])
def read_batches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    batches = crud.get_batches(db, skip=skip, limit=limit)
    return batches


@app.get("/classification_result/", response_model=list[schemas.ClassificationResult])
def read_classification_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_classification_results(db, skip=skip, limit=limit)
    return results


@app.post("/result_image/", response_model=schemas.ResultImage)
def create_result_image(result_id: int, result_image: schemas.ResultImageCreate, db: Session = Depends(get_db)):
    db_result_image = crud.create_result_image(
        db=db, result_image=result_image, result_id=result_id)
    return db_result_image


@app.get("/result_images/{result_image_id}", response_model=schemas.ResultImage)
def read_result_image(result_image_id: int, db: Session = Depends(get_db)):
    db_result_image = crud.get_result_image(
        db=db, result_image_id=result_image_id)
    if db_result_image is None:
        raise HTTPException(status_code=404, detail="ResultImage not found")
    return db_result_image


@app.get("/classification_results/{result_id}/images", response_model=list[schemas.ResultImage])
def read_result_images(result_id: int, db: Session = Depends(get_db)):
    db_result_images = crud.get_result_images(db, result_id=result_id)
    if db_result_images is None:
        raise HTTPException(status_code=404, detail="ResultImages not found")
    return db_result_images


@app.delete("/result_images/{result_image_id}", response_model=schemas.ResultImage)
def delete_result_image(result_image_id: int, db: Session = Depends(get_db)):
    db_result_image = crud.delete_result_image(
        db=db, result_image_id=result_image_id)
    if db_result_image is None:
        raise HTTPException(status_code=404, detail="ResultImage not found")
    return db_result_image
