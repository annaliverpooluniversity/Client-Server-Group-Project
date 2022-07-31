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
# Import library to serialize to XML 
from dicttoxml import dicttoxml
# Import library to write xml serialized data to xml file
from xml.dom.minidom import parseString
import unittest


# Initializing dictionary names


# Creating a socket that will connect to the server.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Sockets needs a host and port to connect to the server.
# Here we define the host as the local host and a random port.
HOST = socket.gethostname()
PORT = 65444


# Define a function that will connect to the server. 
def connect_to_server(event):
    try:
        client_socket.connect((HOST,PORT))
        return True
    except:
        return False
    

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
    f=open(filename,'rb')
    l=f.read(4096)
    while(l):
        client_socket.sendall(l)
        l=f.read(4096)
    f.close()
    client_socket.close()
# Finally, we use the client connection to the server to send the file. 
            

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
       filetypes=(("Text Files", "*.csv"),)
       )

#assign dict_from_csv as a global variable to make available in other functions
   global dict_from_csv
# Here we are transfer the contents of the CSV file into a Python dictionary.   
   with open(tf,'r') as inputfile:   
        reader = csv.reader(inputfile)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}
       

# Function to serialize dictionary with Binary format.
# We write this dictionary into a local client 'write_file'
def dict_to_binary(event):
    with open ("data_file_as_Binary.txt","wb") as write_file:
        pickle.dump(dict_from_csv,write_file)

#    with open ("data_file_as_Binary.txt","rb") as read_file:
#        print(pickle.load(read_file))
        

# Function to serialize dictionary with JSON format.
# We write this dictionary into a local client 'write_file'
   
def dict_to_json(event):
    
#    print(dict_from_csv)
    
    with open("data_file_json.json","w") as write_file:
        json.dump(dict_from_csv,write_file)

# Functions to serialize dictionary to XML format
def dict_to_xml(event):
    xml_data = dicttoxml(dict_from_csv)
    xml_decode = xml_data.decode()
    
    with open("data_file_xml.xml", "w") as write_file: #creating a file with xml extension that can be written
        write_file.write(xml_decode)
        

class UnitTesting(unittest.TestCase):
    
    def test1_connection(self):
        print("Testing if connection works...")
        connection = connect_to_server('test')
        self.assertTrue(connection, "There is no connection!")
        print("Connection test passed!")
        
    def test2_encryption(self):
        print("Testing if encryption works...")
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
            self.assertNotEqual(file_data, encrypted_data, "Encryption not working!")
        print("Encryption test passed!")
        
    
    def test3_json_serialization(self):
        print("Testing if json serialization works...")
        with open("UnitTestData.csv",'r') as inputfile:   
             reader = csv.reader(inputfile)
             dict_from_csv = {rows[0]:rows[1] for rows in reader}
             known_outcome = '''{
                 "\u00ef\u00bb\u00bfOrder ID\": \"Customer Name\",
                 "CA-2016-152156\": \"Claire Gute\",
                 "US-2015-108966\": \"Sean O'Donnell\",
                 "CA-2016-138688\": \"Darrin Van Huff\"
             }'''
             self.assertEqual(json.loads(known_outcome), json.loads(json.dumps(dict_from_csv, indent=4)))
        print("json serialization test passed!")


    def test4_xml_serialization(self):
        print("Testing if XML serialization works...")
        with open("UnitTestData.csv",'r') as inputfile:   
             reader = csv.reader(inputfile)
             dict_from_csv = {rows[0]:rows[1] for rows in reader}
             xml_data = dicttoxml(dict_from_csv)
             xml_decode = xml_data.decode()
             known_outcome = '<?xml version="1.0" encoding="UTF-8" ?><root><key name="Order ID" type="str">Customer Name</key><CA-2016-152156 type="str">Claire Gute</CA-2016-152156><US-2015-108966 type="str">Sean O&apos;Donnell</US-2015-108966><CA-2016-138688 type="str">Darrin Van Huff</CA-2016-138688></root>' 
             self.assertEqual(known_outcome, xml_decode.encode('ascii', 'ignore').decode())
        print("XML serialization test passed!")
        
        
    def test5_binary_serialization(self):
        print("Testing if binary serialization works...")
        with open("UnitTestData.csv",'r') as inputfile:   
             reader = csv.reader(inputfile)
             dict_from_csv = {rows[0]:rows[1] for rows in reader}
             known_outcome = b"\x80\x04\x95\x8a\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x0e\xc3\xaf\xc2\xbb\xc2\xbfOrder ID\x94\x8c\rCustomer Name\x94\x8c\x0eCA-2016-152156\x94\x8c\x0bClaire Gute\x94\x8c\x0eUS-2015-108966\x94\x8c\x0eSean O'Donnell\x94\x8c\x0eCA-2016-138688\x94\x8c\x0fDarrin Van Huff\x94u."
             self.assertEqual(known_outcome, pickle.dumps(dict_from_csv))
        print("binary serialization test passed!")
        
    def test6_connection_closing(self):
        print("Testing if connection closes...")
        try:
            client_socket.close()
            connection = True
        except:
            connection = False
        self.assertTrue(connection, "The connection closing did not work!")
        print("Connection closing test passed!")


if __name__ == '__main__':
    unittest.main()



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
btn_dictxml.bind("<Button-1>",dict_to_xml)

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
