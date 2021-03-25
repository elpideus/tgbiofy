""" This module updates user's Telegram information when his song on Spotify is changed.
Author: elpideus <elpideus@gmail.com>
Version: Beta 1.0 """
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient
from datetime import datetime
from termcolor import colored
import urllib.request
import configparser
import spotipy
import time


config = configparser.ConfigParser()
config.read("config.ini")
client = TelegramClient(
    'default',
    int(config["!USER!"]["tg_api_id"]),
    config["!USER!"]["tg_api_hash"])
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope="user-read-currently-playing",
                                                       client_id=config["!SPOTIFY!"]["client"],
                                                       client_secret=config["!SPOTIFY!"]["secret"],
                                                       redirect_uri=config["!SPOTIFY!"]["redirect"]
                                                       ))  # Connects to Spotify API


async def main():
    """ This function is the main function of the program. """
    me = await client.get_me()

    while True:  # loop
        info = await client(GetFullUserRequest(id=me.username))
        if sp.currently_playing(config["!SPOTIFY!"]["market"]) is not None:
            song = sp.currently_playing(config["!SPOTIFY!"]["market"])["item"]
            if song is not None:
                if info.about != ("Listening to " + song["name"][0:57]):
                    if config["!SETTINGS!"]["names"] == "True":
                        await client(UpdateProfileRequest(
                            first_name="Listening to " + song["name"][0:57],
                            last_name="by " + song["artists"][0]["name"]
                        ))
                    if config["!SETTINGS!"]["bio"] == "True":
                        await client(UpdateProfileRequest(about="Listening to " + song["name"][0:57]))
                    print(datetime.now().strftime("%H:%M:%S > ") + "Listening to " +
                          colored(song["name"][0:57], "green") + " by " + colored(song["artists"][0]["name"], "green"))
                    if config["!SETTINGS!"]["profile_photo"] == "True":
                        urllib.request.urlretrieve(song["album"]["images"][0]["url"], "album.jpg")
                        if await client.upload_file("album.jpg") != await client.get_profile_photos(me):
                            await client(DeletePhotosRequest((await client.get_profile_photos(me))))
                            await client(UploadProfilePhotoRequest(await client.upload_file("album.jpg")))
                    time.sleep(30)
                else:
                    time.sleep(3)
        else:
            if config["!SETTINGS!"]["bio"] == "True":
                await client(UpdateProfileRequest(about="Not listening to music at the moment"))
            if config["!SETTINGS!"]["names"] == "True":
                await client(UpdateProfileRequest(
                    first_name=config["!USER!"]["first_name"],
                    last_name=""))
            time.sleep(10)


with client:
    print(datetime.now().strftime("%H:%M:%S > ") + colored("Program has been booted.", "green"))
    client.loop.run_until_complete(main())
