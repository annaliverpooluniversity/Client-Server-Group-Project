# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 17:40:51 2022

@author: Anna
"""

import socket

import os

import tkinter as tk
from tkinter import *
from tkinter import filedialog

from cryptography.fernet import Fernet 


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 65444

server_socket.bind((HOST,PORT))
print("Server Socket Created")

server_socket.listen(1)
  
while True:
    
    clientsocket,addr = server_socket.accept()    
    print("Client Connected")
   
       
    def close_window(event):
        clientsocket.close()
        server_socket.close()        
        window.destroy()
    
    def decrypt_file(event):
   
        keyfilename = filedialog.askopenfilename(
            initialdir ="C:/Users/Desktop/Server/",
            title = "Open File with Encryption Key",
            )
        keyfilesize = os.path.getsize(keyfilename)      
        key = open(keyfilename,'rb').read()
        f = Fernet(key)
     
        filename = filedialog.askopenfilename(
            initialdir ="C:/Users/Desktop/Server/",
            title = "Open File to Decrypt",
            )
        filesize = os.path.getsize(filename)   
                      
        with open(filename,"rb") as file:
           
            encrypted_data = file.read()
            
        
        decrypted_data = f.decrypt(encrypted_data)
        
        
        with open(filename, "wb") as file:
            file.write(decrypted_data)
           
    