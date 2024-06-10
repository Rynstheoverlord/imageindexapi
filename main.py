from fastapi import FastAPI
import random
import json

app = FastAPI()

with open("images.json", 'r') as img:
    images = json.load(img)["images"]


@app.get("/")
def all_images():
    return {"images": images}


@app.get("/random")
def random_image():
    image = random.choice(images)
    return {"image": image}