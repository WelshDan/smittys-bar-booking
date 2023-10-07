![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **May 11th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.




![Screenshot](static/assets/img/smittys-logo.jpg "Smitty Logo")
---

# Smitty's Bar & Restaurant<br>aka - A lesson in time-management, project-planning and sticking to the basics
<br>
This project was bootstrapped using the Restaurantly website template available from <https://bootstrapmade.com/restaurantly-restaurant-template/><br>
and powered by the Cross Platform Cloud IDE called Codeanywhere <https://app.codeanywhere.com/>

## Includes

- Layout and Navigation
- Programs and tools
- Bugs, problems and issues
- My feedback and experiences
- Links, references and credits
<br>

### Layout and Navigation

The website has 4 navigational pages:

| 'html' Page Name         |          Accessed how?          |
| ------------------------ | :-----------------------------: |
| 'index' Home             | Loading homepage, 'logging out' |
| 'login' Login            | Clicking on 'log in' button   |
| 'signup' Sign Up         | Clicking on 'sign up' button   |
| 'booktable' Book-a-table | Clicking on 'Book table' button |
<br>

#### The html pages


##### Homepage start up screen

This is the first screen upon opening the website. The homepage can also be accessed at any time by clicking on "SMITTY'S BAR & RESTAURANT" located to the left of the the links. It can be scrolled down and also has working links found across the top of the header.

These links are:

- Home
- How to book
- Menu
- Drinks
- Events
- Gallery
- Contact
<br>

##### Home "hero section"

This part of the webpage shows two buttons that change depending on whether the user is logged in or not.

This is the page in its default position. Before logging in, the user can either choose to log in or sign up:<br>
![Screenshot](static/assets/img/README/index1.jpg" "Main page hero when logged in")

And this is the page after logging in, the user can now access the "Book a Table" page or choose to log out:<br>
![Screenshot](static/assets/img/README/login2.jpg "Main page hero when logged in")
<br>

##### Other links on main page

The following links on the page are seen as follows:

How to Book:<br>
![Screenshot](static/assets/img/README/index2.jpg "How to book")

Menu:<br>
![Screenshot](static/assets/img/README/index4.jpg "Food choices")

Drinks:<br>
![Screenshot](static/assets/img/README/index5.jpg "Drinks choices")

Events:<br>
![Screenshot](static/assets/img/README/index6.jpg "Drinks choices")

Gallery:<br>
![Screenshot](static/assets/img/README/index7.jpg "Drinks choices")

\*Contact:<br>
![Screenshot](static/assets/img/README/index8.jpg "Contact")
<br>

#### Other html pages


##### Sign in page

This page is accessed through the "Sign Up" button and then the aim was that upon entering the nesessary details, the user would have their details registered to the admin part of django and then the user would be logged in(see bugs):<br>
![Screenshot](static/assets/img/README/signup.jpg.jpg "Contact")
<br>

##### Log in page

The aim here was that this should have been accessed through the "Log In" button and then entering a previously registered email address and password, the user would be logged in(see bugs):<br>
![Screenshot](static/assets/img/README/login1.jpg.jpg "Contact")

---

## Programs and tools

#### Programs

The following are a list of the technical stuff used during this website:

- Django
- Python
- JavaScript (Bootstrap only)
- HTML
- CSS

What should have also been used but wasn't (see problems):

- PSQL

#### Tools

The following are a list of the technical stuff used during this website:

- Bootstrap

#### Log in profiles and profiles used during production:

Superuser:
username: admin
email: admin@email.com
Password: September:2023

Email Smittys Bar:
email: testemailsmittysbar@gmail.com
password: SmittysBar:2023

Test User:
dave@daveemail.com / Dave / Davis / Thursday:2023

---

## My feedback

#### My feedback

I feel ashamed to hand in

---

## Links, references and credits

#### Links and references

- \*Bootstrap template:
  Template Name: Restaurantly<br>
  Template URL: <https://bootstrapmade.com/restaurantly-restaurant-template/><br>
  Link: <https://github.com/technext/restaurantly/releases/download/v1.0/Restaurantly.zip><br>
  Author: BootstrapMade.com<br>
  License: <https://bootstrapmade.com/license/><br>

- Help installing allauth:<br>
  Code with Stein <https://www.google.com/search?sca_esv=567555228&rlz=1C1CHBD_svSE1043SE1044&q=linking+django+allauth&tbm=vid&source=lnms&sa=X&ved=2ahUKEwjFjeKh9b2BAxUbRvEDHSdhA7MQ0pQJegQIChAB&biw=1536&bih=735&dpr=1.25#fpstate=ive&vld=cid:54078088>

- Pictures:<br>
  Pixabay <https://pixabay.com/>

- Help with authentication upon login:<br>
  djangoproject.com <https://docs.djangoproject.com/en/4.2/topics/auth/default/#auth-web-requests>

- Help with postgresql connection:<br>
  Profile: "Pretty Printed" <https://www.youtube.com/watch?v=t6RbanOhna4>

- Youtube online guides and tutorials: Codemy.com<br>

#### Credits

Mentor: Akshat Garg<br>
Fiverr debugger: Haris (coodingmentore)<br>
