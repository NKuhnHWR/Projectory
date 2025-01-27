from flask import Flask

app = Flask(__name__)

@app.route("/")
def landingpage():
    return "<p>Welcome to Projectory!</p>"

@app.route('/view_guest/<int:profile_id>')
def view_guest(profile_id):
    return 'Here the profile for a specific project is visible. (Only view, no Edit)'

@app.route('/register')
def register():
    return 'Create a new account here'

@app.route('/login')
def login():
    return 'Welcome back! Login to your already existing account'

@app.route('/view_user/<int:profile_id>')
def view_user(profile_id):
    return 'User can see his or her page and click on Edit or New project'

@app.route('/create project/project_id')
def view_profile(project_id):
    return 'Add a new project to your Projectory'

@app.route('/edit_profile/<int:project_id>')
def view_profile(project_id):
    return 'Update your profile information here'