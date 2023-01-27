# YoutubeDownloaderForStandardPeople

hello! this is my youtube downloader script, couple things to note:

it will always try and download up to 1080p as thats good for most things including download size, if you need to download 4k then im sorry but thats not an option atm since i made this for personal use but decided it would be good on github.

you WILL need to install pytube and ffmpeg-python to run this, im not sure how you do it on linux but if you have windows and pip installed you can simply type

```pip install pytube```

```pip install ffmpeg-python```

into a command prompt and that should work

(if python-ffmpeg or ffmpeg is installed it will interfere with the ffmpeg-python package so to be safe do a pip uninstall on both of those if you run into errors with ffmpeg).

I recommend running this in the latest version of python (3.11 as of writing) since i had issues with it working in older versions, and make sure you run it in the default python IDE or console, PyCharm or VScode may not work (at least in my experience).

oh and also this is pretty important, if you dont have ffmpeg already installed in your PATH on your computer you will need to include the exe file in the same working directory, you can download it from https://ffmpeg.org/ i literally cannot include it for you the exe is 100mb, github only lets me upload 25mb, dont worry its not hard, but if you dont plan to download 1080p videos you wont need this luckily.

and dont delete files specifically the ones called audio and video if they appear in the folder (its literally the audio and video of your video before its slapped together using ffmpeg so leave em alone lol).

the finished video/audio will automatically just be dumped into the same place the script is in, so because it comes in the folder if you run it in there it will just output the finished video in there (which is fine but if you REALLY want to have it spit it somewhere else then look for all the code parts that look like ```"./{0}.mp4".format(title)``` and for all of them (there should only be 3) change ./ to your desired filepath, for example for desktop it will look something like ```C:/Users/YourProfileName/Desktop/{0}.mp4```).

i recommend leaving it in its own folder for safety reasons, otherwise anything called video or audio in the same working directory it risks overwriting or deleting (it has no safe guards or typical error handling it doesnt even work sometimes) but if you leave it in its folder and run it then all will be good.

but yeah with all of that said enjoy, btw it can only download videos no shorts but audio and video is enough for general use
