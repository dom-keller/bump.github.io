import requests
from flask import Flask, redirect, request, url_for

# Initialize Flask app (this will be your web server)
app = Flask(__name__)

# GitHub OAuth app credentials (replace with your own)
client_id = 'Ov23li3i16KHX8LIEPg6'  # Your GitHub OAuth Client ID
client_secret = '35f56dae59bf401e10c6938cea16f024ea594037'  # Your GitHub OAuth Client Secret
redirect_uri = 'http://localhost:8000/callback'  # Callback URL set in GitHub OAuth App settings

# Step 1: Redirect to GitHub for OAuth login
@app.route('/')
def home():
    auth_url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={client_id}&redirect_uri={redirect_uri}&scope=user:email"
    )
    return redirect(auth_url)

# Step 2: GitHub redirects here with a code parameter
@app.route('/callback')
def callback():
    # Get the code from the URL
    code = request.args.get('code')

    # Step 3: Exchange the code for an access token
    token_url = 'https://github.com/login/oauth/access_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': redirect_uri,
    }
    headers = {'Accept': 'application/json'}

    # Make POST request to exchange the code for the access token
    response = requests.post(token_url, data=data, headers=headers)
    access_token = response.json().get('access_token')

    # Step 4: Use the access token to get the user's profile info (including email)
    if access_token:
        user_info = get_user_info(access_token)
        return f"User Info: {user_info}"
    else:
        return "Failed to get access token"

# Function to get user's info using the GitHub API
def get_user_info(access_token):
    user_api_url = 'https://api.github.com/user'
    headers = {'Authorization': f'token {access_token}'}

    response = requests.get(user_api_url, headers=headers)
    user_info = response.json()

    # Get the user's primary email (if public)
    email = user_info.get('email', 'No email found (may be private)')

    # Fetch additional verified email addresses
    email_api_url = 'https://api.github.com/user/emails'
    response = requests.get(email_api_url, headers=headers)
    emails = response.json()

    # You can choose to display all emails or just the first one
    verified_emails = [email['email'] for email in emails]

    return f"Primary Email: {email}, Verified Emails: {verified_emails}"

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=8000)
