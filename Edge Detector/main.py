import cv2 as cv2
import os, sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk


root = tk.Tk()
root.withdraw()
filepath = filedialog.askopenfilename()
cv2_image = cv2.imread(filepath,0)
cv2.imwrite("gray.jpeg",cv2_image)
canny_image = cv2.Canny(cv2_image, 200, 200)
cv2.imwrite("canny1.jpeg",canny_image)
root.destroy()

root = tk.Tk()
image = Image.open(filepath)
image_width, image_height = image.size
canvas = tk.Canvas(root,bd = 0, cursor = "arrow", height=image_height, width=image_width)
tk_image = ImageTk.PhotoImage(image)
image = canvas.create_image(image_width/2, image_height/2, anchor = "center",image=tk_image)
canvas.pack()
root.mainloop()
