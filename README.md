# Smitty's Bar & Restaurant

Bootstrapped using the Restaurantly website template available from <https://bootstrapmade.com/restaurantly-restaurant-template/>

Edited in the Cross Platform Cloud IDE Codeanywhere <https://app.codeanywhere.com/>

![Screenshot](static/assets/img/smittys-logo.jpg "Smitty Logo")

---------------

## Table of contents

1. The basics of Smitty’s<br/>
    1.1 Brief introduction<br/>
    1.2 Basic mechanics<br/>
    1.3 Link to website<br/>
2. Planning<br/>
    2.1 Ideas and UX Design<br/>
    2.2 User Stories<br/>
3. Layout<br/>
    3.1 Page Layout <br/>
    3.2 Excel file<br/>
    3.3 Intractability<br/>
4. Important code functions<br/>
    4.1 Python functions<br/>
    4.2 Python start code<br/>
5. Testing<br/>
Responsiveness testing
Browser compatibility
Bugs resolved and unresolved
Lighthouse testing outcomes
Code validation
    5.1 Manual testing<br/>
    5.2 Other tests<br/>
6. Issues & Bugs<br/>
    6.1 Resolved issues<br/>
    6.2 Unresolved issues<br/>
    6.3 Possible future developments<br/>
7. Deployment<br/>
    7.1 Heroku deployment<br/>
    7.2 ElephantSQL creation<br/>
    7.3 Database creation<br/>
8. Credits<br/>
    8.1 Credits<br/>
    8.2 References<br/>
    8.3 Thanks<br/>

-------------

## 1. The basics of Smitty's

#### 1.1 Brief introduction

The Smitty’s Bar & Restaurant website is a website for a fictitious bar that contains a login system and a booking system to store reservations. I designed the pub layout myself. User can sign up, log in, book a table and look around at all that this pub has to offer.

#### 1.2 Basic mechanics

The website was created using the following:

- [Bootstrap framework Restaurantly](https://bootstrapmade.com/restaurantly-restaurant-template/) for the framework of the website
- [Django Python framework](https://www.djangoproject.com) as the progaming language
- [ElephantSQL](https://www.elephantsql.com/) for the connection to the database
- [Heroku](https://www.heroku.com) or the deployment of the website

#### 1.3 Link to the website

The website can be found [here](https://smittys-bd7d75f32e46.herokuapp.com/)

----------------

## 2. Planning

#### 2.1 Ideas and UX Design

**Ideas**

The thought process started with the suggestion of creating a booking system. I have experience of pub culture and so by being able to translate this idea into something I could relate to made the experience a lot more interesting, although maybe the attention to the visuals ended up being a lot greater than was needed. More attention to the functionality would’ve made this project a lot more enjoyable as I was progressing through.
Also with the bootstrap website being so advanced it actually made the process a lot harder. The more a customised, the more it created errors and bugs.

**UX Design**



#### 2.2 User Stories

**Programmer**

- As a **programmer** I can **create a colour pattern and favicon for the website** to **make it pleasant for users**
- As a **programmer** I can **provide layout details and information to the user** to **help them make a choice and entice them to book a table**
- As a **programmer** I can **create a secure log in to the system** to **provide security of the details of the user**
- As a **programmer** I can **create a useful database** to **store information and provide it easily on the bookings of tables**

**Admin**

- As an **admin** I can **edit and check information** to **help with bookings and meet user demands**

User Stories not chosen:

- As a **user** I can **create an avatar** to **make my profile more fun**
- As a **user** I can **book multiple tables** to **make sure I can fit all my friends in**
- As a **user** I can **use the pub layout map to choose the table I want to sit at**so that I can **easily see what table suits my choice for my chosen time**

User Stories not closed:

- As a **programmer** I can **create a mailing system** to **keep the user/owners update with bookings and any changes/cancellations**
- As a **programmer** I can **create sufficient checks** to **enable the website to run without errors**
- As a **programmer** I can **create an upcoming events page** so that I can **inform the user of what future events are happening at the pub**

## Include

- Layout and Navigation
- Programs and tools
- Bugs, missing parts and issues
- My feedback
- Links, references and credits

The initial aim of this website was to provide a website to a fictional bar that included log/sign in/out functions and could utilise the inbuilt admin tool of Django and the database functions of PostgreSQL.

This is a website and so the only thing needed would be to sign up and log in.

### Layout and Navigation

The website has 4 navigational pages:

| 'html' Page Name         |          Accessed how?          |
| ------------------------ | :-----------------------------: |
| 'index' Home             | Loading homepage, 'logging out' |
| 'login' Login            |   Clicking on 'log in' button   |
| 'signup' Sign Up         |  Clicking on 'sign up' button   |
| 'booktable' Book-a-table | Clicking on 'Book table' button |

#### The html pages

##### Homepage start up screen

This is the first screen upon opening the website. The homepage can also be accessed at any time by clicking on "SMITTY'S BAR & RESTAURANT" located to the left of the the links. It can be scrolled down and also has working links found across the top of the header.

These links are:

- SMITTY'S
- Home
- How to book
- Menu
- Drinks
- Events
- Gallery
- Contact
- Register/Login (When not logged in)
- Book a table/Logout (When logged in)

##### Home "hero section"

The navbar appears on all pages.

The logo can be clicked on to return to the homepage:

![Screenshot](static/assets/img/README/nav_logo.jpg "Main page hero logo")

This part of the webpage shows two buttons that change depending on whether the user is logged in or not.

This is the page in its default position. Before logging in, the user can either choose to log in or sign up:

![Screenshot](static/assets/img/README/homepage_start.jpg "Main page hero when not logged in")

And this is the page after logging in, the user can now access the "Book a Table" page or choose to log out:

![Screenshot](static/assets/img/README/homepage_start_inlogged.jpg "Main page hero when logged in")

##### Links on main page

The navbar links can be clicked on to jump straight to the sections or the user can just scroll downwards

How to Book:
![Screenshot](static/assets/img/README/howtobook_navbar.jpg "How to book section of main page")

Menu:
![Screenshot](static/assets/img/README/menu_navbar.jpg "Menu section of the main page")

Drinks:
![Screenshot](static/assets/img/README/drinks_navbar.jpg "Drinks section of the main page")

Events:
![Screenshot](static/assets/img/README/events_navbar.jpg "Events section of the main page")

Gallery:
![Screenshot](static/assets/img/README/gallery_navbar.jpg "Gallery section of the main page")

Contact Us:
![Screenshot](static/assets/img/README/index8.jpg "Contact section of the main page")

**Footer section**

Footer:
![Screenshot](static/assets/img/README/homepage_footer.jpg "Footer section of the main page")

#### Other html pages

##### Sign in page

This page is accessed through the "Sign Up" button and then the aim was that upon entering the nesessary details, the user would have their details registered to the admin part of django and then the user would be logged in(see bugs):
![Screenshot](static/assets/img/README/signup.jpg "Sign in")

##### Log in page

The aim here was that this should have been accessed through the "Log In" button and then entering a previously registered email address and password, the user would be logged in(see bugs):
![Screenshot](static/assets/img/README/login1.jpg "Log in")

---

## Programs and tools

#### Programs

The following have been used during this website:

- Django
- Python
- JavaScript (Bootstrap only)
- HTML
- CSS

What should have also been used but wasn't (see problems):

- PSQL

#### Tools

The following have been used during this website:

- Bootstrap

#### Log in profiles and profiles used during production

Superuser:
username: admin
email: admin@email.com
Password: admin

Email Smittys Bar:
email: testemailsmittysbar@gmail.com
password: SmittysBar:2023

Test User:
dave@daveemail.com / Dave / Davis / Thursday:2023

---

## Bugs, missing parts and issues

There are sadly many bugs, issues and missing parts to this website.

#### Bugs

- Upon entering login email and password, the html pages doesn't log the user in.
- Upon entering signing in email and password, there is an error code
- Message function is created and the code is added to the 'base.html' file but it does not load.

- Models in booking and user apps are incorrectly titled as Reservations and Users, instead of Reservation and User

#### Missing Parts

There are many missing parts to the website:

- PSQL database function not created
- PSQL database tables not created
- Table booking function on 'booktable.html' not created
- The Contact US form is not connected

#### Issues

- The style.css file contains code that is not used and maybe even isn't connected.
- There are styling inconsistencies on the 'login.html' page

- drinks section of index. links not rotatable

#### Problems

- [Crispy](https://github.com/Dandresfsoto/crispy-forms-materialize/issues/13>)
https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html
Temporarily removed Crispy

- Origin checking failed - does not match any trusted origins
[Add "CSRF_TRUSTED_ORIGINS =" to settings](https://stackoverflow.com/questions/38841109/csrf-validation-does-not-work-on-django-using-https)
Changed to workspace link, then it should be changed to deloyed link address

---

## My feedback

#### My feedback

I can diplomatically say that this has been a challenge. I have learnt so much from the negative parts I've experienced during this project, to an almost life-changing level.
This project needed a simpler base bootstrap template, less time on the stylings and more time on the functionalities.

---

## Links, references and credits

#### Links and references

- \*Bootstrap template:
  Template Name: Restaurantly
  Template URL: <https://bootstrapmade.com/restaurantly-restaurant-template/>
  Link: <https://github.com/technext/restaurantly/releases/download/v1.0/Restaurantly.zip>
  Author: BootstrapMade.com
  License: <https://bootstrapmade.com/license/>

- Help installing allauth:
  Code with Stein <https://www.google.com/search?sca_esv=567555228&rlz=1C1CHBD_svSE1043SE1044&q=linking+django+allauth&tbm=vid&source=lnms&sa=X&ved=2ahUKEwjFjeKh9b2BAxUbRvEDHSdhA7MQ0pQJegQIChAB&biw=1536&bih=735&dpr=1.25#fpstate=ive&vld=cid:54078088>

- Pictures:
  Pixabay <https://pixabay.com/>

- Help with authentication upon login:
  djangoproject.com <https://docs.djangoproject.com/en/4.2/topics/auth/default/#auth-web-requests>

- Help with postgresql connection:
  Profile: "Pretty Printed" <https://www.youtube.com/watch?v=t6RbanOhna4>

- Youtube online guides and tutorials: Codemy.com

#### Credits

Mentor: Akshat Garg
Fiverr debugger: Haris (coodingmentore)

[connecting heroku and django](https://www.youtube.com/watch?v=UkokhawLKDU)
import django_heroku
from decouple import config
installed pipreqs to only use reqs that are necessary
installed piptools to combine

[adding datetimepicker] (https://pypi.org/project/django-bootstrap-datepicker-plus)
added datepicker using pip install django-bootstrap-datepicker-plus
install pip install django-bootstrap-v5
[adding datetimepicker usage](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Usage.html#model-form-usage)
installed pip install django-crispy-forms to run datetimepicker

models.py [datetime](https://stackoverflow.com/questions/2029295/django-datefield-default-options)
installing db in postgresql using Code Institute module [Database Management Systems](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DB101+2021_T1/courseware/c0c31790fcf540539fd2bd3678b12406/87ffa16374c74c55b202724586a834c9/?child=last)
issues with migrations - Tutor Assistance (Holly) - migrations deleted and elephantsql database reset, then migrations rerun date 220124
NEW SUPERUSER: admin/admin
Test users: Alan/Alans/alan@gmail.com/Alan:2024
