import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk, ImageDraw


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.initializeUI()

    def initializeUI(self):
        self.root.geometry("300x400+50+50")
        self.root.title("2.1 - User Profile GUI")
        self.root.resizable(False, False)
        self.setUpMainWindow()

    def create_circular_image(self, image_path, size=90):
        try:
            img = Image.open(image_path)

            crop = img.crop((0, 0, img.width, img.height))
            crop = crop.resize((size, size), Image.Resampling.LANCZOS)

            mask = Image.new('L', (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)

            output = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            output.paste(crop, (0, 0))
            output.putalpha(mask)

            return ImageTk.PhotoImage(output)
        except Exception as e:
            print(f"Image not found.\nError: {e}")
            return None

    def createImageLabels(self):
        bg_frame = tk.Frame(self.root, bg="#6EC6F6", width=300, height=155)
        bg_frame.place(x=0, y=0)

        image_path = "../dz_lk4_tkinker/images/profile_image.jpeg"
        photo = self.create_circular_image(image_path, size=90)

        if photo:
            photo_label = Label(self.root, image=photo, bg="#6EC6F6")
            photo_label.image = photo  # Сохраняем ссылку
            photo_label.place(x=110, y=10)

    def setUpMainWindow(self):
        self.createImageLabels()

        user_label = Label(self.root, text="Максим Зименс",
                           font=("Arial", 20), bg="white")
        user_label.place(x=60, y=120)

        bio_label = Label(self.root, text="Биография",
                          font=("Arial", 17, "bold"), bg="white")
        bio_label.place(x=15, y=155)

        about_label = Label(self.root,
                            text="Я студент 2-го курса ВУЗ МАИ",
                            font=("Arial", 12),
                            bg="white",
                            justify="left",
                            wraplength=270)
        about_label.place(x=15, y=180)

        skills_label = Label(self.root, text="Умения",
                             font=("Arial", 17, "bold"), bg="white")
        skills_label.place(x=15, y=225)

        languages_label = Label(self.root, text="Python | Excel",
                                font=("Arial", 11), bg="white")
        languages_label.place(x=15, y=250)


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg="white")
    window = MainWindow(root)
    root.mainloop()
