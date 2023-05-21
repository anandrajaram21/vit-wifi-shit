# VIT Wifi

## Do note that this repo is made for macOS users specifically.

Making VIT Wifi a lil less painful for macOS users. The captive portal keeps popping up every damn time, so here are some handy commands to disable the captive portal completely (dw, can be reversed)

```bash
sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean false
```

To enable the captive portal again (idk, if you feel sussy about something)

```bash
sudo defaults delete /Library/Preferences/SystemConfiguration/com.apple.captive.control Active
```

Also, pls restart your mac after running the above commands

Now that the pain in the ass captive portal is out of the way, we can just move on to the actual VIT Wifi login.

This repo has 3 Python scripts

1. wifi-connect-login.py - This finds the VIT wifi network, connects to it, and logs you into the wifi
2. wifi-login.py - This just logs you into the wifi (assumes you are already connected to VIT wifi) (Much faster than 1)
3. wifi-logout.py - idk why you'll need it, but its just there

Please install the following using pip install

1. requests
2. python-dotenv

Copy the .env.example file to a .env file

Change variables in the .env to have your specific username and password.

Create a macOS shortcut to run the script. If something doesn't work, google it.
