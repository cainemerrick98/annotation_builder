import os
from app.settings import settings

def save_uploaded_file(file_id: str, content: bytes):
    with open(os.path.join(settings.UPLOAD_FOLDER, f"{file_id}.csv"), "wb") as f:
        f.write(content)

def save_annotated_file(file_id: str, content: bytes):
    with open(os.path.join(settings.ANNOTATED_FOLDER, f"{file_id}.csv"), "wb") as f:
        f.write(content)

def load_file_to_dataframe(file_id: str, use_test_folder: bool = False):
    """
    Load a file (CSV or Excel) into a pandas DataFrame.
    
    Args:
        file_id: The ID of the file to load
        use_test_folder: If True, load from test data folder, otherwise from uploads folder
        
    Returns:
        A pandas DataFrame containing the file data
    """
    import pandas as pd
    
    # Choose the appropriate folder based on the environment
    folder = settings.TEST_DATA_FOLDER if use_test_folder else settings.UPLOAD_FOLDER
    file_path = os.path.join(folder, f"{file_id}")
    
    for ext in settings.ACCEPTED_FILE_EXTENSIONS:
        if os.path.exists(file_path + ext):
            return pd.read_csv(file_path + ext)
    raise FileNotFoundError(f"No file found for ID {file_id} with accepted extensions")
