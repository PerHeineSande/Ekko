import requests
import base64
from PIL import Image
import io

def generate_image(prompt):
    response = requests.post('http://localhost:7860/sdapi/v1/txt2img',
        json={
            "prompt": prompt,
            "negative_prompt": "blurry, bad quality",
            "steps": 20,
            "width": 512,
            "height": 512,
        })
    
    image_data = response.json()['images'][0]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    image.save('output.png')
    print("Image saved as output.png")

generate_image("a cat sitting on a mountain, photorealistic")