Dota App - Web Scraping Practice  
This project is a web scraping tool designed to gather and analyze data from Dota 2 statistics sources such as OpenDota. It uses Python to extract relevant data for further processing.

Features
Scraping Dota 2 stats: Collect data using OpenDota.  
Data processing: Using Django to store and updte scrapped data.  
Requirements
Python 3.x  
Requests: selenium, django, celery etc. (full list in requirements.txt)  

Usage
Clone the repo:
- git clone https://github.com/GawarWawar/dota_app.git
Install dependencies:
- pip install -r requirements.txt
Make django preparations:
- python manage.py createsuperuser  
- python manage.py migrate  
Run the Django instance, Celery worker and celery-beat instance:
- python manage.py runserver
- celery -A celery_instance worker -l info 
- celery -A celery_instance beat -l info 
Register Dota Profile in Admin at /admin/opendota_forcer/dotaprofile/ and scrapper will automatically press button to parse last match every half an hour.