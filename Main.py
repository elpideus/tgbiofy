""" This module updates user's Telegram information when his song on Spotify is changed.
Author: elpideus <elpideus@gmail.com>
Version: Beta 1.0 """
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from spotipy.oauth2 import SpotifyOAuth
from telethon import TelegramClient
from datetime import datetime
from termcolor import colored
import urllib.request
import configparser
import spotipy
import time


config = configparser.ConfigParser()
config.read("config.ini")  # Reads the configuration file
client = TelegramClient(
    'default',
    int(config["!USER!"]["tg_api_id"]),
    config["!USER!"]["tg_api_hash"])  # Creates a connection to Telegram
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-currently-playing",
                                               client_id=config["!SPOTIFY!"]["client"],
                                               client_secret=config["!SPOTIFY!"]["secret"],
                                               redirect_uri=config["!SPOTIFY!"]["redirect"]
                                               ))  # Connects to Spotify API


async def main():
    """ This function is the main function of the program. """
    me = await client.get_me()  # Gets the user after phone number verification

    while True:  # loop
        info = await client(GetFullUserRequest(id=me.username))  # Gets some info about the Telegram user
        if sp.currently_playing(config["!SPOTIFY!"]["market"]) is not None:
            # If there is a song playing (no ad). If this is not getting checked the program crashes cause of an error.
            song = sp.currently_playing(config["!SPOTIFY!"]["market"])["item"]
            # Gets some information about the Spotify song
            print(song)
            if info.about != ("Listening to " + song["name"][0:57]):  # Checks if the user Telegram Bio is not the same
                await client(UpdateProfileRequest(
                    first_name="Listening to " + song["name"][0:57],
                    last_name="by " + song["artists"][0]["name"],
                    about="by " + song["artists"][0]["name"]
                ))  # Updates the Telegram user names and bio
                print(datetime.now().strftime("%H:%M:%S > ") + "Listening to " + colored(song["name"][0:57], "green") +
                      " by " + colored(song["artists"][0]["name"], "green"))
                urllib.request.urlretrieve(song["album"]["images"][0]["url"], "album.jpg")  # Downloads the album image
                if info.profile_photo != await client.upload_file("album.jpg"):
                    await client(UploadProfilePhotoRequest(await client.upload_file("album.jpg")))
                # Updates the Telegram user profile photo
                time.sleep(30)  # Waits for 30 seconds
            else:
                time.sleep(3)  # Waits three seconds
        else:  # If no song is playing
            await client(UpdateProfileRequest(
                about="Not listening to music at the moment",
                first_name=config["!USER!"]["first_name"],
                last_name=""
            ))  # Updates bio and names
            time.sleep(10)  # Then waits for 10 seconds


with client:
    print(datetime.now().strftime("%H:%M:%S > ") + colored("Program has been booted.", "green"))
    client.loop.run_until_complete(main())
