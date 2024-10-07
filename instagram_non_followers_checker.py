import instaloader

def check_non_followers(username: str, password: str):
    """
    Logs into an Instagram account and checks which users the account follows but do not follow back.

    Args:
        username (str): The Instagram username.
        password (str): The Instagram account password.

    Returns:
        None: Prints the usernames of the accounts that do not follow back.
    """
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Log in to the account
    L.login(username, password)

    # Load the user's profile
    profile = instaloader.Profile.from_username(L.context, username)

    # Get the list of followers
    followers = set(follower.username for follower in profile.get_followers())

    # Get the list of followees (people you follow)
    followees = set(followee.username for followee in profile.get_followees())

    # Find users you follow who don't follow you back
    non_followers = followees - followers

    # Print the non-followers
    print("Users who don't follow you back:")
    for user in non_followers:
        print(user)


# Replace 'your_username' and 'your_password' with your Instagram credentials
username = "your_username"
password = "your_password"

# Call the function to check for non-followers
check_non_followers(username, password)
