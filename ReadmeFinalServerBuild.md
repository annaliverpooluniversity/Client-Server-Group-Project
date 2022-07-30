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
Server GUI Interface only opens after a succesful connection has been made from the client
------------------------------------------------------------------------------------------------------------------------------
- Watch out! The server GUI Window might open behind the Client GUI window. 
- The server GUI window has four buttons that help interact with data stored on the client. 

------------------------------------------------------------------------------------------------------------------------------
Print Contents to Screen
------------------------------------------------------------------------------------------------------------------------------
- Click this button to view contents of a file on screen.
- Once you click this button, a new window will open that allows you to select a file.
- The contents of this file will be displayed in the window. 

------------------------------------------------------------------------------------------------------------------------------
Print Contents to File
------------------------------------------------------------------------------------------------------------------------------
- Click this button to view contents of a file into a preset text file called 'Text Output File'.
- Once you click this button, a new window will open that allows you to select a file.
- The contents of this file will be appended to the 'Text Output File'.

------------------------------------------------------------------------------------------------------------------------------
Decrypt Text File
------------------------------------------------------------------------------------------------------------------------------
- This button allows the server to decrypt files. 
- Once you click the button, a dialog will open asking you to select the key file. 
- This should be the same file 'key.key' with which the file was encrypted by the client. 
- Once you have selected the key, another dialog opens that asks for the file to be decrypted. 
- Select the file to be decrypted and with the right key, the contents should be decrypted. 
- Use one of the other functions to view the content!

------------------------------------------------------------------------------------------------------------------------------
Close Server and Window
------------------------------------------------------------------------------------------------------------------------------
- This button closes the connection to the client, closes the server and also closes the server GUI Window.



 
