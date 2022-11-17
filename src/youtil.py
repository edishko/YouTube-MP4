# ---- ---- ---- ---- # Libaries #
from pytube import YouTube, Playlist
import glob
import os
import shutil

# ---- ---- ---- ---- # Class #
class Youtilities():

    def ytil_makedir(self, ytil_input_path, ytil_input_dirname, ytil_input_ext = ""): # dirmaker #
        # make dictionary for videos #
        ytil_dirpath = os.path.join(ytil_input_path + "/",ytil_input_dirname).strip(f".{ytil_input_ext}")
        if(os.path.exists(ytil_dirpath) == False): # check if directory exists #
            os.mkdir(ytil_dirpath, 0o666)

        return ytil_dirpath # return the path #

    def ytil_playlist(self,ytil_input,ytil_output): # turns playlist to mp4 #
        # open playlist #
        playlist = Playlist(ytil_input)
        
        output = self.ytil_makedir(ytil_output, playlist.title) # make a dir #
        
        print(f"\n| {playlist.title} | playlist started!\n")

        # for a video in a playlist #
        for video in playlist.videos:
            video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output)
            print(f"| {video.title} | video downloaded!")

    def ytil_video(self,ytil_input,ytil_output): # turns video to mp4 #
        YouTube(ytil_input.replace("/shorts/","/watch/")).streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download(ytil_output)
        print(f"\n| {ytil_input} | video downloaded!")

    def ytil(self, ytil_input_path, ytil_output_path):

        filepathlist = glob.glob(ytil_input_path + "/*.txt") # get file list #

        for filepath in filepathlist: # for each file in file list #

            print(f"\n| {os.path.basename(filepath)} | file started!")

            output = self.ytil_makedir(ytil_output_path,os.path.basename(filepath),"txt") # make outputpath and check for errors #
            
            # open file, get the linkset, close the file #
            file = open(filepath)
            linkset = [link.strip("\n") for link in file.readlines()] # define linkset
            file.close()

            for link in linkset: # makes all videos of a linkset

                if (link.find("/watch") != -1 or link.find("/watch") != -1):
                    self.ytil_video(link,output)
                    
                elif (link.find("/playlist?") != -1):
                    self.ytil_playlist(link,output)
                    print(f"\n| {Playlist(link).title} | playlist finished!")

            print(f"\n| {os.path.basename(filepath)} | file finished!")

Youtilities().ytil("dirpath/Input", "dirpath/Output") # replace dirpath with a path to this directory.