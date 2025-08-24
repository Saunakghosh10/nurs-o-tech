from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/user')
def user_dashboard():
    return render_template('user.html')

@app.route('/profile/<user_id>')
def profile(user_id):
    return render_template('profile.html', user_id=user_id)

# For Vercel deployment - simple WSGI app export
if __name__ == '__main__':
    app.run()
else:
    # Export the Flask app for Vercel
    application = app
