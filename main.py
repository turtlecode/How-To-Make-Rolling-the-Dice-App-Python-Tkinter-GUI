from tkinter import *
import random

root = Tk()
root.geometry("500x500")

def get_number(x):
	if x == '\u2680':
		return(1)
	elif x == '\u2681':
		return(2)
	elif x == '\u2682':
		return(3)
	elif x == '\u2683':
		return(4)
	elif x == '\u2684':
		return(5)
	elif x == '\u2685':
		return(6)

def roll_dice():

	d1 = random.choice(my_dice)
	d2 = random.choice(my_dice)

	sd1 = get_number(d1)
	sd2 = get_number(d2)

	dice_label1.config(text=d1)
	dice_label2.config(text=d2)

	sub_dice_label1.config(text=sd1)
	sub_dice_label2.config(text=sd2)

	total = sd1 + sd2
	total_label.config(text=f"You Rolled: {total}")


my_dice = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685',]

my_frame = Frame(root)
my_frame.pack(pady=20)

dice_label1 = Label(my_frame, text='', font=("Helvetica", 100), fg="black")
dice_label1.grid(row=0, column=0, padx=5)
sub_dice_label1 = Label(my_frame, text="")
sub_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text='', font=("Helvetica", 100), fg="black")
dice_label2.grid(row=0, column=1, padx=5)
sub_dice_label2 = Label(my_frame, text="")
sub_dice_label2.grid(row=1, column=1)

my_button = Button(root, text="Roll Dice", command=roll_dice, font=("Helvetica", 24))
my_button.pack(pady=20)

total_label = Label(root, text="", font=("Helvetica", 24), fg="grey")
total_label.pack(pady=40)

roll_dice()

root.mainloop()