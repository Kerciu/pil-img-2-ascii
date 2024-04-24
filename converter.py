# TODO SCALE THE IMAGE
# TODO TRANSFORM TO THE SHADES OF GREY
# TODO MAP PIXELS TO ASCII
# TODO RENDER TEXT FILE

import os, sys
from PIL import Image


def openImage(fileHandle: str) -> Image:
    try:
        imageData = {}
        with Image.open(fileHandle) as im:
            imageData["height"] = im.height
            imageData["mode"] = im.mode
            imageData["width"] = im.width
            imageData["colors"] = im.getcolors()
            imageData["histogram"] = im.histogram()
            imageData["format"] = im.format

    except FileNotFoundError:
        raise FileNotFoundError("File was not found")
    except Exception as e:
        raise Exception("There was an error while processing your image: ", e)

    return imageData
