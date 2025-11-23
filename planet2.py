import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.initializeUI()

    def initializeUI(self):
        self.root.geometry("800x700")
        self.root.title("Пример Label")
        self.setUpMainWindow()

    def setUpMainWindow(self):
        image_path = '../dz_lk4_tkinker/123.png'
        try:
            img = Image.open(image_path)
            img = img.resize((600, 600), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            world_label = Label(self.root, image=photo)
            world_label.image = photo
            world_label.place(x=100, y=100)
        except Exception as error:
            print(f"Image not found.\nError: {error}")

        hello_label = Label(self.root, text="Hello, World!",
                            font=("Arial", 22,),
                            fg="Blue")
        hello_label.place(x=300, y=100)


if __name__ == '__main__':
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()

