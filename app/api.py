from fastapi import FastAPI, UploadFile, File, HTTPException
from app.settings import settings
from app.annotation_builder import AnnotationBuilder
from pydantic import BaseModel
from app.files import save_file, load_file_to_dataframe
import uuid

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

class AnnotationRequest(BaseModel):
    file_id: str
    criteria: str
    examples: list[dict]
    explain: bool = False

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print(file.content_type)
    if file.content_type not in settings.ACCEPTED_FILE_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file extension")
    if file.size > settings.MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")
    
    content = await file.read()
    file_id = str(uuid.uuid4())
    
    save_file(file_id, content)
    
    return {"file_id": file_id}

@app.post("/annotate")
async def create_annotation(request: AnnotationRequest):
    
    data = load_file_to_dataframe(request.file_id) 
    
    annotation_builder = AnnotationBuilder(
        data,
        request.criteria,
        request.examples,
        request.explain
    )
    
    return {"annotation": "result"} 




