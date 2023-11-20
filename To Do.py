import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

root = Tk()
root.geometry("500x500")

#Font
my_font = Font(
	family="calibri",
	size=30,
	weight="bold")

#Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#List box
my_list = Listbox(my_frame,
	font=my_font,
	width=35,
	height=5,
	bg="SystemButtonFace",
	bd=0,
	fg="#000000",
	highlightthickness=0,
	selectbackground="#FF0000",
	activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

#Instruction list
instruction_list = ["Welcome to your notes.","Add, Cross off and Delete","tasks using the buttons below."]
#Display INstructions in list box
for item in instruction_list:
    my_list.insert(END, item)

#Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#Add Scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Text box
my_entry = Entry(root, font=("Calibri", 24), width=26)
my_entry.pack(pady=20)

#Button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions
def delete_item():
	my_list.delete(ANCHOR)

def add_item():
	my_list.insert(END, my_entry.get())
	my_entry.delete(0, END)

def cross_off_item():
	# Cross off item
	my_list.itemconfig(
		my_list.curselection(),
		fg="#dedede")
	
	# Get rid of selection bar
	my_list.selection_clear(0, END)

def uncross_item():
	# Cross off item
	my_list.itemconfig(
		my_list.curselection(),
		fg="#000000")
	# Get rid of selection bar
	my_list.selection_clear(0, END)

def delete_crossed():
	count = 0
	while count < my_list.size():
		if my_list.itemcget(count, "fg") == "#dedede":
			my_list.delete(my_list.index(count))
		
		else: 
			count += 1

def save_list():
	file_name = filedialog.asksaveasfilename(
		initialdir="C:/gui/data",
		title="Save File",
		filetypes=(
			("Dat Files", "*.dat"), 
			("All Files", "*.*"))
		)
	if file_name:
		if file_name.endswith(".dat"):
			pass
		else:
			file_name = f'{file_name}.dat'

		# Delete crossed off items before saving
		count = 0
		while count < my_list.size():
			if my_list.itemcget(count, "fg") == "#dedede":
				my_list.delete(my_list.index(count))
			
			else: 
				count += 1

		# grab all the stuff from the list
		stuff = my_list.get(0, END)

		# Open the file
		output_file = open(file_name, 'wb')

		# Actually add the stuff to the file
		pickle.dump(stuff, output_file)


def open_list():
	file_name = filedialog.askopenfilename(
		initialdir="C:/gui/data",
		title="Open File",
		filetypes=(
			("Dat Files", "*.dat"), 
			("All Files", "*.*"))
		)

	if file_name:
		# Delete currently open list
		my_list.delete(0, END)

		# Open the file
		input_file = open(file_name, 'rb')

		# Load the data from the file
		stuff = pickle.load(input_file)

		# Output stuff to the screen
		for item in stuff:
			my_list.insert(END, item)


def delete_list():
	my_list.delete(0, END)

#Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add items to Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
#Dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)


#Add Buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed)
#Button positions
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()
