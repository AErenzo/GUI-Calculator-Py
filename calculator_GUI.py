from tkinter import*

#GUI properties
# Create a variable for the GUI space, assign the template Tk
gui = Tk()
# Set the dymensions for the GUI space
gui.geometry("360x460")
# Set the title of the GUI
gui.title("Calculator")
# Create a varieble for the GUI label, assign the properties of the label
guilabel = Label(gui, text="Calculator", bg='White', font=('Univers', 35, 'bold'))
# packing the properties for the gui label and positioning it on the top
guilabel.pack(side=TOP)
# config the gui properties, ready to be called. Set background to dark grey
gui.config(background='Grey')





# creating variable for data user data entry
textin = StringVar()
# create a global varieble for for the operator button being used
selector = ""

# Button click functions, numbers 'and' oporator chosen
# creating a function to determine number button clicked using lambda

def buttonclk(number):
	global selector
	selector = selector+str(number)
	textin.set(selector)


# oporation functions

def opobut():
	global selector
	add = str(eval(selector))
	textin.set(add)
	selector = ''

def opobut():
	global selector
	subt = str(eval(selector))
	textin.set(subt)
	selector = ''

def opobut():
	global selector
	multi = str(eval(selector))
	textin.set(multi)
	selector = ''

def opobut():
	global selector
	divi = str(eval(selector))
	textin.set(divi)
	selector = ''

#function for clean button

def clrbtn():
	textin.set('')

#creating buttons for gui

guitext = Entry(gui, font=('Univers', 12, 'bold'), textvar=textin, width=25, bd=5, bg='light blue')
guitext.pack()

btn1 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(1), text="1", font=('Univers', 16, 'bold'))
btn1.place(x=10, y=100)

btn2 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(2), text="2", font=('Univers', 16, 'bold'))
btn2.place(x=10, y=170)

btn3 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(3), text="3", font=('Univers', 16, 'bold'))
btn3.place(x=10, y=240)

btn4 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(4), text="4", font=('Univers', 16, 'bold'))
btn4.place(x=75, y=100)

btn5 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(5), text="5", font=('Univers', 16, 'bold'))
btn5.place(x=75, y=170)

btn6 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(6), text="6", font=('Univers', 16, 'bold'))
btn6.place(x=75, y=240)

btn7 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(7), text="7", font=('Univers', 16, 'bold'))
btn7.place(x=140, y=100)

btn8 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(8), text="8", font=('Univers', 16, 'bold'))
btn8.place(x=140, y=170)

btn9 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(9), text="9", font=('Univers', 16, 'bold'))
btn9.place(x=140, y=240)

btn0 = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk(0), text="0", font=('Univers', 16, 'bold'))
btn0.place(x=10, y=310)

btndot = Button(gui, padx=47, pady=14, bd=4, bg='white', command=lambda:buttonclk("."), text=".", font=('Univers', 16, 'bold'))
btndot.place(x=75, y=310)

btnplus = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk("+"), text="+", font=('Univers', 16, 'bold'))
btnplus.place(x=205, y=100)

btnminus = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk("-"), text="-", font=('Univers', 16, 'bold'))
btnminus.place(x=205, y=170)

btnmulti = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk("*"), text="*", font=('Univers', 16, 'bold'))
btnmulti.place(x=205, y=240)

btndivid = Button(gui, padx=14, pady=14, bd=4, bg='white', command=lambda:buttonclk("/"), text="/", font=('Univers', 16, 'bold'))
btndivid.place(x=205, y=310)

btnclr = Button(gui, padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbtn, font=('Univers', 16, 'bold'))
btnclr.place(x=270, y=100)

btnequal = Button(gui, padx=151, pady=14, bd=4, bg='white', text="=", command=opobut, font=('Univers', 16, 'bold'))
btnequal.place(x=10, y=380)

gui.mainloop()

