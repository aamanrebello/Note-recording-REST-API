PERSONAL NOTE TAKER API
----
**FUNCTIONALITY**
-

 Allows a user to register on the API's database with a user ID. Allows the user to save new personal notes, update (rewrite, append, prepend) them, list them out, delete them or transfer them to an "archive" file.

 Notes are stored in *text files*. Each user has his/her own folder in which his/her notes are stored.  All users' names and ID's are listed on a *.mdb* (Microsoft Access) database. All of these storage files/folders are stored in a parent folder called "Storage".


**ABOUT THE PROJECT**
-
 - The API is written in Python. It uses the *Flask* framework to create the API. 

 - It stores personal notes as *.txt* files. This is because *.txt* files are easier to manipulate and manage, and cheaper to store, than other data structures like databases. They can be compressed, archived, or put on *AWS* services like *S3* more easily. Python dictionaries etc. do not provide the same capability for storage.

 - User details (Name, User ID) and records of notes and archives are stored in a Microsoft Access *.mdb* database. . Microsoft Access is probably not the best choice of engine,  but it was chosen for ease of implementation. The engine can easily be changed by suitable modifications.

 - For posting, updating notes and creating new users, necessary data is sent from a client program via *json*.

 - Each functionality e.g. listing notes, saving new notes etc. is in a separate API in a separate *.py* file. The programs listen on different ports. This makes the application more conducive to scaling up and adding new functionality.
 
 - Below is an architectural overview of the API (note the data model used in the database):
                       ![image](https://user-images.githubusercontent.com/56508438/92012205-10954b00-ed44-11ea-8666-c239b13e1602.png)


 **FILES AND FOLDERS**
 -
 1. Python_API
    - *__init.py__*
    - *apitest.py* (used to test the post, update and create_user functionalities by passing JSON values)
    - *personalnotes_archive.py* (saves note to archives as GZIP, unzips note and returns to normal)
    - *personalnotes_user.py* (creates/deletes new user folders and records)
    - *personalnotes_delete.py* (deletes note files/archives)
    - *personalnotes_get.py* (lists all notes and archives for a user in JSON format)
    - *personalnotes_post.py* (saves new note for a user)
    - *personalnotes_update.py* (updates selected note - prepend, append or rewrite)
    - *modify_db.py* (Contains all SQL commands required by the application that modify the database through insertion/deletion.)
    - *common_functions.py* (contains functions called commonly by all the above files e.g. reading from *config.txt*, non-modifying database queries etc)
    - *config.txt* (contains important configuration information in JSON format)
    - *runall.bat* (Batch script that runs all programs simultaneously in Windows)
    - *runall* (Bash script that runs all programs simultaneously in Linux environment)
 2. Storage
    - *folder for each user's Notes*. Name is in format *<UserID>_notes*.
    - *API_Users.mdb* (database that records users, notes, archived notes and date of creation)
 3. README.md.


 **REQUIREMENTS**
 -
 1. Python 3.x (modules *pyodbc, os, shutil, flask* must be installed)
 2. Microsoft Access (Databases are stored in 2002 - 2003 format) - can be changed to another DB engine by modifying the *dbconfig* field in *config.txt*. The field basically provides information to set up a pyodbc connection to the database being used - see its usage in *common_functions.py* and *modify_db.py*. 


 **HOW TO USE**
 -
 1. Depending on where this folder is stored, the *base_path* field in the *config.txt* file must be changed to the absolute path of this folder. This is because Flask does not seem to recognise relative paths which means that the full path needs to be entered. The *base_path* field is used to prevent the need to enter absolute paths throughout the code. By default, this field is set to *C:Users/aaman/Documents/Note_Taker*.

 2. For each function, the corresponding program file needs to be run. I do so on the terminal window i.e. command prompt. The different programs (POST, GET etc) operate on different ports and can therefore be run simultaneously. Alternately, you can also run the batch script (*runall.bat*) on Windows or the bash script (*runall*) in a Linux environment. The latter has not been fully tested and may need tweaking.

 3. For *post, update and create_user* operations, a client program needs to be run in a separate terminal window. The *apitest.py* file in *Python_API* provides sample code to run in a client program. The code can be uncommented and run - as many operations as required.

 4. The other operations can be run on a web browser at the URL displayed on running the program. Each program file contains details of the exact URL to enter to run it.

 5. The *config.txt* file may also be used to change parameters related to the database connection.


 **POSSIBLE IMPROVEMENTS/ENHANCEMENTS**
 -
  1. To archive files, the file is moved to a folder called "Archives" that exists for every user. It is then compressed into *.gz* format. I am not sure whether this is how archiving should be done, and this is probably an area that needs to be looked into.
  
  2. Using a better DBMS than MS Access. Maybe something like MySQL?

  3. Alternately, the API can make use of cloud services like *Amazon S3* (for storage of files), *Amazon RDS* (for databases of details), *Amazon API Gateway* (for interfacing the API code). The code can be written on event driven services like *AWS lambda*. This would improve performance and scalability. Although I have mentioned the *AWS* options, other cloud services could be used as well.
