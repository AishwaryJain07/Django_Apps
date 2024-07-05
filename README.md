# Django_Apps


In This Project, I made two basic applicatations:

1: A new Year application that tells wether it is new year or not.

  What I used!
  
 - I used render function and Python Datetime library to check whether it is 1st of january, It displays "YES" or not, It displays "NO".

 - Simply uses return render(request) to fetch and Display the Results.


2: Task List.
-This Application allows you to add and delete Task you want.

  What I used!
  
 - I made html pages to add the tasks, Index.html and layout.html( this contains the basic layout that add.html and index.html inherits)

 - a static css files inherited to use the defined css in all the files.

 - **Implemented sessions** to create multiple sessions for multiple users.
   
 - **Added CSRF Authentication** for both Server Side and Client Side Verification.

How to use!

-> Make sure Django and Python are installed correctly on your System.

-> Clone this Repository on your Local System using "git clone https://github.com/AishwaryJain07/Django_Apps.git"

-> In the Bash (on windows) / Terminal (on Linux), Browse the folder containing this cloned Repository and Run "python manage.py runserver" to run the app .

-> In case you find issues in saving the Tasks, Try to run "python manage.py clearsessions" to r=delete the cached data.

-> Go on and Add your Tasks Happily and Achieve Them.
