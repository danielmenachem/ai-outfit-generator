import uuid
import os
from flask import Flask, render_template, request
from vision import detect_dominant_color

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

@app.route("/", methods=["GET", "POST"])
def home():
    
    result = None
    
    if request.method == "POST":
        outfit_request = request.form.get("outfit-request")
        image_file = request.files.get("item-image")

        if image_file and image_file.filename != "":
            unique_filename = str(uuid.uuid4()) + ".jpg"
            file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            image_file.save(file_path)
            
            dominant_color = detect_dominant_color(file_path)

            result = {
                "filename": unique_filename,
                "request": outfit_request,
                "color": dominant_color
            }
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)