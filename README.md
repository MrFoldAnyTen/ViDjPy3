# ViDjPy3<br/ >
Virtualenv Python3 Django    https://pythonprogramming.net/django-web-server-publish-tutorial/<br/ >
<br/ >

git clone https://github.com/MrFoldAnyTen/ViDjPy3.git <br/ >
cd ViDjPy3/<br/ >
atom .<br/ >
virtualenv -p python3 ENV<br/ >
source ENV/bin/activate<br/ >
pip install django<br/ >
python --version<br/ >
python -m django --version<br/ >
pip install django<br/ >


mkdir tutorial<br/ >
cd tutorial/<br/ >

django-admin startproject mysite<br/ >
cd mysite/<br/ >
python manage.py startapp webapp<br/ >
python manage.py runserver<br/ >

http://127.0.0.1:8000/<br/ >


http://127.0.0.1:8000/webapp/hey/<br/ >

# Part 2<br/ >

## Jinja Templates <br/ >
