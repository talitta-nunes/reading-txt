# Reading TXT App

This is a basic reading txt file called "CNAB.txt" and inserting its content at the database

## Screenshots

**Initial Screen:**

![Initial Screen](https://github.com/talitta-nunes/reading-txt/blob/main/assets/screenshots/initial_screen.png)

**Success Screen:**

![Success Screen](https://github.com/talitta-nunes/reading-txt/blob/main/assets/screenshots/success_screen.png)

**Table:**

![table](https://github.com/talitta-nunes/reading-txt/assets/70520439/f9b23c10-aca6-4b60-9781-84a7c0163eb9)

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
