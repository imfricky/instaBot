from instabot import Bot
import os

# Creating the instance of instagram bot 
bot = Bot()

# credentials.txt is the file in which you have to write three particular
# In first line write the username
# In second line write the password
# In third line write the username of the account whose difference of followers and following you want to check

f = open("credentials.txt","r")
username_org = f.readline()
password = f.readline()
check_user = f.readline()


username_org = username_org.rstrip("\n")
password= password.rstrip("\n")
check_user= check_user.rstrip("\n")

#print(username)
#print(password)

# Close the credentials file
f.close()

# Here we are logging in to instagram using our bot
bot.login(username=username_org,password=password)

# We get the list of the followers of the user you mentioned in 3rd line of the credentials.txt
followers = bot.get_user_followers(check_user)

# We get the list of the followings of the user you mentioned in 3rd line of the credentials.txt
following = bot.get_user_following(check_user)



# Here we create a file followers.txt to save the list of username of followers and there full name
fname = "followers.txt"

with open(fname, "w", encoding="utf-8") as follower_txt:
    print("Working on the Followers File")
    follower_txt.write("The List of followers with thier Full Name : \n\n\n")
    for follower in followers:
        username = bot.get_username_from_user_id(follower)
        full_name = bot.get_user_info(follower).get('full_name')
        #print(username +" : "+full_name)
        follower_txt.write(username +" : "+full_name+"\n")

follower_txt.close()
print("Followers file completed and closed")


# Here we create a file following.txt to save the list of username of following and there full name
fname = "following.txt"

with open(fname, "w", encoding="utf-8") as following_txt:
    print("Working on the Followings File")
    following_txt.write("The List of Following with thier Full Name : \n\n\n")
    for following1 in following:
        username = bot.get_username_from_user_id(following1)
        full_name = bot.get_user_info(following1).get('full_name')
        #print(username +" : "+full_name)
        following_txt.write(username +" : "+full_name+"\n")

following_txt.close()

print("Followings file completed and closed")

# This is the set of difference of the users who are ain't following you back
following_difference = set(following) - set(followers)
# This is the list of difference of the users who are ain't following you back
list_of_following_difference = list(following_difference)

# This is the file in which the difference is stored
fname = "variance.txt"
with open(fname, "w", encoding="utf-8") as variance:
    print("Working on the difference of followers and following in variance file")
    variance.write("Total no of people whom you are following but there ain't following back : "+str(len(list_of_following_difference))+"\n")
    variance.write("List of People whom you are following but there ain't following back : \n")
    for difference in list_of_following_difference :
        username =bot.get_username_from_user_id(difference)
        full_name = bot.get_user_info(difference).get('full_name')
        variance.write(str(username) + "   :   " + str(full_name)+"\n")

    # This is the set of difference of the users whom you ain't following back
    followers_difference = set(followers)- set(following)
    # This is the list of difference of the users whom you ain't following back
    list_of_followers_difference = list(followers_difference)
    variance.write("###############################*************************************#############################")
    variance.write("Total no of people who are following you but you ain't following back : "+str(len(list_of_followers_difference))+"\n")
    variance.write("List of people who are following you but you ain't following back : \n")
    for difference in list_of_followers_difference:
        username = bot.get_username_from_user_id(difference)
        full_name = bot.get_user_info(difference).get('full_name')
        variance.write(str(username) + "   :   " + str(full_name)+"\n")

variance.close()
# variance.txt file closed
print("Variance file completed and closed")
bot.logout()
# Bot logged out of account



