import os
import uuid 

UPLOAD_FOLDER = "static/uploads"

def save_image(image_file):
    unique_filename = str(uuid.uuid4()) + ".jpeg"
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    
    image_file.save(file_path)

    return unique_filename, file_path
