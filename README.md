# Reading TXT App

This is a basic reading txt file called "CNAB.txt" and inserting its content at the database

## Screenshots

**Initial Screen:**

![TELA INICIAL](https://github.com/talitta-nunes/reading-txt/assets/70520439/81dd6e64-0ae5-42a8-8ebb-fb3d9537fcbf)


**Success Screen:**

![tela de sucesso](https://github.com/talitta-nunes/reading-txt/assets/70520439/7a164f5d-e36e-4a16-bc44-7045980f2e1d)


**Table:**

![table](https://github.com/talitta-nunes/reading-txt/assets/70520439/f9b23c10-aca6-4b60-9781-84a7c0163eb9)

**Looking for the /vision url:**

![image](https://github.com/talitta-nunes/reading-txt/assets/70520439/1237e5e8-dc4a-49bf-bae5-7600724df455)

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
