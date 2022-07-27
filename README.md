#Readme Client (for Readme Server see below) 
------------------------------------------------------------------------------------------------------------------------------
Readme file for the Group Project
------------------------------------------------------------------------------------------------------------------------------
- Store 'FinalServerBuild.py' and 'FinalClientBuild.py' in separate folders. This will mimic the client and server being on two separate machines. 
- Start by calling 'python FinalServerBuild.py' from terminal/command prompt.
- The terminal should print "Server Socket Created"; confirming that the server is created and listening for the client connection. 
- From a separate terminal/command prompt call 'python FinalClientBuild.py'. This should open up a GUI Window called 'Client Interface' with nine buttons. 
- Click on connect to server. 
- The server terminal/command prompt should print "Client Connected" once there is a succesful connection between the client and the server. 
- Unfortunately, at the moment, files can be sent only once. After which both, the client and the server need to be restarted. 

------------------------------------------------------------------------------------------------------------------------------
Send file (unencrypted)
------------------------------------------------------------------------------------------------------------------------------
- click on the button - 'Send File (Unencrypted)'
- Dialog box opens up; select the file that you want to transfer from Client to Server without encryption.
- Once you select the file and the server successfully receives it, another GUI Window opens up called 'Server Interface' with four buttons. 

------------------------------------------------------------------------------------------------------------------------------
Import CSV file to create dictionary
------------------------------------------------------------------------------------------------------------------------------
-  Click on the 'Import CSV file to create dictionary'
- Select a CSV file. Best to use the attached Sales.csv data.
- This dictionary is not stored in Python and the next three buttons can be used to serialize this dictionary. 

------------------------------------------------------------------------------------------------------------------------------
Serialize Dictrionary to Binary
------------------------------------------------------------------------------------------------------------------------------
- Click on the button 'Serialize Dictionary to Binary'
- This button takes the dictionary and serializes it and stores it in a local file called 'data_file_as_Binary.txt'

------------------------------------------------------------------------------------------------------------------------------
Serialize Dictrionary to JSON
------------------------------------------------------------------------------------------------------------------------------
- Click on the button 'Serialize Dictionary to JSON'
- This button takes the dictionary and serializes it and stores it in a local file called 'data_file_json.json'

------------------------------------------------------------------------------------------------------------------------------
Serialize Dictrionary to XML
------------------------------------------------------------------------------------------------------------------------------

- Click on the button 'Serialize Dictionary to XML'
- This button takes the dictionary and serializes it and stores it in a local file called 'XXXXXXXXX'

------------------------------------------------------------------------------------------------------------------------------
Generate Encryption Key
------------------------------------------------------------------------------------------------------------------------------
- This button generates a key in 'key.key'. 
- This is used to encrypt files that can be sent over the server.
- Please remember to not click this repeatedly as it can permanently overwrite the original key and any files encrypted will remain so forever.

------------------------------------------------------------------------------------------------------------------------------
Send File (Encrypted)
------------------------------------------------------------------------------------------------------------------------------
- This button opens a dialog that allows the user to select the file that is then encrypted and sent to the server. 

------------------------------------------------------------------------------------------------------------------------------
Close Client
------------------------------------------------------------------------------------------------------------------------------
- Clicking this button will close the connection to the server.
- This will also close the client GUI window. 





