import os

from PIL import Image


# Image opening function
def open_img(imgPath: str) -> Image.Image | None:
    """Opens image from a given path

    Args:
        imgPath (str): Path of an image file

    Returns:
        Image or None: Returns image on success, else returns none on failure
    """
    try:
        return Image.open(imgPath).copy()
    except FileNotFoundError:
        print(f"Error: Image does not exist in {imgPath}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def save_img(img: Image.Image, savePath: str) -> None:
    """Save the image after modifications are made

    Args:
        im (Image): Image to be saved
        savePath (str): Path for the image to be saved to

    Returns:
        str: Returns an error if saving succeeds or fails
    """
    try:
        file_ext = os.path.splitext(savePath)[1].lower()
        if file_ext == ".jpg" or file_ext == ".jpeg":
            img.save(savePath, format="JPEG", quality=90)
        else:
            img.save(savePath)
    except Exception as e:
        print(f"Error saving image to {savePath}: {e}")


def rotate_img(img: Image.Image) -> Image.Image:
    """Rotates an image 90 degrees

    Args:
        img (Image.Image): The image to be rotated

    Returns:
        Image.Image: The rotated image
    """
    return img.rotate(90)


def resize_img(img: Image.Image, width: int, height: int) -> Image.Image:
    """Resizes a given image by width and height

    Args:
        img (Image.Image): The image to be resized
        width (int): Width to resize to (in pixels)
        height (int): Height to resize to (in pixels)

    Returns:
        Image.Image: Resized image
    """
    return img.resize((width, height), resample=5)
