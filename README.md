# full-stack-frameworks-django

[Issue Tracker](https://full-stack-frameworks-django.herokuapp.com/) is a Django web application developed as part of the Code Institute Full Stack Software Development Diploma - FULL STACK FRAMEWORKS DJANGO module. 

### What is this site for?
 
 This portal is a support center for the imaginary BUZZ application (the App). It facilitates the resolution of bugs and the implementation of new feature requests for the App. When logged in, a user may view the list of tickets (BUGS or FEATURES), view a single ticket's page to get more information, vote on a ticket (each user can only vote once per ticket) and edit tickets (users may only edit tickets which they created). When voting on tickets, users are charged 5 Euro to vote on a Feature. Voting on bugs is free.
 The promise is that the developers will spend at least 50% of their time working on the highest ranking feature.
 In addition to the ticket system there is also a blog which is maintained and updated by staff. The Blog is readonly for non-staff users. Blog posts can only be edited by their original author.

 
### How does it work
 
The site is divided into multiple django apps. One for each logical function/section. Django uses the Model View Controller (MVC) Architecture pattern. The model (model.py) represents the data in a database, the views (html templates styled with css) display the data in the client and the controller (view.py) is the middleman that allows communication between the two. Each app has its own self contained MVC implementation.

#### accounts

The accounts app looks after user authentication and makes use of the powerful built in django authentication `django.contrib.auth` module. 

#### blogposts

The blogposts app manages the blog section of the project. Its controller is responsible for retrieving blogpost data and updating the blogpost model with new or edited blog posts. Each of the functions are preceded by the `@login_required` decorator. The Model here contains a class representing the Post entity and the view is comprised of three html templates.

#### payments

The payments app manages the payments side of things. Users are redirected to the payments view function when voting on a 'Feature' ticket. Then from here the charge view function is used to make a payment using the stripe API. When the charge is processed the `vote_service` is triggered to actually register the vote.

#### vote_service

In the services folder you will find the vote_service module. This will register a vote on a ticket in the database and was abstracted out as a service because the voting functionality is used by both the ticket app and the payments app.

#### tickets

The tickets app manages the tickets in the project. The views.py file has four functions: all_tickets; ticket_detail; create_or_edit_ticket; upvote_ticket; which retrieve a list of tickets, retrieve individual tickets by id, create or edit tickets and upvote tickets respectively. Like the in blogposts app each of these functions is protected by the `@login_required` decorator and the create/edit function includes logic which only allows ticket owners to edit their own tickets. 
Further to this two custom template tags were created to check if a user already voted on a particular ticket and to check if a user owns a ticket and if so the template logic will disable the upvote and edit buttons for that ticket respectively. 

#### home

The home app serves the index page.


## Technologies Used

- [Django](https://www.djangoproject.com/)
    - **Django** was used as the web framework for this project. This is an opinionated framework which comes with 'batterise included' and facilitates rapid application development.

- [SQLite](https://www.sqlite.org/index.html)
    - **SQLite** comes as standard with django and was used during the development phase as the primary database for this project.

- [python-dotenv](https://pypi.org/project/python-dotenv/)
    - The **python-dotenv** package was used to set environment variables from a local .env file during development.

- [stripe](https://stripe.com/ie)
    The **stripe** payments platform was used to facilitate online payments.

- [PostgreSQL](https://www.postgresql.org/)
    - The project database was switched to **PostgreSQL** when moving to the production environment. This is the preferred database system when deploying apps to [Heroku](https://www.heroku.com/)

- [Psycopg2](http://initd.org/psycopg/)
    - **Psycopg** was used as a PostgreSQL adapter when the application was moved to the production environment.

- [dj_database_url](https://pypi.org/project/dj-database-url/)
    - **dj_database_url** is a package which facilitates the use of the DATABASE_URL environment variable to configure a Django application.

- [Whitenoise](http://whitenoise.evans.io/en/stable/)
    - **Whitenoise** was utilised to serve the application's static files once it was deployed to [Heroku](https://www.heroku.com/)

- [gunicorn](https://gunicorn.org/)
    - In the production environment **Gunicorn** was used as the WSGI HTTP Server.


## Testing

Testing has been automated using the django.test library. 
Each app has its own test.py module within which the test cases were constructed. 

To run these tests run this command from your terminal when at the root of the project: `python3 -m unittest`


## Deployment

### Heroku

The site was deployed to Heroku via new branch (production) which was based on the master branch. Environment variables used for the database were replaced with corresponding config vars.

### Locally

If you would like to run this code locally, follow these instructions:

1. Clone the repository 
  * (with ssh) `git clone git@github.com:JamesDungan/code-institute-data-centric.git` 
  * (with https) `https://github.com/JamesDungan/code-institute-data-centric.git`
2. Open the folder in your favorite IDE
3. Install [python3](https://www.python.org/downloads/) on your machine 
4. Open a terminal and from the root of this project create a virtual environment where you will install all of your dependancies
5. Then activate the virtual environment and run `pip install -r requirements.txt` from the root of the project.
6. You will have to replace MONGODB_URI, DBS_NAME and COLLECTION_NAME in database.py with your own database credentials.     
6. Now that all of your dependancies have been installed you can run the app by running `python3 rest-server`


