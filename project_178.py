from tkinter import *
import random
root = Tk()
root.title("Encyclopedia")
root.geometry("600x600")

label = Label(root, font = ("cursive", 15, "bold"), bg = "white")
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

class game:
    def __init(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["BLUE", "PINK", "GREEN", "RED", "YELLOW", "CYAN"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["blue", "pink", "green", "red", "yellow", "cyan"]
        self.random_number_for_color = random.randint(0, 5)
        label["text"] = self.text[self.random_number_for_text]
        label["fg"] = self.color[self.random_number_for_color]
        
    def obj(self):
        obj1 = self.updateGame()

btn = Button(root, text = "START", command = obj, bg = "dark olive green", fg = "white", relief = FLAT, padx = 10, pady = 1, font = ("Arial",15))
btn.place(relx = 0.8, rely = 0.8, anchor = CENTER)

root.mainloop()
