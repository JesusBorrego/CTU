# swe481g2
Group Project Pandas Pizza


With these instructions, type commands indicated by italics and then hit enter. These instructions assume the user has git installed on their system.

# OSX Instructions:

1. **Install Python 3** if you haven't already. If you don't have it installed, please download the version for your machine here: https://www.python.org/downloads/

2. **Go to the directory on your machine where you want to install the project.** Let's assume that the project will be installed in a folder called Projects in the user's (ctustudent) home directory. (/Users/ctustudent/Projects/SWE)

  Open the terminal app and run this command (search using spotlight, the magnifying glass in the top right if necessary)

 *cd /Users/ctustudent/Projects/*

3. **Clone the github repository**

  *git clone https://github.com/thesalientone/swe481g2.git*

  Note that it may ask you to enter your name and password. Enter them when prompted and press enter. You may not see your password being typed, but the computer is registering your strokes.

4. **Create a virtual environment**

  There should be a folder created when the git repository was cloned. If the name of that folder is swe481g2, then enter

  *python3 -m venv local_virtual*

5. **Activate the virtual environment**

  *source ./local_virtual/bin/activate*

  You should now see (local_virtual) before your prompt such as

  (local_virtual) ctustudent@localhost $

  This activates a contained python environment for the project that is separate from the python on your computer.

6. **Install Packages**

  *pip install -r swe481g2/requirements.txt*

  This will install all the necessary files for the project.

7. **Start Webserver**

  *python3 swe481g2/swe481g2_django/manage.py runserver*

  You should now be able to see the web application if you follow the link in the terminal!






# Startup Commands
* virtualenv env
* pip install django
* pip install Pillow
* django-admin startproject swe481g2_django
* cd swe481g2_django
* python3 manage.py startapp customer
* python3 manage.py startapp restaurant
* python3 manage.py migrate
* python3 manage.py createsuperuser

## Super user account details:

username = ctu

password = ctuonline
