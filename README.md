
# NAYAN (I. SEE. YOU.)

Nayan detects head movement and iris for preventing cheating in online exams conducted remotely.

# Login-Page-using-Python-and-MySQL
It's a GUI project using python tkinter and MySQL database.

Make sure you already have installed all the modules used in this project. Please see the requirement.txt file for all the requirements.


Steps to follow after installing all the modules. Otherwise this application will not work properly.

->Create a database with this name, "student_database"
->create a table with this name, "student_register"


USE this code to create the table under the "student_database" database

create table student_register(
   f_name VARCHAR(50) NOT NULL,
   l_name VARCHAR(50) NOT NULL,
   email VARCHAR(100) NOT NULL,
   question VARCHAR(50) NOT NULL,
   answer VARCHAR(100) NOT NULL,
   password VARCHAR(50) NOT NULL,
   PRIMARY KEY ( email )
);

# SignUp-Page-using-Python-and-MySQL

Make sure you already created a database with name, 

"student_database" and along with that a table with name, "student_register"

must be made in order to have all the new enteries registered in the database

# Head-Movement-Detection

This project can perform head movement detection in Python using OpenCV.

[Running these codes requires Python and OpenCV]

head_2.py : Code that performs head-movement-detection using the real time video from a camera [Python + OpenCV] 

It detects and displays warnings on whether cheating detected or not 

# Iris-Detection

This project can perform iris detection in Python using OpenCV.

[Running these codes requires Python and OpenCV]

iris.py : Code that performs iris-detection using the real time video from a camera [Python + OpenCV]




# Download

Install NAYAN with the help of an executable file (.exe)

-> The dist folder contains login_page.exe file
-> Downloading that on system would allow you to run the file 


    
## Roadmap

- On downloading the login_page.exe file, we have to register using our email id and password.

- If not a registered user then registeration is to be done by signup page by adding your first name, last name, email id, security question and setting of a password.

- On registeration, login is to be done by entering credentials.

- Credentials are then cross-checked by the database

- Once cross-checked camera window appears and it detects the head movent and iris

- On detection it displays message whether "cheating detected" or not


## Screenshots

![image](https://user-images.githubusercontent.com/80629008/231268340-50abf72f-2758-4cbc-9db5-827421099b37.png)

![image](https://user-images.githubusercontent.com/80629008/231268867-e84a8890-c573-4273-8eb4-f3922557b7f3.png)


## Authors

- [@adeptarachnerd](https://github.com/adeptarachnerd)
- [@muskan0251gupta](https://github.com/muskan0251gupta)
- [@Rishita17Shahi](https://github.com/Rishita17Shahi)
- [@prakshi2802](https://github.com/prakshi2802)


