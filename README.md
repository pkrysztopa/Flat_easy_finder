* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)

## General info
<details>
<summary>Click here to see general information about <b>Flat easy finder</b>!</summary>
<b>Flat easy finder</b> is an application designed to help you find a flat in a simple and easy way. 
Looking through the offers on the Internet can be very time-consuming, so we decided to create an application that will help you find the perfect flat for you. 
The application gives you the opportunity to search for a flat with flexible filters and sorting options without having to visit many websites.
That makes this application a great tool for people who are looking for a flat for themselves, as well as for people who are looking for investment opportunities.
</details>

## Technologies
<ul>
<li>Python 3.11</li>
<li>sqlite3</li>
<li>Selenium</li>
<li>BeautifulSoup</li>
<li>Flask</li>
</ul>

## Setup
Clone the repo
```git clone https://github.com/pkrysztopa/Flat_easy_finder```
Download chromedriver from https://chromedriver.chromium.org/downloads and put it in the main folder.
Install all dependencies
```pip install sqlite3``` ```pip install selenium``` ```pip install BeautifulSoup``` ```pip install Flask```
Run the application
```python run.py```
Open your browser and go http://127.0.0.1:5000 or http://192.168.0.66:5000
Under the "Zgraj dane" text is a field where you can put a number of webpages which you want to scrap (one page has about 72 apartment announcements).
After this you can browse the data and use filters to collect the data you want.

## More detailed information about modules
<details>
<summary>Click here to see detailed information about <b>Flat easy finder</b>!</summary>
The core of the application is webscraping functionality localized in <b>src/trackig</b> module, which is responsible for collecting data from services such as otodom.pl, morizon.pl, gratka.pl, domiporta.pl and olx.pl.
<b>WebCrawler</b> object is responsible for connecting and going through the websites and collecting links to offers. 
<b>WebScraper</b> object then goes through the gathered links, collects data from them and saves them in a <b>Flat</b> object. 
Gathered data is then organized, transformed and unified, by <b>Transformer</b> object.
Transformed data is then saved in the database by <b>DBHandler</b> object. This module is also responsible for reading data from the database and sending it to the user.
All these objects are connected by <b>FlatEasyFinder</b> object, which is responsible for the flow of the application.
Gathered data is then presented to the user by module <b>ui</b>, which is responsible for the graphical interface of the application.
Tables are generated, by HtmlGenerator object, which is responsible for generating html code for tables.
</details>

## Application view
<img src = "[(https://github.com/pkrysztopa/Flat_easy_finder/assets/99322740/728cc34b-d823-4c47-909b-f8893e4cba64)](https://private-user-images.githubusercontent.com/99322740/237950858-728cc34b-d823-4c47-909b-f8893e4cba64.JPG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZXkxIiwiZXhwIjoxNjgzODg5MTQ4LCJuYmYiOjE2ODM4ODg4NDgsInBhdGgiOiIvOTkzMjI3NDAvMjM3OTUwODU4LTcyOGNjMzRiLWQ4MjMtNGM0Ny05MDliLWY4ODkzZTRjYmE2NC5KUEc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDUxMlQxMDU0MDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00YjE2MzEyZWZjNDQwOTE2MmYxMDU0N2VhOTc3YTQ3YjUwNTk2ZWNmZDJkYjNlMGRjYTA1ZGRhMmE3ZmFhZjlkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.3gqBasaIuKi-4gXWQADImVrQJ_-M6JS9Gm5t6OVzCBI)"></img>
