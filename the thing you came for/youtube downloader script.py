#importing packages
from pytube import YouTube, helpers
import ffmpeg
import os

#defining awesome percentage function for callback usage
def download_percentage(chunk, file_handler, bytes_remaining):
    try:
        print('{0}% done...'.format(round((1 - bytes_remaining / video.filesize) * 100, 3)))
    except NameError:
        print('{0}% done...'.format(round((1 - bytes_remaining / audio.filesize) * 100, 3)))

#loop so you dont have to restart the program, handy for downloading multiple videos back to back
while True:
    # url input from user
    URL = str(input("Enter the URL of the video you want to download or nothing to exit: \n>> "))
    if not bool(URL): #way to exit out of program
        break
    yt = YouTube(URL, on_progress_callback=download_percentage) #creating YouTube object with the progress callback
    yt.check_availability() #checks if its actually a real link before progressing if not then error
    check = True #used later to decide whether or not to do ffmpeg
    title = helpers.safe_filename(yt.title) #windows safe youtube title filename
    ask = bool(input("type literally anything here if you want just the audio "))
    if ask:
        audio = yt.streams.get_audio_only() #finding audio stream and displaying the bitrate, typically its 128kbps
        print("found a audio stream! its bitrate is {0}".format(audio.abr))
    elif not ask:
        video = yt.streams.filter(file_extension="mp4", res="1080p", adaptive=True).first() #grabs 1080p stream
        if video is None: #if video is 720p or less this happens
            video = yt.streams.filter(file_extension="mp4").get_highest_resolution() #gets highest possible resolution stream if 1080p doesn't exist
            check = False
        if check:
            audio = yt.streams.get_audio_only() #grabs highest quality audio stream available for later
        print("found a video stream! its quality is {0} {1}fps".format(video.resolution, video.fps))
    #download the file
    if not ask:
        if check: #main downloading part
            print("downloading {0}mb of audio".format(audio.filesize_mb))
            audio.download(output_path=".", filename="audio.mp3")
            print("downloading {0}mb of video".format(video.filesize_mb))
            video.download(output_path=".", filename="video.mp4")
    elif ask: #downloading audio if user wants just audio
        print("downloading {0}mb of audio".format(audio.filesize_mb))
        audio.download(output_path="./", filename="{0}.mp3".format(title)) #sticks it in same directory

    #put the video and audio together
    if not ask and check:
        input_video = ffmpeg.input("./video.mp4")
        input_audio = ffmpeg.input('./audio.mp3')
        print("combining audio and video...")
        ffmpeg.output(input_video.video, input_audio.audio, "./{0}.mp4".format(title),
                      codec='copy').overwrite_output().run(quiet=True) #the main thing that puts it together and outputs it into same directory
        os.remove("./audio.mp3")
        os.remove("./video.mp4") #cleaning up
    if not check:
        print("downloading {0}mb of video".format(video.filesize_mb))
        video.download(output_path="./", filename="{0}.mp4".format(title)) #720p and under video downloading and outputting, the reason this doesnt use ffmpeg is because audio and video are shipped together for 720p and under videos
    #all done
    print(yt.title + " has been successfully downloaded.")
