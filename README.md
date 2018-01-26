Installation Instructions:

=======
Unix:
=======

1. Clone the respository: 

git clone https://github.com/kelseyblair/MusicLibrary.git
cd MusicLibrary

2. Check is python is installed

2. Set up virtual environment
2.1 Check if Python is installed
python --version

If it is and the version is 3 or greater:
python3 -m venv myvenv

Version 2 or less:
virtualenv myvenv

source myvenv/bin/activate
pip install --upgrade pip
pip install django
cd mainsite

3. Migrate
python manage.py migrate

4. runserver
python manage.py runserver

========
Windows:
========
