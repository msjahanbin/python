# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'username'  # <- enter username here
insta_password = 'password'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True)

    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["flower"], amount=3)
    
