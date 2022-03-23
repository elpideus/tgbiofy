# tgbiofy

#### Display what you are currently listening to on your Telegram profile.
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

# Запуск / Run
1. Run the script:
```bash
$ python3 Main.py
```
2. A web page will open in the browser. Let it load and then go back to the terminal.
3. Login by using your phone number. **!!!Bot tokens won't work!!!**
4. Enjoy!


---
> README written by [L4zzur](https://github.com/L4zzur) for his own modified version of tgbiofy.




