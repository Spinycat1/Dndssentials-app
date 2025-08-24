def write_to_save(textbox_name):
    inventory_text = textbox_name.get("0.0", "end")
    file_save = open("inventory_save.txt", "w")
    file_save.write(inventory_text)
    file_save.close()
