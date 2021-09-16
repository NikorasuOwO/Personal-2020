import instaloader

USER = "liberal_paradise_store"
PASSWORD = "tshirtstothemoon"
PROFILE = USER

# Get instance
L = instaloader.Instaloader()

# Login or load session
L.login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file(USER) # (load session created w/
                               #  `instaloader -l USERNAME`)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, PROFILE)

# Print list of followees
for followee in profile.get_followees():
    print(followee.username)

# (likewise with profile.get_followers())
