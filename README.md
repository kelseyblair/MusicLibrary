#Installation Instructions:


##Unix:


1. Clone the respository: 
```
git clone https://github.com/kelseyblair/MusicLibrary.git

cd MusicLibrary
```

2. Set up virtual environment

* Check if Python is installed

```
python --version
```

* If it is and the version is 3 or greater:
```
python3 -m venv myvenv
```

* Version 2 or less:
```
virtualenv myvenv
```

```
source myvenv/bin/activate

pip install --upgrade pip

pip install django

cd mainsite
```

3. Migrate
```
python manage.py migrate
```

4. Run local server and go to the website
```
python manage.py runserver
```
* In your web broswer, navigate to 127.0.0.1:8000

##Windows:

