from random import randint

def entry_value_casting(entry_value):
    try:
        value_intermediate = int(entry_value)
        integer_output = abs(value_intermediate)
        return integer_output
    except ValueError:
        return 0

def dice_roll(dice_value_var, dice_quantity, text_box):
    text_box.configure(state="normal")
    text_box.delete("0.0", "end")
    dice_value = dice_value_var.get()
    if dice_value == "d4":
        value_to_int = 4
    elif dice_value == "d6":
        value_to_int = 6
    elif dice_value == "d8":
        value_to_int = 8
    elif dice_value == "d10":
        value_to_int = 10
    elif dice_value == "d12":
        value_to_int = 12
    elif dice_value == "d20":
        value_to_int = 20
    elif dice_value == "d100":
        value_to_int = 100
    else:
        text_box.insert("end", "Invalid dice value. \n")
        return
    
    for i in range(dice_quantity):
        roll = randint(1, value_to_int)
        text_box.insert("end", f"{roll}\n")
    text_box.configure(state="disabled")
    
