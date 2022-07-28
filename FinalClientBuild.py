# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:52:21 2022

@author: Anna
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
#Import library for reading CSV files to build a dictionary.
import csv
# Import library to serialize into JSON format
import json
# Import library to serialize with Binary format
import pickle


# Creating a socket that will connect to the server.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Sockets needs a host and port to connect to the server.
# Here we define the host as the local host and a random port.
HOST = socket.gethostname()
PORT = 65444

#This is a comment to check how GITHUB works 

# Initializing dictionary names
dict_from_csv = {} 
binary_dict = {}


# Define a function that will connect to the server. 
def connect_to_server(event):
    client_socket.connect((HOST,PORT))
    

# Define a function that will send a selected file to the server unencypted.
def unencrypted_send(event):
 
# Create a dialog box to select the file to be sent to the server unencrypted.      
    filename = filedialog.askopenfilename(
        initialdir ="C:/Users/Desktop/",
        title = "Open File to Transfer",
        )
    
# Getting the filesize. Useful if we should want to create progress bars.     
    filesize = os.path.getsize(filename)

# Asking the client to send the file name and filesize to the server.
    client_socket.send(f"{filename}<SEPARATOR>{filesize}".encode())

# Here we are copying the contents of the file
# Split into smaller pieces that will be transferred to the server.
    with open(filename,'rb') as f:
        while True:
            bytes_read = f.read(4096)
            if not bytes_read:
                break

# Finally, we use the client connection to the server to send the file. 
            client_socket.sendall(bytes_read)
            
  
        


# Here we define a function that generates a key and writes it to a file
def write_key(event):
    key = Fernet.generate_key()             #generate a symmetric authenticated key
    with open("key.key",'wb') as key_file:  #opens a file key.key
        key_file.write(key)                 #write the Fernet key to the file
        
# Since this is a unique key, we won't be generating a new kay each encryption


# Hence, we define a function that loads the key for us.
def load_key():
    return open("key.key",'rb').read()

            
# Define a function that will send a selected file to the server encrypted. 
def encrypted_send(event):

# Create a dialog box to select the file to be sent to the server encrypted.        
    filename = filedialog.askopenfilename(
        initialdir ="C:/Users/Desktop/",
        title = "Open File to Transfer",
        )
    
# Getting the filesize. Useful if we should want to create progress bars.      
    filesize = os.path.getsize(filename)
    
# Loading the key with which to encrypt the file.         
    f = Fernet(load_key())
    
    with open(filename,"rb") as file:
        # Read all the file data
        file_data = file.read()
        # Encrypt data
        encrypted_data = f.encrypt(file_data)
        
    # Writing the encrypted file with the same name 
    # Thus, it will override the original    
        
    with open(filename,"wb") as file:
        file.write(encrypted_data)
        
# Asking the client to send the file name and filesize to the server.
    client_socket.send(f"{filename}<SEPARATOR>{filesize}".encode())

# Here we are copying the contents of the file
# Split into smaller pieces that will be transferred to the server.    
    
    with open(filename,'rb') as f:
        while True:
            bytes_read = f.read(4096)
            if not bytes_read:
                break
            
            
# Finally, we use the client connection to the server to send the file.          
            client_socket.sendall(bytes_read)
            
    
# Define a function that will close the connection and the client window.
def close_client(event):
    window.destroy()
    client_socket.close()
    

# Define a function that will import a CSV file and build a dictionary    
def dictionary_creation(event):

# Create a dialog box to select the CSV file to be loaded into a dictionary.    
   tf = filedialog.askopenfilename(
       initialdir="C:/Users/Desktop/", 
       title="Open CSV file", 
       filetypes=(("Text Files", "*.*"),)
       )


# Here we are transfer the contents of the CSV file into a Python dictionary.   
   with open(tf,'r') as inputfile:   
        reader = csv.reader(inputfile)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}

# Function to serialize dictionary with Binary format.
# We write this dictionary into a local client 'write_file'
def dict_to_binary(event):
    with open ("data_file_as_Binary.txt","w") as write_file:
        pickle.dump(dict_from_csv,write_file)

# Function to serialize dictionary with JSON format.
# We write this dictionary into a local client 'write_file'
   
def dict_to_json(event):
    with open("data_file_json.json","w") as write_file:
        json.dump(dict_from_csv,write_file)


# We are creating a GUI to access our client called 'Client Interface'
window = tk.Tk()
window.title("Client Interface")

# Define the window to have 3x3 layout with set size and tracking the window size.  
window.rowconfigure([0,1,2], minsize=50,weight = 1)
window.columnconfigure([0,1,2],minsize=50,weight = 1)

# Creating a button with binding to connect to the server
btn_connect = tk.Button(master=window,text="Connect to Server")
btn_connect.grid(row=0, column=0, sticky = "nsew",padx=5,pady=5)
btn_connect.bind("<Button-1>",connect_to_server)

# Creating a button with binding to send a file unencrypted to the server. 
btn_senduenc = tk.Button(master=window,text="Send File (Unencrypted)")
btn_senduenc.grid(row=0, column=1, sticky = "nsew",padx=5,pady=5)
btn_senduenc.bind("<Button-1>",unencrypted_send)

# Creating a button with binding to import a CSV file and create a dictionary. 
btn_dictimp = tk.Button(master=window,text="Import CSV file to create Dictionary")
btn_dictimp.grid(row=0, column=2, sticky = "nsew",padx=5,pady=5)
btn_dictimp.bind("<Button-1>",dictionary_creation)

# Creating a button with binding to serialize a dictionary in Binary format. 
btn_dictbin = tk.Button(master=window,text="Serialize Dictionary to Binary")
btn_dictbin.grid(row=1,column=0,sticky ="nsew",padx=5,pady=5)
btn_dictbin.bind("<Button-1>",dict_to_binary)

# Creating a button with binding to serialize a dictionary in JSON format.
btn_dictjson = tk.Button(master=window, text="Serialize Dictionary to JSON")
btn_dictjson.grid(row=1,column=1,sticky = "nsew",padx=5,pady=5)
btn_dictjson.bind("<Button-1>",dict_to_json)

# Creating a button with binding to serialize a dictionary in XML format.
btn_dictxml = tk.Button(master=window, text="Serialize Dictionary to XML")
btn_dictxml.grid(row=1,column=2,sticky = "nsew",padx=5,pady=5)

# Creating a button with binding to generate an encryption key. 
btn_sendenc = tk.Button(master=window,text="Generate Encryption Key")
btn_sendenc.grid(row=2, column=0, sticky = "nsew",padx=5,pady=5)
btn_sendenc.bind("<Button-1>",write_key)

# Creating a button with binding to send a file encrypted to the server. 
btn_sendenc = tk.Button(master=window,text="Send File (Encrypted)")
btn_sendenc.grid(row=2, column=1, sticky = "nsew",padx=5,pady=5)
btn_sendenc.bind("<Button-1>",encrypted_send)

# Creating a button with binding to close server connection and the client window.
btn_closeclient = tk.Button(master=window,text="Close Client")
btn_closeclient.grid(row=2, column=2, sticky = "nsew",padx=5,pady=5)
btn_closeclient.bind("<Button-1>",close_client)

# Function calling to open the window. 
window.mainloop()