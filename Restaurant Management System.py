from tkinter import *
import random
import time

# Initialize the main application window
root = Tk()
root.geometry("1600x700+0+0")
root.resizable(0, 0)
root.title("Restaurant Management System")

# Frame for the title
Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

# Frame for the main content
f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# Frame for the calculator
f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# Display current time
localtime = time.asctime(time.localtime(time.time()))

# Title Label
lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Restaurant Management System By Amar Kumar", fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)

# Time Label
lbltime = Label(Tops, font=('aria', 20), text=localtime, fg="steel blue", anchor=W)
lbltime.grid(row=1, column=0)

# Calculator variables
text_Input = StringVar()
operator = ""

# Entry display for the calculator
txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white", justify='right')
txtdisplay.grid(columnspan=4)

# Button click functions for the calculator
def btnclick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")

def eqals():
    global operator
    try:
        sumup = str(eval(operator))
        text_Input.set(sumup)
    except Exception:
        text_Input.set("Error")
    operator = ""

# Order calculation
def Ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)

    # Get input values
    cof = float(Fries.get())
    colfries = float(Largefries.get())
    cob = float(Burger.get())
    cofi = float(Filet.get())
    cochee = float(Cheese_burger.get())
    codr = float(Drinks.get())

    # Calculate costs
    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costoffilet = cofi * 50
    costofcheeseburger = cochee * 50
    costofdrinks = codr * 35

    # Total calculations
    total_cost = (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)
    PayTax = total_cost * 0.33
    ServiceCharge = total_cost / 99

    # Set results in the respective fields
    cost.set(f"Rs. {total_cost:.2f}")
    Tax.set(f"Rs. {PayTax:.2f}")
    Service_Charge.set(f"Rs. {ServiceCharge:.2f}")
    Subtotal.set(f"Rs. {total_cost:.2f}")
    Total.set(f"Rs. {total_cost + PayTax + ServiceCharge:.2f}")

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

# Calculator buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('C', 5, 1), ('=', 5, 2), ('.', 5, 3),
    ('/', 5, 3)
]

for (text, row, col) in buttons:
    action = clrdisplay if text == 'C' else eqals if text == '=' else lambda x=text: btnclick(x)
    Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=text, bg="powder blue", command=action).grid(row=row, column=col)

# Status label
status = Label(f2, font=('aria', 15, 'bold'), width=16, text="-By Amar Kumar", bd=2, relief=SUNKEN)
status.grid(row=7, columnspan=3)

# Variables for order entries
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

# Order entry labels and inputs
labels = [
    ("Order No.", rand), ("Fries Meal", Fries), ("Lunch Meal", Largefries),
    ("Burger Meal", Burger), ("Pizza Meal", Filet), ("Cheese Burger", Cheese_burger),
    ("Drinks", Drinks), ("Cost", cost), ("Service Charge", Service_Charge),
    ("Tax", Tax), ("Subtotal", Subtotal), ("Total", Total)
]

for idx, (text, var) in enumerate(labels):
    Label(f1, font=('aria', 16, 'bold'), text=text, fg="steel blue", bd=10, anchor='w').grid(row=idx, column=0)
    Entry(f1, font=('ariel', 16, 'bold'), textvariable=var, bd=6, insertwidth=4, bg="powder blue", justify='right').grid(row=idx, column=1)

# Buttons for total, reset, and exit
btns = [
    ("TOTAL", Ref), ("RESET", reset), ("EXIT", qexit)
]

for idx, (text, cmd) in enumerate(btns):
    Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text=text, bg="powder blue", command=cmd).grid(row=7, column=idx + 1)

# Price list function (if needed)
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    # Add your price list implementation here

# Run the application
root.mainloop()
