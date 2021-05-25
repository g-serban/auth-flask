# flask-secure-login-page


Project structure:
.
└── flask_auth_app

    └── project
    
        ├── __init__.py       # setup our app
        
        ├── auth.py           # the auth routes for our app
        
        ├── db.sqlite         # our database
        
        ├── main.py           # the non-auth routes for our app
        
        ├── models.py         # our user model
        
        └── templates
        
            ├── base.html     # contains common layout and links
            
            ├── index.html    # show the home page
            
            ├── login.html    # show the login form
            
            ├── profile.html  # show the profile page
            
            └── signup.html   # show the signup form
