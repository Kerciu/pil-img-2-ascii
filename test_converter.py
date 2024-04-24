from converter import Converter
import pytest
from PIL import Image
import copy


valid_image = "436723673_960194535814578_393422992170066543_n.jpg"


def test_openImage_file_not_found():
    with pytest.raises(FileNotFoundError):
        Converter.openImage("non_existent_image.jpg")


def test_openImage_invalid_image():
    with pytest.raises(Exception):
        Converter.openImage("invalid_image.jpg")


def test_openImage_valid_image():
    image = Converter.openImage(valid_image)
    assert isinstance(image, Image.Image)


def test_scaleImage_valid_image():
    image = Image.new("RGB", (100, 100))
    scaled_image = Converter.scaleImage(image, 50, 50)
    assert scaled_image.size == (50, 50)


def test_scaleImage_invalid_image():
    invalid_image = "invalid_image"
    with pytest.raises(Exception):
        Converter.scaleImage(invalid_image, 50, 50)


def test_scaleImage_zero_dimensions():
    image = Image.new("RGB", (100, 100))
    scaled_image = Converter.scaleImage(image, 0, 0)
    assert scaled_image.size == (1, 1)


def test_scaleImage_negative_dimensions():
    image = Image.new("RGB", (100, 100))
    scaled_image = Converter.scaleImage(image, -50, -50)
    assert scaled_image.size == (1, 1)


def test_transformToGrey_success():
    im = Image.new("RGB", (100, 100), color="red")
    im_grey = im.convert('L')
    result = Converter.transformToGrey(copy.deepcopy(im))
    assert result.mode == "L"
    assert result.size == im.size
    assert result.tobytes() == im_grey.tobytes()


def test_transformToGrey_exception():
    with pytest.raises(Exception):
        Converter.transformToGrey(None)


def test_getAverage():
    grey_image = Image.new("L", (100, 100), color=128)
    expected_average = 128
    average = Converter.getAverage(grey_image)
    assert average == expected_average


def test_getAverage_black_image():
    black_image = Image.new("L", (50, 50), color=0)
    expected_average = 0
    average = Converter.getAverage(black_image)
    assert average == expected_average


def test_getAverage_white_image():
    white_image = Image.new("L", (200, 200), color=255)
    expected_average = 255
    average = Converter.getAverage(white_image)
    assert average == expected_average
