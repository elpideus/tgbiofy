# tgbiofy

#### Display what you are currently listening to on your Telegram profile.

![Python Version](https://img.shields.io/badge/Python-v3.11-informational?style=for-the-badge&logo=python)
![GitHub release ](https://img.shields.io/github/v/release/elpideus/tgbiofy?include_prereleases&style=for-the-badge&logo=github)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/elpideus/tgbiofy?style=for-the-badge&logo=github)
![GitHub all releases](https://img.shields.io/github/downloads/elpideus/tgbiofy/total?style=for-the-badge&logo=github)
![GitHub](https://img.shields.io/github/license/elpideus/tgbiofy?style=for-the-badge)\
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/elpideus/tgbiofy?style=for-the-badge&label=Updates%20Frequency)
![GitHub last commit](https://img.shields.io/github/last-commit/elpideus/tgbiofy?style=for-the-badge&label=Updated)
![GitHub Repo stars](https://img.shields.io/github/stars/elpideus/tgbiofy?label=Stars&style=for-the-badge&logo=github)
![GitHub forks](https://img.shields.io/github/forks/elpideus/tgbiofy?label=Forks&style=for-the-badge&logo=github)
![GitHub watchers](https://img.shields.io/github/watchers/elpideus/tgbiofy?label=Watchers&style=for-the-badge&logo=github)

---

# Installation:

###### Clone this repo:
```bash
$ git clone https://github.com/elpideus/tgbiofy.git
```

###### Go to the "tgbiofy" directory:
```bash
$ cd tgbiofy
```

###### Install the required libraries using pip:
```bash
$ pip3 install -r requirements.txt
``` 

# Setting up:

### Telegram:

1. Go to [my.telegram.org](https://my.telegram.org/)
2. Authorize and click on API development tools
3. Create an application and set the web type (you can specify any names, we only need api_id and api_hash):
![1.1](https://github.com/L4zzur/spotify-to-telegram/raw/main/img/2.png)
> Don't share these tokens with anyone

### Spotify
1. Go to [Spotify Dashboard](https://developer.spotify.com/dashboard/)
2. Log in and create a new application 
![1.2](https://github.com/L4zzur/spotify-to-telegram/raw/main/img/3.png)
3. Go to the created application, and then in settings
![1.3](https://github.com/L4zzur/spotify-to-telegram/blob/main/img/4.png)
4. Add or change the Redirect URIs line: http://localhost:8080/callback
![1.4](https://i.ibb.co/phHsr5f/redirecturis.png)
>  Don't share these tokens with anyone

### Python
1. Edit the `config.ini` file by entering your data.

# Run
1. Run the script:
```bash
$ python3 Main.py
```
2. A web page will open in the browser. Let it load and then go back to the terminal.
3. Login by using your phone number. **!!!Bot tokens won't work!!!**
4. Enjoy!

---

# Configuration

From the `config.ini` file it is also possible to easily change the settings of the script. Changing these settings 
allow everyone to have a customized version of the script. The settings can be found under the `[!SETTINGS!]` section 
in the `config.ini` file.\
Below a list of the settings and a description of what each one does:
1. `lite_version` - Disables every other settings and only enables the `bio` setting. In other words it only allows for
the "_About_" section to be changed. It is **False** by default.
2. `first_name` - Allows for the first name to be changed. If **True** the first name will be `Listening to 
<song name>`. Usually it is suggested to set the same value as for `last_name`, and is **True** by default.
3. `last_name` - Allows for the last name to be changed. If **True** the last name will be `by <artist name>`. It is 
suggested to set the same value as for `first_name`, which is **True** by default.
4. `profile_photo` - The profile picture can be changed to the album's cover. It is **True** by default.
5. `bio` - Defines if and what should be changed in the _"About"_ section of the user's profile. It can be either
"**link**" or "**info**". The default value is **link**. 

It is possible to start and stop the script via a message to yourself (Saved Messages). You can either use 
`/tgbiofy start` or `/tgbiofy stop`. The script updates every 30 seconds, so you may need to wait at most 30 seconds 
before seeing the changes on your profile.

---

# Important - legal information

> A user by the name of [L4zzur](https://github.com/L4zzur) modified this project and published it as his own, without a
copyright notice nor a source disclosure. His upload is nothing more than a striped down version of this project which 
only allows for the "_About_" section to be changed.\
Pay attention to the fake copies out there and always examine the code before executing as it could contain indesired
malware (miners, keyloggers, ransomware, etc.). 

The license can be found inside this project. It is possible to modify this project and even distribute it for 
commercial purposes and/or patent use. However, the source need to be disclosed and there needs to be a copyright and 
license notice. Also, it needs to be published under the same license.

If your project includes or is a modified version of this script, and you are unsure about the legal terms contact me at
[elpideus@gmail.com](mailto:elpideus@gmail.com).