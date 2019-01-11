<center>
<img align="left" src="https://i.imgur.com/49xERdm.png">
<h1>Cakeday Scheduler</h1>
Never miss your Cakeday posts ever again
</center>
</br>


___
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Requirements and Setup](#requirements-and-setup)
* [Execution](#execution)
* [Contributing](#contributing)

## General info
What you are looking at is a simple script, made in honor of my first <b><a href="https://www.reddit.com/user/Tarasa24_CZE" target="_blank">Reddit</a> Cakeday</b>.

We all know that Cakeday is great way for earning karma, that's why we all prepare our dedicated posts beforehand. Why not to make our lives easier and have bot to post them for us?

The script execute itself at startup and it will close itself within milliseconds, if it is not your Cakeday.

But when your great day arise, you will be greeted with this cute ASCII image:

![top_notch_GUI](https://i.imgur.com/3zbQF9R.png)

## Technologies
Project is created with:
* <a href="https://github.com/praw-dev/praw" target="_blank">PRAW: The Python Reddit API Wrapper</a>
* <a href="https://www.text-image.com/convert/ascii.html" target="_blank">Image to ASCII converter</a>

## Requirements and Setup
As this is a Python project, you will obviously need the python itself plus one dependency.

➤ [Python](https://www.python.org/) 🐍

```
 $ pip install praw
```

In order for bot to post images on your behalf, you will need to register your own Reddit application over at <a href="https://www.reddit.com/prefs/apps" target="_blank">reddit.com/prefs/apps</a> (**Choose script as an application type** during the creation process).

<a href="https://github.com/reddit-archive/reddit/wiki/oauth2" target="_blank">When in doubt, use this guide</a>

And now add your obtained *client_id* and *client_secret*, along with your username and password, to the **config.json**:

```json
{
  "client_id": "FPLOvb-3_rWmF3x",
  "client_secret": "fMnfh0YndQ9f5bZF3BUi5oOn8mE",
  "password": "skpUP/08vTZ#NYA0JSQuiv+IrXCYNd1by.",
  "username": "Tarasa24_CZE"
}
```
>Values are randomly generated, you don't need to try them 🤞

## Execution
For the sake of running this script automatically at startup, place the `py/autorun.py` **shortcut** to the startup folder.
* Default for **Win10**: `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
* For every user: `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`

---
For the creation of a post order. Run `py/create_order.py`. You will be asked to fill following conditions:
 * Title of your posts
 * Subreddits name (alternatively use *u_NICKNAME* to post to your profile)
 * Your file URL (Due the limitation a the API, files must be already hosted elsewhere, i.e. <a href="https://imgur.com/upload" target="_blank">Imgur.com</a>)

Result will be placed to the `py/orders.json` file:
 ```json
[
      {
        "title": "Beep, boop, I am a bot. I posted all the images/gifs, as you requested. Happy Cakeday!",
        "subreddit": "u_Tarasa24_CZE",
        "url": "https://i.imgur.com/9IVURrH.gifv",
        "cakeday": [12, 1, 2019]
      }
]
 ```

## Contributing
Script itself uses couple calls, specific for the windows machines. Therefore unusable on Linux/Mac etc. If you fancy, redesigning this project for your favorite system, don't hesitate to fork.
