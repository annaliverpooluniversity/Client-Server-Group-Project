"""
The following libraries have comments besides them that explains why they are imported.
"""

import socket  # Import library for building a TCP server-client

import os  # Import library to work with directories and files

# Import libraries to build GUI 
import tkinter as tk
from tkinter import *
from tkinter import filedialog

from cryptography.fernet import Fernet  # Import library for encryption and decryption of files.

import unittest  # Import library to run unit test for parts of the code.
from os.path import exists  # Import library to work with directories and files (Used in the unit test)

""" 
A socket with a defined host and port is created to make a connection with the client. The host is defined as the 
local host and the port is given a port number of 65444 so it is a private port. A function is then defined to connect 
the server socket to the host and port.
"""
# Creating a socket that will create a server and help connect to the client.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sockets needs a host and port to connect to the server.
# Here we define the host as the local host and a random port.
HOST = socket.gethostname()
PORT = 65444


def openre_server(event):
    # Creating a server with assigned Host and Port
    server_socket.bind((HOST, PORT))
    print("Server Socket Created")

    # Listening for connections. We limit the number of concurrent connections to 1.
    server_socket.listen(1)
    # Accepting a client connection to the server and confirming the same. 

    # declaring the connection to client as global to access in other functions.
    global clientsocket
    global addr

    clientsocket, addr = server_socket.accept()
    print("Client Connected")


def receive_files(event):
    # Should the client send a file, the server is ready to receive
    received = clientsocket.recv(4096).decode()

    # Server receives filename and filesize.
    filename, filesize = received.split("<SEPARATOR>")
    # Removing the path to the file and storing the name
    filename = os.path.basename(filename)

    # Storing file size, could be used for tracking trasnfer progress
    filesize = int(filesize)

    # Reading and writing the contects from the client into a file.
    with open(filename, "wb") as f:
        print("File opened")
        while True:
            bytes_read = clientsocket.recv(4096)
            if not bytes_read:
                break
            try:
                f.write(bytes_read)
            except Exception as e:  # e is the error message that could occur in the try block
                print(e)
    f.close()


# function to close the client connection, server and server GUI window.    
def close_window(event):
    clientsocket.close()
    server_socket.close()
    window.destroy()


# Function to decrypt an encrypted file.
def decrypt_file(event):
    # Opening a dialog box to enter the key for decryption.
    keyfilename = filedialog.askopenfilename(
        initialdir="C:/Users/Desktop/Server/",
        title="Open File with Encryption Key",
    )
    keyfilesize = os.path.getsize(keyfilename)
    key = open(keyfilename, 'rb').read()
    f = Fernet(key)

    # Opening a dialog box to select the file to be decrypted.
    filename = filedialog.askopenfilename(
        initialdir="C:/Users/Desktop/Server/",
        title="Open File to Decrypt",
    )
    filesize = os.path.getsize(filename)

    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()

    # Decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    # Write to the original file
    with open(filename, "wb") as file:
        try:
            file.write(decrypted_data)
        except Exception as e:  # e is the error message that could occur in the try block
            print(e)


# Define function to print contents of received file to 'Text Output File'             
def print_to_file(event):
    # Dialog to select the file that needs to be printed to the text output file.
    filename = filedialog.askopenfilename(
        initialdir="C:/Users/Desktop/Server/",
        title="Open File to Print to File",
    )
    filesize = os.path.getsize(filename)

    # Here the contents of the selected file are printed to the text output file.
    with open(filename, "r", encoding='utf-8') as infile:
        with open("TextOutPutFile.txt", 'a', encoding='utf-8') as outfile:
            for line in infile:
                try:
                    outfile.write(line)
                except Exception as e:  # e is the error message that could occur in the try block
                    print(e)


# Function to display the contents of the selected file to the screen                 
def print_to_screen(event):
    # A function to open a dialog to select a file and make the contents available
    def openFile():
        tf = filedialog.askopenfilename(
            initialdir="C:/Users/Desktop/Server/",
            title="Open file to display",
            filetypes=(("Text Files", "*.txt"),)
        )
        pathh.insert(END, tf)
        tf = open(tf, 'r', encoding='utf-8')
        data = tf.read()
        txtarea.insert(END, data)
        tf.close()

    # Open a window that will be used to dispay the contents of a selected file
    ws = tk.Tk()
    ws.title("File Contents")
    ws.geometry("650x650")
    ws['bg'] = 'black'

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


"""
The below section is unit tests to test smaller sections of a few parts of the code. Unit test needs to be run before 
the code is run to make sure there are no error in the important parts tested. Below are the tests with explanation:
 test1: the server starts up using exception handling since it is a crucial step to make sure the server starts. 
        To ensure that the test runs it had to have an external server; a separate server is created. This conflicts 
        with the original server. Therefore, to test whether the startup works, the original server would not work. 
        To use the original server, test1 will have to be changed into a comment to avoid this error. 
 test2: the decryption function decrypts the file. This is done by comparing the file with the data and the decrypted 
        data. Using the assertNotEqual, if the two are not the same therefore the encryption is not working, 
        otherwise it is.
 test3: the Output File exists as expected. AsserTrue is used to check whether the file is created or not.
"""


class UnitTesting(unittest.TestCase):

    def test1_server_startup(self):
        print("Testing server starts up...")
        try:
            test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            test_socket.bind((HOST, PORT))
            connection = True
        except Exception as e:  # e is the error message that could occur in the try block
            connection = False
        self.assertTrue(connection, "Server did not start up!")
        print("Server starts up test passed!")

    def test2_decryption(self):
        print("Testing if decryption works...")
        # Opening a dialog box to enter the key for decryption.        
        keyfilename = filedialog.askopenfilename(
            initialdir="C:/Users/Desktop/Server/",
            title="Open File with Encryption Key",
        )
        key = open(keyfilename, 'rb').read()
        f = Fernet(key)

        filename = "Encrypted_UnitTestData.csv"

        with open(filename, "rb") as file:
            # read the encrypted data
            file_data = file.read()

        # Decrypt data
        decrypted_data = f.decrypt(file_data)

        # Write to the original file
        with open(filename, "wb") as file:
            try:
                file.write(decrypted_data)
            except Exception as e:  # e is the error message that could occur in the try block
                print(e)
        self.assertNotEqual(file_data, decrypted_data, "Decryption not working!")
        print("Decryption test passed!")

    def test3_output_to_file(self):
        print("Testing if output file exists...")
        print_to_file('test')
        self.assertTrue(exists("TextOutPutFile.txt"), "Output file does not exist!")
        print("Output file test passed!")


if __name__ == '__main__':  # The main with the unittest refers back to the class that is in the top level.
    unittest.main()

# Opening the main server window that will be used as an interface
window = tk.Tk()
window.title("Server Interface")

# Server interface will have four buttons 
window.rowconfigure([0], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=50, weight=1)

# Creating a button with binding that prints the contents of a file to the screen
btn_opnser = tk.Button(master=window, text="Open Server")
btn_opnser.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
btn_opnser.bind("<Button-1>", openre_server)

# Creating a button with binding that prints the contents of a file to the screen
btn_recfile = tk.Button(master=window, text="Click to receive file")
btn_recfile.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
btn_recfile.bind("<Button-1>", receive_files)

# Creating a button with binding that prints the contents of a file to the screen
btn_scprnt = tk.Button(master=window, text="Print Contents to Screen")
btn_scprnt.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
btn_scprnt.bind("<Button-1>", print_to_screen)

# Creating a button with binding that prints the contents of a file to the text output file
btn_fprnt = tk.Button(master=window, text="Print Contents to File")
btn_fprnt.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
btn_fprnt.bind("<Button-1>", print_to_file)

# Creating a button with binding that decrypts a selected text file    
btn_decrypt = tk.Button(master=window, text="Decrypt Text File")
btn_decrypt.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)
btn_decrypt.bind("<Button-1>", decrypt_file)

# Creating a button with binding that closes the client connection, server and window       
btn_allcloser = tk.Button(master=window, text="Close Server and Window")
btn_allcloser.grid(row=0, column=5, sticky="nsew", padx=5, pady=5)
btn_allcloser.bind("<Button-1>", close_window)

# Opening up the main server window.
window.mainloop()
