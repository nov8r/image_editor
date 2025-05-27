from main import open_img


def test_open():
    result = open_img("C:\\Users\\ethan\\Desktop\\image_editor\\images\\Headshot.JPG")
    assert result
