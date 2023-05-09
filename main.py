from pytube import exceptions, Playlist, YouTube
import os
from pathlib import Path


def youtube2mp3(url, outdir):
    # url input from user
    yt = YouTube(url)

    try:
        # Extract audio with 160kbps quality from video
        try:
            video = yt.streams.filter(abr='160kbps').last()
        except KeyError:
            print("ERROR: KeyError on bitrate")
            return
        # Download file
        out_file = video.download(output_path=outdir)
        base, ext = os.path.splitext(out_file)
        new_file = Path(f'{base}.mp3')
        try:
            os.rename(out_file, new_file)
        except FileExistsError:
            print("ERROR: file already in dir")
        # Check success of download
        if new_file.exists():
            print(f'{yt.title} has been successfully downloaded.')
        else:
            print(f'ERROR: {yt.title}could not be downloaded!')
    except exceptions.AgeRestrictedError:
        print("ERROR: Age Restriction")
        print(f"{url} - is age restricted")


def downloadPlaylist():
    playlist_url = input("Please type in the youtube playlist link: ")
    playlist_urls = Playlist(playlist_url)
    for url in playlist_urls:
        print(f"\n[{playlist_urls.index(url)}/{len(playlist_urls)}]")
        youtube2mp3(url, os.getcwd() + "/songs")
    print("\nDONE, please check your /songs folder where you ran the program.")


downloadPlaylist()
