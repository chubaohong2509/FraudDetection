import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import joblib
import pandas as pd 
from sklearn import datasets
from sklearn.linear_model import Perceptron 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
from PIL import ImageTk, Image
#loadmodel
model = joblib.load('Fraudmodel.pkl')
def preprocess_data(data):
    # Implement your data preprocessing steps here
    # ...
    preprocessed_data = data  # Placeholder, replace with actual preprocessing steps
    return preprocessed_data
def reset():
    type_combobox.set("")
    amount_entry.delete(0,'end')
    old_entry.delete(0,'end')
    new_entry.delete(0,'end')
def detect_fraud():
    typee = type_combobox.get()
    amount=amount_entry.get()
    old=old_entry.get()
    new=new_entry.get()
    if typee and amount and old and new:
        final_type = type_to_value[typee]
        typ=int(final_type)
        amount=int(amount_entry.get())
        old=int(old_entry.get())
        new=int(new_entry.get())
     
        
    
    
        x = preprocess_data([typ,amount,old,new])
        x = np.array(x)
        x = x.reshape(1, -1)
        predictions = model.predict(x)
        if predictions == 1:
            messagebox.showwarning("Fraud Detected", "Fraudulent transaction detected!")
        else:
            messagebox.showinfo("Fraud Detection", "No fraud detected.")
    else:
        messagebox.showwarning("Warning","Please fill in all the information!")
# create the root window
window = tk.Tk()
window.geometry('500x700')
window.resizable(False,False)
window.title('Fraud Detection')
window.configure(bg="#005f69")
label=tk.Label(window,text="Nguyễn Thị Phương Thoa - 31211025778",font=("Arial",15),bg="#005f69",fg="#f26f33").place(x=70,y=650)
image = Image.open('fraud.png')
image = image.resize((250,200))
python_image = ImageTk.PhotoImage(image)
# create label
image_label = tk.Label(window, image=python_image)

image_label.place(x=140,y=430)

# label with a specific font
label = tk.Label(window,text='Online Payment Fraud Detection',font=("Arial", 
20, "bold"),background="#005f69", foreground= '#f26f33')
label.pack()
frame=tk.Frame(window,bg="#005f69")
frame.pack()
info_frame = tk.LabelFrame(frame, bg="#005f69",fg="#f26f33",font=("Arial", 
15),text='User Information')
info_frame.grid(row=0, column=0, padx=30, pady=10, sticky='news')

# Row 0 in User Info
amount_label = tk.Label(info_frame,width=17,fg="#f26f33",bg="#005f69",font=("Arial", 
15), text='Amount of transaction')
amount_label.grid(row=0, column=0)
type_label = tk.Label(info_frame, width=15,bg="#005f69",fg="#f26f33",font=("Arial", 
15),text="Type of transaction")
type_label.grid(row=0, column=1)

# Row 1 in User Info
amount_entry = tk.Entry(info_frame,font=("Arial", 
13))
amount_entry.insert(0,' balance before the transaction')
amount_entry.grid(row=1, column=0)
type_combobox = ttk.Combobox(info_frame,font=("Arial", 
13),background="#005f69", values=["", "Cash in", "Cash out", "Payment","Debit","Transfer"])
type_combobox.grid(row=1, column=1)
type_to_value = {"Cash in": 0, "Cash out": 1, "Payment": 2, "Debit": 3, "Transfer": 4}

old_label = tk.Label(info_frame, width=20,bg="#005f69",fg="#f26f33",font=("Arial", 
15),text="OldbalanceOrig")
old_label.grid(row=2, column=0)
new_label = tk.Label(info_frame, width=15,bg="#005f69",fg="#f26f33",font=("Arial", 
15),text="NewbalanceOrig")
new_label.grid(row=2, column=1)
old_labelDest = tk.Label(info_frame, width=20,bg="#005f69",fg="#f26f33",font=("Arial", 
15),text="OldbalanceDest")
old_labelDest.grid(row=4, column=0)
new_labelDest = tk.Label(info_frame, width=15,bg="#005f69",fg="#f26f33",font=("Arial", 
15),text="NewbalanceDest")
new_labelDest.grid(row=4, column=1)
# Row 1 in User Info

old_entry = tk.Entry(info_frame,font=("Arial", 
13))
new_entry = tk.Entry(info_frame,font=("Arial", 
13))
old_entry.grid(row=3, column=0)
new_entry.grid(row=3, column=1)
old_entryDest = tk.Entry(info_frame,font=("Arial", 
13))
new_entryDest = tk.Entry(info_frame,font=("Arial", 
13))
old_entryDest.grid(row=5, column=0)
new_entryDest.grid(row=5, column=1)

for widget in info_frame.winfo_children():
    widget.grid_configure(padx=7, pady=9)

test_button = tk.Button(frame, width=10, text="Detect Fraud",bg="#005f69",fg="#f26f33", font=("Arial", 
13),command= detect_fraud)
test_button.grid(row=2, column=0, padx=20, pady=20) 
reset_button = tk.Button(frame,width=10, text="Reset",fg="#f26f33", font=("Arial", 
13),bg="#005f69", command= reset)
reset_button.place( x=20, y=332)



window.mainloop()