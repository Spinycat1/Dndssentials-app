import customtkinter as ctk
from dndssentials_lib import *
import atexit
from tkinter import PhotoImage
import os

app = ctk.CTk()
app.geometry("500x500")
app.title("DnD-ssentials")

tabs = ctk.CTkTabview(app) #creates the tabview widget in the app window
tabs.pack(fill="both", expand=True) #puts it in the window and expands it to fill the whole window

tabs.add("Homepage") #the homepage tab (the starting one)
tabs.add("Dice Roller") #the dice roller tab
tabs.add("Stats Roller") #the stat roller tab
tabs.add("Inventory Manager") #the inventory tab

#Homepage items#
homepage = tabs.tab("Homepage")
home_title_label = ctk.CTkLabel(homepage,
    text="DnD-ssentials",
    font=("Times New Roman", 30)
    )
home_title_label.pack(pady=30)
homepage_intro_label = ctk.CTkLabel(homepage,
    text="""Welcome to DnD-ssentials,
    the digital dnd toolbox for players and dungeon masters alike!

    Access the tools you need using the tabs above.""",
    font=("Times New Roman", 15),
    width=30
    )
homepage_intro_label.pack(pady=30)

#Dice roller items#
diceroller = tabs.tab("Dice Roller")
dice_title_label = ctk.CTkLabel(diceroller,
    text="Dice Roller",
    font=("Times New Roman", 30)
    )
dice_title_label.pack(pady=30)

dice_combobox_var = ctk.StringVar(value="d4") #variable for the combobox
dice_combobox = ctk.CTkComboBox(diceroller, #combobox
    values=["d4", "d6", "d8", "d10", "d12", "d20", "d100"], #options for combobox and their values
    variable=dice_combobox_var,
    state="readonly" #only avaliable input for combobox is the options listed above
    )
dice_combobox.pack(pady=10)

dice_quantity_entry = ctk.CTkEntry(diceroller,
    placeholder_text="Quantity of dice" 
    )
dice_quantity_entry.pack(pady=10)
dice_quantity = dice_quantity_entry.get() #takes in the value of the entry field as a string
dice_quantity_int = entry_value_casting(dice_quantity)

dice_enter_button = ctk.CTkButton(diceroller,
    text="Enter",
    width=60,
    state="disabled"
    )
dice_enter_button.pack(pady=30)

roll_output_box = ctk.CTkTextbox(diceroller,
    width=300,
    height=300,
    font=("Times New Roman", 15),
    state="disabled",
    corner_radius=10
    )
roll_output_box.pack(pady=10)

def dice_enter_pressed(): #to update the values of the combobox and entry
    quantity_string = dice_quantity_entry.get()
    quantity_int = entry_value_casting(quantity_string)
    if quantity_int and quantity_int > 0:
        dice_roll(dice_combobox_var, quantity_int, roll_output_box)
    else:
        roll_output_box.delete("0.0", "end")
        roll_output_box.insert("end", "Invalid quantity\n")

dice_enter_button.configure(command=dice_enter_pressed) #gives the button function when pressed

def update_button_state(event=None): #function to enable button when the entry field is valid.
    value = dice_quantity_entry.get()
    result = entry_value_casting(value)
    if result is not None and result > 0:
        dice_enter_button.configure(state="normal")
    else:
        dice_enter_button.configure(state="disabled")

dice_quantity_entry.bind("<KeyRelease>", update_button_state) #when a button is released when in the entry, the update_button_state will trigger and update the button state accordingly.

#Stats roller items#

statroller = tabs.tab("Stats Roller")
stats_title_label = ctk.CTkLabel(statroller,
    text="Stats Roller",
    font=("Times New Roman", 30)
    )
stats_title_label.pack(pady=30) #this is just the title of the page

stat_roll_button = ctk.CTkButton(statroller,
    text="Roll",
    font=("Times New Roman", 15),
    width=60,
    command=lambda: stat_rolling_func(stats_textbox)
)
stat_roll_button.pack(pady=20) # When the user presses the button, it will activate the function to roll the stats

stats_textbox = ctk.CTkTextbox(statroller,
    width=400,
    height=300,
    font=("Times New Roman", 15),
    corner_radius=10,
    state="disabled"
)
stats_textbox.pack(pady=30) #this is the textbox where the stat roller output will end up.

#Inventory manager items#
inventorymanager = tabs.tab("Inventory Manager")
inventory_label = ctk.CTkLabel(inventorymanager,
    text="Inventory Manager",
    font=("Times New Roman", 30)
    )
inventory_label.pack(pady=30)

inventory_save_file = open("inventory_save.txt")
inventory_display = inventory_save_file.read()

inventory_save_button = ctk.CTkButton(inventorymanager,
    width=100,
    text="Save",
    font=("Times New Roman", 15),
    command=lambda: write_to_save(inventory_textbox) 
)
inventory_save_button.pack(pady=10)

inventory_textbox = ctk.CTkTextbox(inventorymanager,
    width=450,
    height=400,
    corner_radius=10    
)
inventory_textbox.pack(pady=30)
inventory_textbox.insert("end", text=f"{inventory_display}")

def app_cleanup():
    if not inventory_save_file.closed:
        inventory_save_file.close()

atexit.register(app_cleanup)

app_directory = os.path.dirname(__file__)
icon_path = os.path.join(app_directory, "resources", "dndssentials_icon.ico")
app.iconbitmap(icon_path)

app.mainloop()

