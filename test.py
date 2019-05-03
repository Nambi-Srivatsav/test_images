import io
import os
import argparse
import pdb
from google.cloud import vision
from google.cloud.vision import types

parser = argparse.ArgumentParser()
parser.add_argument("--file_name")
args = parser.parse_args()

file_name = args.file_name

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
#response = client.label_detection(image=image)
#labels = response.label_annotations
#print(labels)

response = client.text_detection(image=image)
texts = response.text_annotations
#print(texts)
print(texts[0].description)

"""
for text in texts:
	print(text.description)
"""
