**Student Management System**

This is a Django based application for managing student information.
It allows users to view, edit, and add student records into the system.

For more info about the project, please check out the Report.pdf file.

Here are the instructions on how to run this project locally on your computer.
<br><br>

First, clone this repositorty to your computer.

Instructions on how to clone a repository can be found <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">here.</a>
<br><br>

Here's a short and easy way to do it in VS Code: (This is how I do it)

* Make sure to have Git installed.

* Press Ctrl + Shift + P.

* Search for Git: Clone and hit enter.

* Paste the repository URL and press enter.

* Choose a suitable location and the repository will be cloned.

<br>

Once that's done, follow these steps:

* Create and activate the virtual environment.

<code>python -m venv venv</code> creates a virtual environment.

<code>.\venv\Scripts\activate</code> activates it.

* You can create a superuser to access the admin panel.

<code>python manage.py createsuperuser</code>

* Follow the prompts to set a username, email, and password.

* Run the server.

<code>python manage.py runserver</code>

* Open a web browser and go to:

<code>http://127.0.0.1:8000/</code> to access the application

<code>http://127.0.0.1:8000/admin/</code> to access the admin interface.

You're all set!
