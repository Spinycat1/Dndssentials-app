from random import randint

def stat_rolling_func(textbox_name):
    stat_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"] #stat names
    textbox_name.configure(state="normal")
    textbox_name.delete("0.0", "end")
    for i in range(6): #this will repeat 6 times for the 6 different stats
        rolls = [] #empty "rolls" list
        for j in range(4): #repeats 4 times for the 4 different d6 rolls needed for one stat
            rolls.append(randint(1, 6)) #rolls the d6
        rolls.sort() #sorts the rolls into ascending order
        stat_value = (rolls[1] + rolls[2] + rolls[3]) #adds together the 3 largest numbers in the rolls.
        textbox_name.insert("end", f"{stat_names[i]}: {stat_value} \n")
    textbox_name.configure(state="disabled")
       
