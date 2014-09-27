#Aweber API for NodeJS

##Introduction

This repo contains NodeJS and Python scripts working together that allow you to easily integrate your app with [Aweber-Labs API](https://labs.aweber.com/getting_started/main). 

I created this repo out of frustration, because I didn't found anything that would help me use Aweber API with NodeJS

*Note: By using  [Python Aweber-Labs snippets](https://labs.aweber.com/snippets/authentication), you can easily add more functionnalities to this code.*

##Functionality :
The current code lets you add users (email and a validation code) to a pre-created Aweber list, Aweber then sends a validation email to the user.

##Requirements :

* Aweber access tokens, you can get them by using this [ressource from Aweber](https://labs.aweber.com/docs/authentication) :
```
consumer_key
consumer_secret
access_key
access_secret
```


* Python with AweberAPI package 
```
pip install aweber_api
```


* Node JS with python-shell package
```
npm install python-shell
```
