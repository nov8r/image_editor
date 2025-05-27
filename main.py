from PIL import Image


def open_img(imgPath: str) -> bool | str:
    """Opens image from a given path

    Args:
        imgPath (str): Path of an image file

    Returns:
        bool or str: True on success, or error message string on failure
    """
    try:
        im = Image.open(imgPath)
        im.show()
        return True
    except FileNotFoundError:
        return f"Error: Image does not exist in {imgPath}"
    except Exception as e:
        return f"Error: {e}"
