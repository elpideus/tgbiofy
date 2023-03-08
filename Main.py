""" This module updates user's Telegram information when his song on Spotify is changed.
Author: elpideus <elpideus@gmail.com>
Version: Beta 2.0 """

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
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

    first_name = config["!SETTINGS!"]["first_name"]
    last_name = config["!SETTINGS!"]["last_name"]
    profile_photo = config["!SETTINGS!"]["profile_photo"]
    bio_act = config["!SETTINGS!"]["bio"]
    bio_link = config["!SETTINGS!"]["bio_link"]
    market = config["!SPOTIFY!"]["market"]
    me = await client.get_me()

    await client.download_profile_photo(me, "pfpic.jpg", download_big=True)

    while True:
        if sp.currently_playing(market) is not None and sp.currently_playing(market)["item"] is not None:
            if me.first_name != "Listening to " + sp.currently_playing(market)["item"]["name"]:
                if first_name == "True":
                    await client(UpdateProfileRequest(
                        first_name="Listening to " + sp.currently_playing(market)["item"]["name"]
                    ))
                if bio_act == "True":
                    if bio_link == "True":
                        await client(UpdateProfileRequest(
                            about=sp.currently_playing(market)["item"]["external_urls"]["spotify"]
                        ))
                    else:
                        await client(UpdateProfileRequest(
                            about=sp.currently_playing(market)["item"]["name"] + " - " + sp.currently_playing(market)[
                                "item"]["artists"][0]["name"]
                        ))

            if me.last_name != "by " + sp.currently_playing(market)["item"]["artists"][0]["name"] \
                    and last_name == "True":
                await client(UpdateProfileRequest(
                    last_name="by " + sp.currently_playing(market)["item"]["artists"][0]["name"]
                ))

            if profile_photo == "True":
                urllib.request.urlretrieve(sp.currently_playing(market)["item"]["album"]["images"][0]["url"],
                                           "album.jpg")
                await client(DeletePhotosRequest((await client.get_profile_photos(me))))
                await client(UploadProfilePhotoRequest(file=(await client.upload_file("album.jpg"))))

        time.sleep(30)  # the only fix that works for now


with client:
    print(datetime.now().strftime("%H:%M:%S > ") + colored("Program has been booted.", "green"))
    client.loop.run_until_complete(main())
