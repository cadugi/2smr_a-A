import tkinter as tk
import random

class DesktopGoose:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Goose")
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "white")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.goose_image = tk.PhotoImage(file="C:/Users/a.carrero.AULA_2SMR/Documents/python/tonterias/icono/goose.png")  # Replace with your goose image
        self.goose = self.canvas.create_image(0, 0, image=self.goose_image, anchor=tk.NW)
        
        self.image_width = self.goose_image.width()  # Width of the image
        self.image_height = self.goose_image.height()  # Height of the image

        self.dx = random.randint(5, 15)  # Velocity in the x direction
        self.dy = random.randint(5, 15)  # Velocity in the y direction

        self.move_goose()

    def move_goose(self):
        self.canvas.move(self.goose, self.dx, self.dy)
        self.root.after(50, self.move_goose)  # Adjust the delay for the desired speed

        # Check if the goose hits the edge of the screen and make it bounce
        x1, y1, x2, y2 = self.canvas.coords(self.goose)
        if x1 <= 0 or x2 >= self.root.winfo_screenwidth():
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.root.winfo_screenheight():
            self.dy = -self.dy

        # Scale the image to make it smaller and bounce when it hits the edges
        self.canvas.scale(self.goose, 0, 0, 0.9, 0.9)  # Scale down by 10%
        self.image_width *= 0.9
        self.image_height *= 0.9
        self.goose_image = self.goose_image.subsample(2)  # Make the image smaller

root = tk.Tk()
goose = DesktopGoose(root)
root.mainloop()
