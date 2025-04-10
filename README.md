# linkedin-activity-scraper
This is a python script that logs into your Linkedin account, and downloads your latest 30-40 posts and comments. In HTML format.

=> Make sure you have the latest chromedriver in your machine (i use it on ubuntu)
=> If you use it on Windows, go: https://googlechromelabs.github.io/chrome-for-testing/
=> Get the latest stable version
=> Download it, and MAKE SURE YOU EXTRACT/UNZIP the folder under C:\Windows 
=> So you dont have to add anything to the path
=> Clone the repo
=> CD to the directory
=> And then from the terminal executing the script with python linkedin.py should work

### The script does the following things

1. Fires up Chrome browser
2. Goes to linkedin
3. It is a test software so it asks you to login
4. It logins with your credential (make sure in the file to update all the URL and password/username credentials
5. Maximizes the window
6. Then it visits the pages for posts and comments
7. Downloads everything in html format.


### New Script for messaging

1. Visits users profiles
2. Clicks message button
3. Send private message
