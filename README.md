# TwitterTopLinksApp
### Assignment for Software Engineer at Vouch Insurtech


### Prerequisites

 - Django v3.1.1
 - HTML,CSS,JavaScript
 - A Twitter Account
 - Tweepy API
 - pip Packages


Heyy! the website is hosted on **pythonanywhere** .
So you can easily access [here](http://jay0208.pythonanywhere.com/).


## Technology Stack

### Frontend
-   HTML5
-   CSS3
-   Javascript
### Backend
- Django
- Tweepy
### Database
- SQLite3

## Why Django

- **Django** is an open-source python web framework **used** for rapid development, pragmatic, maintainable, clean design, and secure websites. 
- The main goal of the **Django** framework is to allow developers to focus on components of the application that are new instead of spending time on already developed components

## Why Sqlite 
- **SQLite** strives to provide local data storage for individual applications and devices.
-  **SQLite** emphasizes economy, efficiency, reliability, independence, and simplicity.

## Folder Structure

![](https://i.ibb.co/6ymyBDH/folderarrangement.jpg)


## Approach

- First, when the landing page of the website renders, the user can easily login with use of **Login with Twitter** Button
 >![](https://i.ibb.co/dgQ0wry/frontpage.jpg)

- Now, The user is redirected to Twitter to complete the authentication

- After Completing the authorization , The user lands to the main page. On the main page a user can see two tables at the top . one for the **Users who shared the highest number of URLs** with the URL count and one for the **Top URLs being shared** with the count of how many times they got shared  
>![-](https://i.ibb.co/PchHsFh/mainpagestart.jpg)
- Followed by the tables user can see all the Tweets from last 7 days which are from User's Stream.
>
![-](https://i.ibb.co/6bmhVfS/stream.jpg)
- On the top left corner , user can see a **Sign Off** button on main page which redirects user to a main page.

- If by some means or bad luck user get some error user will be direct to **Error 404**  Page . On which there will be a button which will direct user to home page
 >![enter image description here](https://i.ibb.co/CvPWmBy/error404.jpg)

### Database Schema
![](https://i.ibb.co/H4NNyD2/database.jpg)

## Packages to be installed
```
Django==3.1.1
requests==2.24.0
tweepy==3.9.0
```
## Installation for Local-Systems
1.  Create a folder 'Vouch' in your home directory  by `mkdir Vouch`
2.  Copy the content of the zip to the folder.
3.  Enter the folder:  `cd Vouch`
4. Open `views.py` enter the `consumer_key` and `consumer_secret_key` on top two lines  and save it .
5.  Install the required packages by :  `pip install "package-name"` or by `pip install -r requirements.txt`
6.  Start application by :  `python manage.py runserver`
7.  Visit http://127.0.0.1:8000/ to run the application.


## Contact

- -  Name : Jayash Batra
- -   Email:  [jayashbatra@gmail.com](mailto:jayashbatra@gmail.com)

