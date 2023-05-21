import requests
import subprocess
import os
import time
from dotenv import dotenv_values


def login(username, password):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://phc.prontonetworks.com",
        "Referer": "http://phc.prontonetworks.com/cgi-bin/authlogin",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }

    data = {
        "userId": username,
        "password": password,
        "serviceName": "ProntoAuthentication",
        "Submit22": "Login",
    }

    response = requests.post(
        "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html",
        headers=headers,
        data=data,
        verify=False,
    )


def check_connection():
    try:
        requests.get("https://www.google.com")
        return True
    except:
        return False


def check_vit_wifi():
    command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s | awk '{print $1}'"
    networks = subprocess.check_output(command, shell=True).decode("utf-8").split("\n")
    networks = networks[1:-1]
    vit_networks = [
        network for network in networks if "VIT5G" in network or "VIT2.4G" in network
    ]
    if len(vit_networks) == 0:
        print("VIT Wifi not found")
        return
    else:
        return vit_networks[0]


def main():
    count = 0
    username = config["USERNAME"]
    password = config["PASSWORD"]

    while count < 3:
        login(username, password)
        if check_connection():
            print("Login Successful")
            break
        else:
            print("Trying again")
            count += 1

    if count == 3:
        print("Login Failed")


def connect_vit_wifi(connect_wifi):
    if connect_wifi:
        vit_network = check_vit_wifi()
        if vit_network is None:
            return
        else:
            command = f"networksetup -setairportnetwork en0 {vit_network}"
            subprocess.check_output(command, shell=True)
            time.sleep(3)
    main()


dir_path = os.path.dirname(os.path.realpath(__file__))
config = dotenv_values(f"{dir_path}/.env")
connect_vit_wifi(True)
