"""
# Import library for building a TCP server-client
import socket
# Import library to work with directories and files
import os
# Import libraries to build GUI 
import tkinter as tk
from tkinter import *
from tkinter import filedialog
# Import library for encryption and decryption of files. 
from cryptography.fernet import Fernet 


# Creating a socket that will create a server and help connect to the client.
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Sockets needs a host and port to connect to the server.
# Here we define the host as the local host and a random port.
HOST = socket.gethostname()
PORT = 65444

# Creating a server with assigned Host and Port
server_socket.bind((HOST,PORT))
print("Server Socket Created")

# Listening for connections. We limit the number of concurrent connections to 1.
server_socket.listen(1)
  
while True:
    
# Accepting a client connection to the server and confirming the same. 
    clientsocket,addr = server_socket.accept()    
    print("Client Connected")
   

    server_socket.close()        





# Define function to print contents of received file to 'Text Output File'             
    def print_to_file(event):

# Dialog to select the file that needs to be printed to the text output file. 
        filename = filedialog.askopenfilename(
            initialdir ="C:/Users/Desktop/Server/",
            title = "Open File to Print to File",
            )
        filesize = os.path.getsize(filename)   

# Here the contents of the selected file are printed to the text output file.         
        with open(filename,"r",encoding='utf-8') as infile:
            with open("TextOutPutFile.txt",'a',encoding='utf-8') as outfile: 
                for line in infile:
                    outfile.write(line)
                    
# Function to display the contents of the selected file to the screen                 
    def print_to_screen(event):

# A function to open a dialog to select a file and make the contents available
        def openFile():           
            tf = filedialog.askopenfilename(
                initialdir="C:/Users/Desktop/Server/", 
                title="Open file to display", 
                filetypes=(("Text Files", "*.*"),)
                )
            pathh.insert(END, tf)
            tf = open(tf,'r',encoding = 'utf-8')
            data = tf.read()
            txtarea.insert(END, data)
            tf.close()

# Open a window that will be used to dispay the contents of a selected file
        ws = tk.Tk()
        ws.title("File Contents")
        ws.geometry("650x650")
        ws['bg']='black'

# Adding a text area to the window to display the contents of the file
        txtarea = Text(ws, width=65, height=25)
        txtarea.pack(pady=20)

# Adding a box that will display the selected file path
        pathh = Entry(ws)
        pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

# Adding a button that calls the openFile function to select a file to display
        Button(
            ws, 
            text="Open File", 
            command=openFile
            ).pack(side=RIGHT, expand=True, fill=X, padx=20)
# Opening the windown for file selection and display
        ws.mainloop()

# Opening the main server window that will be used as an interface
    window = tk.Tk()
    window.title("Server Interface")

# Server interface will have four buttons 
    window.rowconfigure([0], minsize=50,weight = 1)
    window.columnconfigure([0,1,2,3],minsize=50,weight = 1)

# Creating a button with binding that prints the contents of a file to the screen
    btn_scprnt = tk.Button(master=window,text="Print Contents to Screen")
    btn_scprnt.grid(row=0, column=0, sticky = "nsew",padx=5,pady=5)
    btn_scprnt.bind("<Button-1>",print_to_screen)

# Creating a button with binding that prints the contents of a file to the text output file
    btn_fprnt = tk.Button(master=window,text="Print Contents to File")
    btn_fprnt.grid(row=0,column=1,sticky ="nsew",padx=5,pady=5)
    btn_fprnt.bind("<Button-1>",print_to_file)

# Creating a button with binding that closes the client connection, server and window       
    btn_allcloser = tk.Button(master=window,text = "Close Server and Window")
    btn_allcloser.grid(row=0,column=3,sticky="nsew",padx=5,pady=5)



# Creating a button with binding that decrypts a selected text file    
    btn_decrypt = tk.Button(master=window,text = "Decrypt Text File")
    btn_decrypt.grid(row=0,column=2,sticky="nsew",padx=5,pady=5)

    

# Opening up the main server window.      
    window.mainloop()    

    break

    
    



