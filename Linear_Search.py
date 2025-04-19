import tkinter as tk
from PIL import ImageTk,Image
def linear_search(list1,num):
    for i in range(len(list1)):
        if list1[i]==num:
            return True
    return False
def highlight_label(index):
    boxes[index].config(bg="yellow")
def remove_highlight(index):
    boxes[index].config(bg="lightgrey")
def highlight_label1(index):
    boxes[index].config(bg="red")
def label_reset():
    label.config(text="Output will be shown here", font=("Times New Roman", 28,'bold italic'), background='#32e6ff',fg="Black",
                 highlightbackground='black', highlightthickness=3)
def show_output(list1):
    try:
        num=float(entry.get())
        found=False
        for i,element in enumerate(list1):
            if element == num:
                found = True
                label.config(text=f"{element}={num}\nNumber {num} found at Index No.{i} ", font=('Fira Code bold', 28), fg='black', justify='center')
                highlight_label1(i)
                window.update()
                window.after(1500)
                remove_highlight(i)
                window.update()
                window.after(800)
                label_reset()
                break
            else:
                label.config(text=f"{element} != {num}\nSearching Continues...", font=('Fira Code semi bold', 28), fg='black')
                highlight_label(i)
                window.update()
                window.after(1400)
                remove_highlight(i)
        if not found:
            label.config(text=f"Number {num} not found in the List", font=('Fira Code bold', 28), fg='red')
            window.update()
            window.after(2300)
            label_reset()
    except ValueError:
        label.config(text="Invalid Input Type, Please Enter an Integer or Float Value !", font=('Fira Code bold', 25), fg='black')
        window.update()
        window.after(2300)
        label_reset()
def create_entry_boxes():
    try:
        size = int(size_entry.get())
        if size > 10:
            size = 10
        elif size <= 1:
            size=0
            label.config(text='Enter Size More than 1!!',font=('Fira Code bold', 28), fg='red')
            window.update()
            window.after(2300)
            label_reset()
        for i in range(size):
            box = tk.Entry(boxframe, width=10, bg='lightgrey', fg="black", justify='center', font=('comic sans ms bold', 14), border=2, relief=tk.SOLID)
            box.grid(row=0, column=i, padx=4, pady=3)
            boxes.append(box)
    except ValueError:
        label.config(text="Enter only Integer Value for Size !!",font=('Fira Code bold', 25), fg='red')
        window.update()
        window.after(2300)
        label_reset()
def get_list_input():
    try:
        list_values =[float(box.get()) for box in boxes]
        return list_values
    except ValueError:
        label.config(text="Enter only Float or Integer Values for the List !!",font=('Fira Code bold', 25), fg='red')
        window.update()
        window.after(2300)
        label_reset()
window = tk.Tk()
window.title("Linear Search Representation using GUI")
window.config(width=1366, height=768, background='#32e6ff')
header = tk.Label(window, text="LINEAR SEARCH", padx=15, pady=8, borderwidth=3, relief=tk.SOLID,
                  background='white',highlightbackground='black', highlightthickness=2)
header.config(font=('Times New Roman Bold',30,"underline"))
header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
size_label = tk.Label(window, text="Enter the Size of the List (Max 10):",font=("Times New Roman Bold",20), background='#32e6ff')
size_label.place(relx=0.37, rely=0.25, anchor=tk.CENTER)
size_entry =tk.Entry(window, justify='center', font=('comic sans ms bold', 14), border=2.6, relief=tk.SOLID,width=15)
size_entry.place(relx=0.588, rely=0.25, anchor=tk.CENTER)
image1=Image.open('submit.jpg')
image1 =image1.resize((90,40))
photo1=ImageTk.PhotoImage(image1)
submit_button = tk.Button(window,command=create_entry_boxes,border=2, relief=tk.RAISED,image=photo1)
submit_button.place(relx=0.7, rely=0.25, anchor=tk.CENTER)
boxframe = tk.Frame(window)
boxframe.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
boxframe.config(background='#73ff60', border=3, relief=tk.SOLID)
boxes = []
label = tk.Label(window, text="Output will be Shown Here", font=("Times New Roman", 28,'bold italic'),
                 background='#32e6ff',fg="Black",highlightbackground='black', highlightthickness=3)
label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
search_frame=tk.Frame(window,background='#32e6ff',height=74,width=750).place(relx=0.220,rely=0.45)
search_text=tk.Label(search_frame,text="Enter The Item To Search :- ",font=("Times New Roman Bold",20,"bold italic"),
                     background='#32e6ff').place(relx=0.235,rely=0.475)
entry = tk.Entry(search_frame, justify='center', font=('comic sans ms bold', 14), border=10, fg="red",
                 relief=tk.RIDGE, highlightbackground='black', highlightthickness=2)
entry.place(relx=0.588, rely=0.5, height=47, anchor=tk.CENTER)
image = Image.open('Search.png')
image = image.resize((30,30))
photo= ImageTk.PhotoImage(image)
button = tk.Button(search_frame, command=lambda:show_output(get_list_input()),image=photo)
button.place(x=100, y=0,relx=0.65, rely=0.5, anchor=tk.CENTER)
button.config(borderwidth=3.5, relief=tk.SOLID)
window.mainloop()