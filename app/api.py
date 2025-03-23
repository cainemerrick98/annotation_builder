from fastapi import FastAPI, UploadFile, File, HTTPException
from app.settings import settings
from app.annotation_builder import AnnotationBuilder
from pydantic import BaseModel
from app.files import save_uploaded_file, save_annotated_file, load_file_to_dataframe
import uuid
from fastapi.responses import StreamingResponse
from io import StringIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

class AnnotationRequest(BaseModel):
    file_id: str
    criteria: list[str]
    examples: list[dict]
    explain: bool = False

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print(file.content_type)
    if file.content_type not in settings.ACCEPTED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")
    if file.size > settings.MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")
    
    content = await file.read()
    file_id = str(uuid.uuid4())
    
    save_uploaded_file(file_id, content)
    
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

    annotated_data = annotation_builder.annotate_data()
    
    csv_content = annotated_data.to_csv(index=False)
    save_annotated_file(request.file_id, csv_content.encode("utf-8"))
    
    stream = StringIO(csv_content)
    
    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=annotated_{request.file_id}.csv"}
    )




