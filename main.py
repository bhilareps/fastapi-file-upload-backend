from fastapi import FastAPI, File, UploadFile
import os
import shutil

# Initialize FastAPI app
app = FastAPI()

# Define the directory where uploaded files will be stored
UPLOAD_DIRECTORY = "./uploaded_files"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# File upload endpoint
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)

    # Save the uploaded file to the specified directory
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "File uploaded successfully!"}

# Optional: Root endpoint to test if the API is working
@app.get("/")
async def root():
    return {"message": "FastAPI file upload service is running!"}
