* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)

## General info
<details>
<summary>Click here to see general information about <b>Flat easy finder</b>!</summary>
<b>Flat easy finder</b> is an application designed to search for a flat in a simple and easy way. 
Looking through the offers on the Internet can be very time-consuming, so intention of this application is to speed up this process, and to give tools for data collection and data analysis. The application gives user the opportunity to search for a flat with flexible filters and sorting options without having to visit many websites.
That makes this application a good tool for people who are looking for a flat for themselves, as well as for people who are looking for investment opportunities.
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
<li>Clone the repo
```git clone https://github.com/pkrysztopa/Flat_easy_finder```</li>
<li>Download chromedriver from https://chromedriver.chromium.org/downloads and put it in the main folder.</li>
<li>Install all dependencies
```pip install sqlite3``` ```pip install selenium``` ```pip install BeautifulSoup``` ```pip install Flask```</li>
<li>Run the application
```python run.py```</li>
<li>Open your browser and go http://127.0.0.1:5000 or http://192.168.0.66:5000</li>
<li>Under the "Zgraj dane" text is a field where you can put a number of webpages which you want to scrap (one page has about 72 apartment announcements).</li>
<li>After this you can browse the data and use filters to collect the data you want.</li>

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
 
<img src = "https://github.com/pkrysztopa/Flat_easy_finder/issues/9#issue-1707415177"></img>
</details>

## Application view
<img src = "https://private-user-images.githubusercontent.com/99322740/237950858-728cc34b-d823-4c47-909b-f8893e4cba64.JPG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZXkxIiwiZXhwIjoxNjgzODg5MjA2LCJuYmYiOjE2ODM4ODg5MDYsInBhdGgiOiIvOTkzMjI3NDAvMjM3OTUwODU4LTcyOGNjMzRiLWQ4MjMtNGM0Ny05MDliLWY4ODkzZTRjYmE2NC5KUEc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDUxMlQxMDU1MDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zN2JhMTg0MmUxNzY3ZTg2ODkwZDRhMTY5MTk5MmY5NTZhMmZiNGZjMzI2MTllYjczODNhOTlmOWYyNzgwOGZjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.d92DD5cIsI5QEw0BHIe1utb4SnUKKSCz34RI7Uy41mM"></img>

## Contact
email: pkrysztopa@gmail.com
linkedin: https://www.linkedin.com/in/piotr-krysztopa-73bb2aaa/
