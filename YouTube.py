
# Youtube Video Downloader
import os
from pytube import YouTube

def main():
    print("Welcome, this is the Youtube Video Downloader")
    userUrl = input("Paste Your Link ").strip()
    
    if not userUrl:
        print("Error! No link provided. Try again.")
        return
    
    try:
        yt = YouTube(userUrl)
    except Exception as e:
        print(f"Error: Unable to fetch video details. Check the URL.\nDetails: {e}")
        return
    
    print(f"Video title: {yt.title}")
    downloadPath = input("Iput path to your desired location: ").strip()
    
    if not os.path.isdir(downloadPath):
        print("Error: Specified path dont exist. Try again.")
        return
    
    try:
        print("Geting best resoluion ......................")
        videoStream = yt.streams.get_highest_resolution()
        print(f"Downloading {yt.title}")
        
        videoStream.download(output_path=downloadPath)
        print(f"Download complete! Saved to: {os.path.join(downloadPath, yt.title)}")
        
    except Exception as e:
        print(f"Error: Download Failed.!\nDetails: {e}")

if __name__ == "__main__":
    main()