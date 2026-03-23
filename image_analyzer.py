from openai import OpenAI
import base64
import json

client = OpenAI()

def analyze_item(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    prompt = """
    Analyze this clothing item image.
    
    Identify:
    1. The clothing item type
    2. The main color or pattern of the clothing item
    
    Return ONLY valid JSON in this exact format:
    {
        "item_type": "...",
        "main color": "..."
        }"""
    
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt}, 
                    {
                        "type": "input_image", 
                        "image_url": f"data:image/jpeg;base64,{base64_image}"
                    }
                ]
            }
        ]
    )

    output_text = response.output_text
    return json.loads(output_text)