""" This module updates user's Telegram information when his song on Spotify is changed.
Author: elpideus <elpideus@gmail.com>
Version: 1.3 """

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient
from datetime import datetime

from telethon.tl.functions.users import GetFullUserRequest
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

    lite = config["!SETTINGS!"]["lite_version"]
    first_name = config["!SETTINGS!"]["first_name"]
    last_name = config["!SETTINGS!"]["last_name"]
    profile_photo = config["!SETTINGS!"]["profile_photo"]
    bio = config["!SETTINGS!"]["bio"]
    market = config["!SPOTIFY!"]["market"]
    me = await client.get_me()
    currently_playing_song_verify = ""
    timeout = 0
    old_first_name = f'{(me.first_name if me.first_name is not None else "")}'
    old_last_name = f'{(me.last_name if me.last_name is not None else "")}'
    old_full = await client(GetFullUserRequest(me))
    old_about = f'{(old_full.full_user.about if old_full.full_user.about is not None else "")}'
    await client.download_profile_photo(me, "pfpic.jpg", download_big=True)

    while True:
        if currently_playing_song_verify != sp.currently_playing(market)["item"]["name"]:
            timeout = 0

            if bio == "link" and lite != "True":
                await client(UpdateProfileRequest(
                    about=sp.currently_playing(market)["item"]["external_urls"]["spotify"]
                ))
            else:
                await client(UpdateProfileRequest(
                    about="🎵 " + sp.currently_playing(market)["item"]["name"] + " - " + sp.currently_playing(market)[
                        "item"]["artists"][0]["name"]
                ))

            if me.first_name != "Listening to " + sp.currently_playing(market)["item"]["name"] and lite != "True":
                if first_name == "True":
                    await client(UpdateProfileRequest(
                        first_name="Listening to " + sp.currently_playing(market)["item"]["name"]
                    ))

            if me.last_name != "by " + sp.currently_playing(market)["item"]["artists"][0]["name"] \
                    and last_name == "True" and lite != "True":
                await client(UpdateProfileRequest(
                    last_name="by " + sp.currently_playing(market)["item"]["artists"][0]["name"]
                ))

            if profile_photo == "True" and lite != "True":
                urllib.request.urlretrieve(sp.currently_playing(market)["item"]["album"]["images"][0]["url"],
                                           "album.jpg")
                await client(DeletePhotosRequest((await client.get_profile_photos(me))))
                await client(UploadProfilePhotoRequest(file=(await client.upload_file("album.jpg"))))

            currently_playing_song_verify = sp.currently_playing(market)["item"]["name"]

        if timeout >= 1:
            await client(UpdateProfileRequest(first_name=old_first_name, last_name=old_last_name, about=old_about))
            await client(DeletePhotosRequest((await client.get_profile_photos(me))))
            await client(UploadProfilePhotoRequest(file=(await client.upload_file("pfpic.jpg"))))

        timeout += 10
        time.sleep(30)  # the only fix that works for now


with client:
    print(datetime.now().strftime("%H:%M:%S > ") + colored("Program has been booted.", "green"))
    client.loop.run_until_complete(main())
