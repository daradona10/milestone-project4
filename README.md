
# Milestone Project 4: Football World Website:

The deployed website can be accessed from here(Heroku): [https://daradona10-milestoneproject4.herokuapp.com/]

Travis Continuous Integration Testing: [![Build Status](https://travis-ci.org/daradona10/milestone-project4.svg?branch=master)](https://travis-ci.org/daradona10/milestone-project4)


# Goal of the website

The website created is an fully functioning e-commerce website that allows the user to buy the latest football training equipment whether for their local football team
or for leisure play by selecting their size, quantity and adding to the cart. It also allows them to register before checking out. 

# Project Purpose

The project purpose is to demonstrate Full Stack development of the website. The website utilises a PostGres databse together with Python code to access and manipulate
the data. Visualisation is done with HTML, CSS, and JavaScript where required, utilising the Django framework.

# UX

The website provides the relevant functionality to satisfy the requirements in detail( guided by user stories/requirements):

- Provides the opportunity to showcase the latest equipment from Jerseys to Footballs without having to register or login first.
- Provides the opportunity to register in order to complete your order in the checkout page.
- Provides the owner of the site to create, update and delete categories as needed for the site, through the admin panel.

# User Stories

- As a visitor of this site, I want to be able to recommend to other people for the products that are on sale and knowing the quality and pricing is of very good value.
- As a person who is interested in football, I want to be able to browse through the latest football equipment I wish to purchase for my own requirments.
- As a person who registers with the site to be able to checkout with ease when paying for my products.
- As a member of the site, I want to be able to retreive my password if I have forgotten it.
- As a site owner, I want to be able to create, edit or delete categories(products) on this site
- As a site owner I want to be able to see the history order from people who have registered  and to see people who have signed up with the website.

### Wireframes:
Wireframes for the initial development of the site can be found here:
- [Desktop](https://github.com/daradona10/milestone-project4/blob/master/development/Milestone%20Project%204%20desktop.pdf)
- [Mobile](https://github.com/daradona10/milestone-project4/blob/master/development/Milestone%20Project%204%20Mobile.pdf)

### Design Considerations:
It was decided to style the website with a simple and with minimal colors to order to enhance the products pages:
- Multi Page Layout in order to showcase the relevant product pages
- Simple and logical navigation

The design utilises the Bootstrap grid system, containers and components responsive to different screen sizes and devices and using some Font Awesome for icons.
The site is limited tot he use of HTML, CSS, Python, Django and PostGres.

## Features

- Feature 1 - Navigation: Simple navigation of the site that jumps to the selected section on the site (at top of each page).
- Feature 2 - Categories: Ability to view whatever you click on whether on top of Home page or at the bottom.
- Feature 3 - Ability to be able to choose the correct size of garment with a handy drop down menu button.
- Feature 4 - Ability to be able to order whatever quantity of the products the user wishes to purchase.
- Feature 5 - The ability to be able to read about the product description which gives a good indication of whether this product is right for the buyer.
- Feature 6 - Purchase: Ability to purchase products which is stored in the cart.
- Feature 7 - Payment: Ability to fill in details for the product(s) in checkout page and to pay with credit card to complete the sale.
- Feature 8 - Register User: Ability to register as a new user for the person to be able to checkout and complete the sale.
- Feature 9 - Log In: Ability to log in as user.
- Feature 10 - Password Reset: Ability to reset password securely if user forgets password.
- Feature 11 - Social Media: Links to social media platforms.

### Features Left to Implement

- Feature A - Email order to purchaser on successful transaction
- Feature B - To have besides Add to Cart button, a Save for Later button so the buyer can come back later and decide whether to go ahead or delete
- Feature C - To be able to save their contents in the cart after they logged out and then log back in so that it doesn't reset everytime
- Feature D - To have the contact us page listing contact number and email address
- Feature E - To have a newsletter for the latest products drop
- Feature F - To have a Add Discount Code in checkout page
- Feature G - To have a discount for bulk buy especially if a local football team wants to purchase many items
- Feature H - To have another page layout for sale items

## Technologies Used

The following languages, frameworks, libraries, IDE, repositories and tools were used for this website:

- HTML - The project utilises the HTML language for basic layout and functionality

- CSS - The project is styled using CSS where required for classes and specific elements

- Bootstrap - This project utilizes the Bootstrap grid system and components (incorporated through the Bootstrap CDN), to create the layout and responsive design of the page.

- Font Awesome - This project utilises FontAwesome CDN for icons utilised on the website.

- GitPod - This project was created using GitPod IDE for development, as well as committing of progress to GitHub and Heroku.

- Travis CI - This project uses Travis Continuous Integration Testing for build testing.

- AWS 3 - This project uses Amazon Web Services S3 for hosting of static and media files.

- AWS IAM - This project uses **Amazon Web Services IAM ** for access management between the hosted app and S3.

- Heroku - This project uses Heroku for hosting and running of the application.

- GitHub - This project uses GitHub for hosting of project repository.

- W3C CSS Validation Service - This project was tested using the W3C CSS Validation Service for checking conformity and validity of css content.

- W3C Markup Service - this was used for checking conformity and validity of HTML.

# Testing

Testing for the site was performed as follows:

# Code Validation

The HTML file was not passed through the W3C HTML Validation site, due to the use of the Dajngo Template Framework, many errors and warnings raised.
The custom.css file was tested using the W3C CSS Validation site, with no errors reported.

The site was tested on Google Chrome (desktop and mobile ), and Safari (mobile only iPhone6) for functionality. Verified working well although some footer problems
wasn't showing up on all mobile devices.

## Deployment

This project is deployed on Heroku and GitHub and is accessible as follows:

- Website: [https://daradona10-milestoneproject4.herokuapp.com/]
- Repository: [https://github.com/daradona10/milestone-project4]


For this project I used the GitPod IDE platform. The platform allowed me to commit my pages (and changes) to Git, following which it was pushed through to the GitHub repository.

This website can be locally deployed from GitHub by following the method outlined below:

- Use the following link to access the project repository: GitHub.
- Click on the Clone or Download button, under the repository name.
- Copy the clone URL for the repository, found in the Clone with HTTPS section.
- Open Git Bash in your local IDE environment.
- Select the location to where the cloned directory must be made.
- Input git clone together with the copied clone URL into Git Bash and press Enter.
- Create an env.py file in the project directory and set environmental variables for your working environment, which should include the following:
- os.environ.setdefault("HOSTNAME", "Your Hostname")
- os.environ.setdefault("SECRET_KEY", "Your Secret key")
- os.environ.setdefault("EMAIL_ADDRESS", "Your site Email address")
- os.environ.setdefault("EMAIL_PASSWORD", "Your site Email password")
- os.environ.setdefault("STRIPE_PUBLISHABLE", "Your Stripe publishable key")
- os.environ.setdefault("STRIPE_SECRET", "Your Stripe secret key")
- os.environ.setdefault("DATABASE_URL", "Your Postgres database url")
- os.environ.setdefault("AWS_ACCESS_KEY_ID", "Your AWS access key")
- os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "Your AWS secret acess key")
- For the above environmental variables, you will be required to create/provide account details, which include:
- Stripe: Register an account and obtain the relevant keys (for testing environments)
- AWS: -- S3: Create the relevant buckets in order to store static and media files, obtain relevant credentials. -- IAM: Set the relevant permissions and accesses
- PostGres: Access can be created once the project is deployed to Heroku, by creating a new app and creating a Heroku PostGres resource under the Resources tab. The DATABASE_URL can be obtained from the Config Vars under the Settings tab.
- Note that if this is not done, the app will revert to a SQLite database.
- Never publish or push the env.py to public repositories.
- The website can be deployed to and from Heroku by following the next steps:

- Go to the Heroku website to sign up. Create a new project by clicking the New button.
- Download and install the Heroku CLI in your IDE.
- Connect your GitHub to your account in the deploy section on Heroku
- Make sure that the relevant environmental variables is set under the Config Vars section under the Settings tab.
- The deployed version on Heroku is the same as the development version.

# Credits:

# Content:

- Inspiration and product descriptions taken from [www.prodirectsoccer.com]

- This is for educational purposes only and in no way related.

- Images were taken from google images wherever appropriate 

# Code:

- Code especially for the more complex issues like accounts setup, checkout apps and deploying to Heroku properly have been adapted from Code Institute's course material.

- Implementation of certain code have been adapted from the Django Documentation as was indicated on quite a few occasions by my mentor and fellow CI tutors.

# Acknowledgements:

- I would like to thank my mentor, Brian Macharia for input provided during the development of the site.
- I would to thank all the Code Institute tutors especially to Samantha Dartnall who helped me numerous times with some complex issues.
- I want to thank my main tutor Xavier for a lot of help
- To my fellow peers in my group who guided me also
- To a lot of people in the Slack community also










