#Import Library Required
import tkinter
import tkinter.messagebox
from tkinter import *
import customtkinter
import Functions as F
from PIL import Image


#Setting Color Theme
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Create App Object
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Plagarisim Checker")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, padx = (20,10), pady = (20,20), sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Welcome to \nPlagarism Checker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text_color=("black","white"), text="HOMOEPAGE", command=self.Homepage)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text_color=("black","white"), text="COMPARE TWO FILES", command=self.TwoFilePage)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text_color=("black","white"), text = "MULTIPLE COMPARE", command=self.MultipleFilePage)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame,text_color=("black","white"), text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,text_color=("black","white"), values=["Light", "Dark", "System"],
                                                                       command=F.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame,text_color=("black","white"), text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,text_color=("black","white"), values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=F.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        #Set Default values
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        self.Homepage()



    def Homepage(self):
        Frame = customtkinter.CTkFrame(self, corner_radius = 10)
        Frame.grid_columnconfigure((0), weight=1)
        Frame.grid_rowconfigure((0), weight=1)
        Frame.grid(row = 0, column = 1, padx=(10,20), pady=(20,20), rowspan = 4, columnspan = 3, sticky="nsew")
        Banner = customtkinter.CTkImage(light_image=Image.open("light_bg.png"),dark_image=Image.open("dark_bg.png"), size=(900,540))

        Banner_label = customtkinter.CTkLabel(Frame, text = "",image=Banner)
        Banner_label.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nsew")


    def TwoFilePage(self):
        Frame = customtkinter.CTkFrame(self, corner_radius = 10)
        Frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        Frame.grid_rowconfigure((0,1,2,3,4), weight=1)
        Frame.grid(row = 0, column = 1, padx=(10,20), pady=(20,20), rowspan = 4, columnspan = 3, sticky="nsew")
        Label = customtkinter.CTkLabel(Frame,text_color=("black","white"), text="CHOOSE TWO FILES", font=customtkinter.CTkFont(size=20, weight="bold"))
        Label.grid(row=0, column=0, columnspan=5, padx=20, pady=(20, 20), sticky="ew")

        Button_1_text = tkinter.StringVar()
        Button_1_text.set("CHOOSE FILE 1")
        Button_1 = customtkinter.CTkButton(Frame,text_color=("black","white"), textvariable= Button_1_text, command = lambda:F.OpenFile1(Button_1_text))
        Button_1.grid(row=1, column=1, padx=20, pady=20, sticky ="ew")

        Button_2_text = tkinter.StringVar()
        Button_2_text.set("CHOOSE FILE 2")
        Button_2 = customtkinter.CTkButton(Frame,text_color=("black","white"), textvariable=Button_2_text,  command = lambda:F.OpenFile2(Button_2_text))
        Button_2.grid(row=1, column=3, padx=20, pady=20, sticky ="ew")

        Button_3 = customtkinter.CTkButton(Frame,text_color=("black","white"), text = "CHECK PLAGIARISM",  command = lambda:F.TwoFileCompareResult(textbox))
        Button_3.grid(row=2, column=2, padx=20, pady=20, sticky = "ew")

        textbox = customtkinter.CTkTextbox(Frame)
        textbox.grid(row=3, column=0, columnspan= 5, rowspan= 3, padx=(20,20), pady=(20,20), sticky="nsew")


    def MultipleFilePage(self):
        Frame = customtkinter.CTkFrame(self, width = 500, corner_radius = 10)
        Frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        Frame.grid_rowconfigure((0,1,2,3,4), weight=1)
        Frame.grid(row = 0, column = 1, padx=(10,20), pady=(20,20), rowspan = 4, columnspan = 3, sticky="nsew")

        Button_text = tkinter.StringVar()
        Button_text.set("CHOOSE FILES")
        Button = customtkinter.CTkButton(Frame,text_color=("black","white"), textvariable= Button_text, command = lambda:F.OpenFiles(Button_text))
        Button.grid(row=0, column=1, padx=20, pady=20, sticky ="ew")

        Button = customtkinter.CTkButton(Frame,text_color=("black","white"), text= "Check Plagarism", command = lambda:F.MultipleCompareResult(textbox))
        Button.grid(row=0, column=3, padx=20, pady=20, sticky ="ew")

        textbox = customtkinter.CTkTextbox(Frame)
        textbox.grid(row=1, column=0, columnspan= 5, rowspan= 4, padx=(20,20), pady=(20,20), sticky="nsew")




if __name__ == "__main__":
    app = App()
    app.mainloop()
