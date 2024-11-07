import instaloader
import pandas as pd

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Login to Instagram account
username = 'Username'
password = 'password'
L.login(username, password)

# Get the profile of the logged-in user
profile = instaloader.Profile.from_username(L.context, username)

# Get followers and followees (people you follow)
followers = set(follower.username for follower in profile.get_followers())
followings = set(following.username for following in profile.get_followees())

# People who are not following you back
not_following_back = followings - followers  # People you follow but who don't follow you back
not_followed_back = followers - followings    # People who follow you but whom you don't follow back

# Convert lists to DataFrames for Excel
df_followers = pd.DataFrame(list(followers), columns=["Followers"])
df_followings = pd.DataFrame(list(followings), columns=["Followings"])
df_not_following_back = pd.DataFrame(list(not_following_back), columns=["Not Following Back"])
df_not_followed_back = pd.DataFrame(list(not_followed_back), columns=["Not Followed Back"])

# Create an Excel file with multiple sheets
with pd.ExcelWriter("instagram_data.xlsx") as writer:
    df_followers.to_excel(writer, sheet_name="Followers", index=False)
    df_followings.to_excel(writer, sheet_name="Followings", index=False)
    df_not_following_back.to_excel(writer, sheet_name="Not Following Back", index=False)
    df_not_followed_back.to_excel(writer, sheet_name="Not Followed Back", index=False)

print("The lists have been successfully saved to instagram_data.xlsx!")