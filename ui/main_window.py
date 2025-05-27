import tkinter as tk
from tkinter import filedialog as fd

from PIL import ImageTk

from image_processing.operations import open_img, resize_img, rotate_img, save_img


class ImageEditorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Image Editor")
        self.geometry("900x900")
        self.resizable(True, True)
        self._create_menubar()

    def _create_menubar(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Open image...", command=self._open_image)
        file_menu.add_command(label="Save image", command=self._save_image)
        file_menu.add_command(label="Save image as...", command=self._save_image_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Rotate", command=self._rotate_image)
        edit_menu.add_command(label="Resize", command=self._resize_image)

    def _open_image(self):
        file_path = fd.askopenfilename(
            title="Open Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("All files", "*"),
            ],
        )
        if file_path:
            print(f"Selected file: {file_path}")
            self.img = open_img(file_path)
            self.photo = ImageTk.PhotoImage(self.img)
            self.label = tk.Label(self, image=self.photo)
            self.label.place(relx=0.5, rely=0.5, anchor="center")

    def _save_image(self):
        if self.img:
            save_path = fd.asksaveasfilename(
                title="Save Image As...",
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("BMP files", "*.bmp"),
                    ("All files", "*.*"),
                ],
            )
            save_img(self.img, save_path)

    def _save_image_as(self):
        if self.img:
            save_path = fd.asksaveasfilename(
                title="Save Image As...",
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("BMP files", "*.bmp"),
                    ("All files", "*.*"),
                ],
            )
            save_img(self.img, save_path)

    def _rotate_image(self):
        if self.img:
            self.img = rotate_img(self.img)
            self.photo = ImageTk.PhotoImage(self.img)
            self.label.configure(image=self.photo)
            self.label.image = self.photo

    def _resize_image(self):
        if self.img:
            self.img = resize_img(self.img, 400, 400)  # will add dynamic resizing later
            self.photo = ImageTk.PhotoImage(self.img)
            self.label.configure(image=self.photo)
            self.label.image = self.photo
