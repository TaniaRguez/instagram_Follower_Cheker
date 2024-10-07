# Instagram Non-Followers Checker

This Python script allows you to log into your Instagram account and check which users you follow but do not follow you back. The script uses the `Instaloader` library to retrieve your followers and followees securely, without exposing your credentials.

## Features
- Secure login using `Instaloader`.
- Retrieves a list of users you follow and users who follow you.
- Outputs the list of users who don't follow you back.
- Designed to maintain user privacy by not storing credentials or session data unnecessarily.

## Prerequisites
To run this script, you need to have:
- Python 3.6 or above installed.
- The `Instaloader` library installed. You can install it via pip:

  ```bash
  pip install instaloader

--------------------------------------------------------------------

# How to Use?
1. Clone this repository or download the script.
   git clone https://github.com/yourusername/instagram-non-followers-checker.git
2. Replace your_username and your_password in the script with your Instagram credentials.
3. Run the script:
    python instagram_non_followers_checker.py
4. The script will print a list of users that you follow but do not follow you back.

--------------------------------------------------------------------

# Error Handling
If you encounter an error that looks like this:
  LoginException: Login: Checkpoint required. Point your browser to /challenge/action/... - follow the instructions, then retry.

This is a security mechanism from Instagram. To resolve it:

1. Copy the URL provided in the error message and paste it into your browser "www.instagram.com/(paste here)".
2. Follow the instructions from Instagram to verify your login (this may involve confirming your identity via email or phone).
3. Once you've completed the verification, run the script again.

Other Common Issues
  - Rate Limiting: Instagram may limit the number of login attempts or requests. If this happens, wait a few minutes before trying again.
  - Invalid Credentials: Double-check your username and password if you receive a login error.
  - Session Expiration: The script does not store your session by default. You may need to log in again if your session expires.

-----------------------------------
** Privacy Notice
This script was created with user privacy in mind. It:
  - Does not store or log your Instagram credentials.
  - Uses Instagram's official mechanisms to log in securely.
  - Does not share your data with any third parties.
  - You can verify the source code to ensure that your credentials remain safe.


---------------------------

# Contributing
Feel free to submit issues or pull requests to improve the script. Contributions are always welcome!**
