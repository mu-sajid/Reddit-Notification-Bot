# Reddit Notification Script

Script that will send you a text message when someone comments any keyword in a specific subreddit, also able to reply to that comment.

###### Uses:
- Praw (Reddit API Wrapper) -- pip3 install praw
- Twilio (Communication API) -- pip3 install twilio


How to use:
- Install prerequisite API
- [Create an application on Reddit to use API](https://www.reddit.com/prefs/apps)
- Create config file that stores username, password, client_id, and client_secret
- [Create a twillio account](https://console.twilio.com)
- Replace 'client = Client("ACxxxxxxxxxxxxx", 'xxxxxxxxxxxxxxxx')' line with Account SID and Auth Token 
