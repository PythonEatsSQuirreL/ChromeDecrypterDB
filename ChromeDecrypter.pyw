import customtkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import os.path
import os
import sys
import time
import string
import random
import subprocess

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

class MainScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("ChromeDecrypt")
        self.geometry("700x300")
        self.resizable(False, False)
        self.configure(background="white")
        self.grid_columnconfigure(0,weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=180, corner_radius=0, height=300)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.configure(border_width=1, border_color="white")

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Home", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", command=self.display_home_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Save Path", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", command=self.self_decrypting_pre)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="DB File Path", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", command=self.self_decrypting_fille)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Decrypt!", border_width=1, border_color="white", fg_color="DodgerBlue", text_color="white", hover_color="grey",  command=self.self_decrypt_process)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Exit", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", hover=True, command=self.exit)
        self.sidebar_button_5.grid(row=7, column=0, padx=20, pady=12)

        # Create the frame that will appear on the right side of the window
        self.home_frame = customtkinter.CTkFrame(self, width=520, corner_radius=0, height=300)
        self.decrypter_frame = customtkinter.CTkFrame(self, width=520, corner_radius=0, height=300)
        self.other_frame = customtkinter.CTkFrame(self, width=520, corner_radius=0, height=300)

        # Hide the frames initially
        self.display_home_frame()
        self.other_frame.grid_remove()
        self.decrypter_frame.grid_remove()


    def display_home_frame(self):
        # Hide the scripts frame if it is currently displayed
        self.other_frame.grid_remove()
        self.decrypter_frame.grid_remove()
        # Display the home frame
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.configure(border_width=1, border_color="white")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.home_frame, width=300, height=200)
        self.textbox.grid(padx=(20, 0), pady=(20, 0))
        self.textbox.place(relx=0.49, rely=0.41, anchor='center')
        self.textbox.insert("0.0", "Welcome!\n\n" + "Thank you for visiting this small project,\nplease note that this project is currently not\nfinished and can contain bugs.\n\n" + "How to use this ?\n\nPress on 'Save Path' in order to choose where do\n you want to save the decrypted data,\npress on 'DB File Path' in order to choose the file\n you want to decrypt and finally press 'Decrypt!'")
        
        self.textbox.configure(state="disabled")

    def display_home_frame_after(self):
        # Hide the scripts frame if it is currently displayed
        self.other_frame.grid_remove()
        self.decrypter_frame.grid_remove()
        # Display the home frame
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.configure(border_width=1, border_color="white")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.home_frame, width=300, height=200)
        self.textbox.grid(padx=(20, 0), pady=(20, 0))
        self.textbox.place(relx=0.49, rely=0.41, anchor='center')
        #get db name
        ff = str(self.sedecrypt_fille_loc)
        sep = '\\'
        ff = ff.split(sep, -1)[-1]
        #get final file location
        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        file_path_var = os.path.join(current_dir, "var.txt")
        with open(file_path_var, "r") as file:
            lines = file.readlines()
        first_line = lines[0]
        file.close()
        
        self.textbox.insert("0.0", f"Done!\n\n Your file {ff} was decrypted!\n\n You can find all the decrypted data\n stored in the following file: \n\n{first_line}")
        self.textbox.configure(state="disabled")


    def self_decrypting_fille(self):

        self.sedecrypt_fille = askopenfilename()

        self.sedecrypt_fille_loc = os.path.abspath(self.sedecrypt_fille)

        current_fille = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_fille)
        file_path_varr = os.path.join(current_dir, "fl.txt")

        os.path.join(current_dir, "fl.txt")
        mod_pathh = self.sedecrypt_fille_loc
        try:
            with open(file_path_varr, "w") as fille:
                fille.write(str(mod_pathh))
                fille.close()
        except Exception as e:
            print("An error occurred while writing to fl.txt: ", e)

        time.sleep(1)

    def self_decrypting_pre(self):

        self.sedecrypt_save = filedialog.askdirectory()

        self.sedecrypt_save_loc = os.path.abspath(self.sedecrypt_save)


    def self_decrypt_process(self):

        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        file_path_var = os.path.join(current_dir, "var.txt")

        os.path.join(current_dir, "var.txt")

        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        kek = "\\"
        
        mod_path = self.sedecrypt_save_loc + kek + random_string + ".txt"

        try:
            with open(file_path_var, "w") as file:
                file.write(mod_path)
                file.close()
        except Exception as e:
            print("An error occurred while writing to var.txt: ", e)

        time.sleep(1)

        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        file_path_test = os.path.join(current_dir, "sd.py")
        process = subprocess.Popen(['python', file_path_test])

        process.wait()
        
        self.display_home_frame_after()

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    start = MainScreen()
    start.mainloop()