import tkinter as tk
from tkinter import ttk
from acrylic import Color

checklist=[]

# LAYOUT:
#                                       ______________________________
box_head =                                      "Graveyard"
#                                       ______________________________
title =                                         "The Idea Graveyard"
#                                       ______________________________
name_prompt, add_button_text =          "Enter a new idea: " , 'Add'
m1_prompt, m2_prompt, m3_prompt =   "Potential returns: ", "Likelihood of success: ", "Attackability: "
#                                       ______________________________
#                                       [ ] thing 1
#                                       [x] thing 2
#                                       [ ] thing 3
#                                       [x] thing 4
#                                       [x] thing 5
#                                       ______________________________


# CREATE MEMORY FILE <<<---------------
# WRITE MEMORY FILE  <<<---------------

print("👉 program launched")

# ADD ITEMS
def add():
    text = name_entry_box.get()
    m1 = int(m1_entry_box.get())
    m2 = int(m2_entry_box.get())
    m3 = int(m3_entry_box.get())
    color = Color(rgb=[m1, m2, m3])
    color_hex = color.hex
    instance_style = f'Header{color_hex}.TLabel'
    print(f'👉 {instance_style = }')
    style.configure(instance_style, background="white", foreground=color_hex, font=("Arial", 14, 'bold'))

    if text != "" and text.isspace() == False:
        name_entry_box.delete(0, tk.END)
        m1_entry_box.delete(0, tk.END)
        m2_entry_box.delete(0, tk.END)
        m3_entry_box.delete(0, tk.END)
        var = tk.BooleanVar(value=False)
        j = ttk.Checkbutton(list_box, text=text, variable=var, onvalue=True, offvalue=False, style=instance_style)
        j.pack(anchor="w", padx=25, pady=2)
        var.set(False)
        checklist.append((text, var))
        update_root(text, var)
    else:
        pass

# UPDATE CHECKLIST
def update_root(text, var):
    list_status = [checklist[i][1].get() for i, a in enumerate(checklist)]
    print(all(list_status[:-1]))
    if all(list_status[:-1]) == True:
        print("box verifyer")
    else:
        pass
    root.update()

# ROOT WINDOW
root = tk.Tk()
root.title(box_head)

# SET STYLE
style = ttk.Style()
style.configure("TFrame", background="white")
style.configure("Header2.TLabel", background="white", foreground="white", font=("Arial", 14, 'bold'))
style.configure("Yellow.TLabel", background="white", foreground="yellow", font=("Arial", 14, 'bold'))
style.configure("Red.TLabel", background="white", foreground="red", font=("Arial", 14, 'bold'))
style.configure("Blue.TLabel", background="white", foreground="blue", font=("Arial", 14, 'bold'))
style.configure("Header1.TLabel", background="white", foreground="white", font=("Arial", 18, 'bold'))
style.configure("TButton", font=("Arial", 12), background="white", foreground="white", padding=0)
style.map("TButton", background=[("active", "white")])

# NEW idea BOX (grid)
new_idea_box = tk.Frame(root)
new_idea_box.pack(fill="both", padx=20, expand=False)

ttk.Label(new_idea_box, text="", font=("Arial", 2)).grid(row=0, column=0, padx=0, pady=0) #blank (grid)

# name box
new_name = ttk.Label(new_idea_box, text=name_prompt, style="Header2.TLabel")
new_name.grid(row=1, column=0, padx=5, pady=0)

name_entry_box = ttk.Entry(new_idea_box, width=25)
name_entry_box.grid(row=1, column=1, padx=5, pady=0)

add_btn = ttk.Button(new_idea_box, text=add_button_text, style='TButton', command=add)
add_btn.grid(row=1, column=2, padx=5, pady=0)

# m1 box
new_m1 = ttk.Label(new_idea_box, text=m1_prompt, style="Header2.TLabel")
new_m1.grid(row=2, column=1, padx=5, pady=0)

m1_entry_box = ttk.Entry(new_idea_box, width=7)
m1_entry_box.grid(row=2, column=2, padx=5, pady=0)

add_btn = ttk.Button(new_idea_box, text=add_button_text, style='TButton', command=add)
add_btn.grid(row=1, column=2, padx=5, pady=0)

# m2 box
new_m2 = ttk.Label(new_idea_box, text=m2_prompt, style="Header2.TLabel")
new_m2.grid(row=3, column=1, padx=5, pady=0)

m2_entry_box = ttk.Entry(new_idea_box, width=7)
m2_entry_box.grid(row=3, column=2, padx=5, pady=0)

add_btn = ttk.Button(new_idea_box, text=add_button_text, style='TButton', command=add)
add_btn.grid(row=1, column=2, padx=5, pady=0)

# m3 box
new_m3 = ttk.Label(new_idea_box, text=m3_prompt, style="Header2.TLabel")
new_m3.grid(row=4, column=1, padx=5, pady=0)

m3_entry_box = ttk.Entry(new_idea_box, width=7)
m3_entry_box.grid(row=4, column=2, padx=5, pady=0)

add_btn = ttk.Button(new_idea_box, text=add_button_text, style='TButton', command=add)
add_btn.grid(row=1, column=2, padx=5, pady=0)

sep = ttk.Separator(root, orient="horizontal")
sep.pack(fill="x", padx=0, pady=5)


# LIST BOX (packing)
list_box = tk.Frame(root, bd=0)
list_box.pack(fill="both", expand=True, padx=1, pady=1)


ideas = ttk.Label(list_box, text=title, style='Header1.TLabel')
ideas.pack(anchor="nw", padx=10, pady=2)
'''
status = quit_button_text
quit_btn = ttk.Button(list_box, text=status, command=root.destroy, style='TButton')
quit_btn.pack(side="bottom")
'''
# ttk.Label(list_box, text="", font=("Arial", 20)) #blank (grid)

# CALL TKINTER
print("👉 starting gui")
root.mainloop()

print("👉 gui killed")
