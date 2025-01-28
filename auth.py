from flask import Flask, redirect, request, session, render_template, url_for
from data import htmldf  # Importing the HTML representation of the DataFrame
import requests

app = Flask(__name__)
app.secret_key = "nf3buf8nbucn9e38nf9c34ofk"  # Replace with a secure key

# Replace these with your GitHub OAuth App credentials
CLIENT_ID = 'Ov23li3i16KHX8LIEPg6'  # Your GitHub OAuth Client ID
CLIENT_SECRET = '35f56dae59bf401e10c6938cea16f024ea594037'  # Your GitHub OAuth Client Secret
REDIRECT_URI = 'https://dom-keller.github.io/bump.github.io/'  # Callback URL set in GitHub OAuth App settings

# GitHub OAuth endpoints
AUTHORIZATION_BASE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
USER_API_URL = "https://api.github.com/user/emails"

@app.route("/")
def index():
    """Home route."""
    if "user_email" in session:
        user_email = session["user_email"]

        # Filter the dataframe for the logged-in user's email
        user_row = df[df["Email"] == user_email].to_dict(orient="records")

        # Pass the first matching row to the template (if any)
        return render_template(
            "index.html",
            user_email=user_email,
            user_row=user_row[0] if user_row else None
        )
    else:
        # User is not authenticated, prompt login
        return redirect(url_for("login"))

@app.route("/login")
def login():
    """GitHub login route."""
    github_auth_url = f"{AUTHORIZATION_BASE_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=user:email"
    return redirect(github_auth_url)

@app.route("/callback")
def callback():
    """OAuth callback route to handle GitHub authentication."""
    # Retrieve the authorization code from the request
    code = request.args.get("code")
    if not code:
        return "Authorization failed. No code provided.", 400

    # Exchange code for access token
    token_response = requests.post(
        TOKEN_URL,
        headers={"Accept": "application/json"},
        data={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "code": code}
    )
    token_json = token_response.json()
    access_token = token_json.get("access_token")

    if not access_token:
        return "Authorization failed. Could not retrieve access token.", 400

    # Use access token to fetch user's primary email
    user_response = requests.get(
        USER_API_URL,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user_emails = user_response.json()

    # Get the primary email from the response
    primary_email = next((email["email"] for email in user_emails if email["primary"]), None)

    if not primary_email:
        return "Authorization failed. Could not retrieve primary email.", 400

    # Store user's email in the session
    session["user_email"] = primary_email

    # Redirect to the home page
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    """Logout route to clear the session."""
    session.pop("user_email", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
