# myPhone
<p>myPhone tries to link you phone and laptop/computer much closely although windows has a pretty neat implementation of this in form of Your Phone(obviously the motivation for the name) and so do linux in form of GSConnect and KDE Connect but we wanted to try it out and see how we could do that. This project started of as final project that we had to submit for passing and completing a subject (Software Engg.) but for me and my teammates it is much more than that cause it was our first actual project. Though this has a lot of problems and issues cause it was something we were building while learning. But still it works!!</p>

<p>This project would not have been possible without the two amazing piece of software Termux and Termux-api. These two projects were the only reason we could make this. Who would have even thought of making a software for android in Python but thanks to termux we were actually able to do that and not only that but actually get a lot of features are for the most part dependant on Termux-api from which enables us to do all the cool stuff like call and find phone etc.</p>

## Current Features ##
  * Find Phone :- Plays a ring on your phone (play and pause both supported).
  * Clipboard Access :- Anything you copy on phone would be available to laptop/computer.
  * File Access :- It accesses documents, music, images, and audio files and makes then available for access over the network.
      * Music can be played directly through the app.
      * Videos can also be played directly in the app
  * Calling :- A simple dialer that lets you make calls through your laptop/computer. (Though you need to pick your phone to talk)
  * Battery Access :- Lets you see how much battery is left.
  * Contact Access :- Lets you see contacts on your phone. (Has a few bugs)

## Working ##
Most of the functionality of this app comes from Termux and Termux-api. Termux enables this app to run by providing an environment wherein we can run python code in Android and that is what basically enables in running the app. The app runs a Flask server on your phone through which all the data is actually made available 
on the laptop. With the help of python we first find all the files we need and then make then available as links or some other way in case of media. Which is basically the whole File access part.

Then for the rest of the features it is termux-api that comes into play. By using termux commands which are provided by termux-api we can fetch contacts, make calls, access battery, access clipboard etc. For e.g. to access the battery we make a get request to */getBattery* which in turn makes a proper call to termux api that which provides us with the data needed and similarly for other features.

## Installation ##
 * Install termux and termux api (available on play store) on your phone.
 * Clone the repo using (in your phone using termux)
     ```sh
    git clone https://github.com/Taru-garg/SoftwareEngineeringProject
    ```
 * Open the repo and install the requirements using ( Install python before this ```pkg install python``` )
     ```sh
     cd SoftwareEngineeringProject
     pip install -r requirements.txt 
     ```
  * Install termux-api using
      ```sh
      pkg install termux-api
      ```
  * There are a few things that you will have to setup while using the app. In case Termux doesn't have a permission the app will tell you to check phone where
    you will have to give that permission to use that feature.
    
## Running the app ##
  * You need to go to the folder where you cloned the app and then
    ```sh
    cd SoftwareEngineeringProject/server
    python myPhone_server.py 
    ```
## TODO ##
  * We always wanted to somehow bring audio(call) somwehow to laptop so that a person can make a call through this app and talk without even lifting the phone but 
    couldn't figure that out.
  * Notification Access
  * Some security
  
