from flask import Flask, render_template, request
from services.image_service import save_image
from image_analyzer import analyze_item

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    
    result = None
    
    if request.method == "POST":
        outfit_request = request.form.get("outfit-request")
        image_file = request.files.get("item-image")

        if image_file and image_file.filename != "":
            unique_filename, file_path = save_image(image_file)
            
            analysis = analyze_item(file_path)

            result = {
                "filename": unique_filename,
                "request": outfit_request,
                "analysis": analysis
            }
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)