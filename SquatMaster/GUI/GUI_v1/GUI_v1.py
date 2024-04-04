#%% Import libraries
import customtkinter as ctk

#%% Set the color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#%% Build simple logging system

root = ctk.CTk()
root.geometry('500x350')

def login():
    print('Test')
def remember():
    print('Remember')

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login system')
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember me', command=remember)
checkbox.pack(pady=12, padx=10)

root.mainloop()


# %%
