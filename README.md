# Reading txt app

This is a basic reading txt file called "CNAB.txt" and inserting at the database

![Alt Text]("C:\Users\USER\Desktop\TALITTA\READINGFILES\TELA INICIAL.png")


## Documentation

Clone this repo:
```
git clone https://github.com/talitta-nunes/reading-txt.git
```
Change directory into the project directory:
```
cd csvmodel
```
Create a virtual environment:
```
python -m venv venv
```
Activate the virtual environment:
```
Get-ExecutionPolicy
.\venv\Scripts\activate  
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Prepare migrations
```
python manage.py makemigrations
```
Migrate
```
python manage.py migrate
```
Run the server:
```
python manage.py runserver
```
And Boom! You're up and running!

Feel free to contribute towards this project!
