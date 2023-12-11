# Reading txt app

This is a basic reading txt file called "CNAB.txt" and inserting at the database


![TELA INICIAL](https://github.com/talitta-nunes/reading-txt/assets/70520439/49f6ec0b-c81c-4464-85e3-5f450f08117d)

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
