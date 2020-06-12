from pytube import *

yt = YouTube(str(input("Enter the video link: ")))
videos = yt.streams.all()

s = 1
for v in videos:
    print(str(s)+". "+str(v))
    s += 1

n = int(input("Enter the number of the video: "))

vid = videos[n-1]
print ("downloading...!!!")
destination = 'E:\\python\\Django videos\\'
vid.download(destination)


print("Video has been successfully downloaded")


# import easygui

# easygui.msgbox("Hey Gokul...!!!!Download completed", title="Notification")

#########################

# from pytube import *
#
# yt = YouTube(str(input("Enter the video link: ")))
# videos = yt.captions
# print (videos)
# s = 1
# for v in videos:
#     print(str(s)+". "+str(v))
#     s += 1
#
# #n = int(input("Enter the number of the video: "))
# # n=1
# # vid = videos[n-1]
# # print ("downloading...!!!")
# # destination = 'E:\\'
# # vid.download(destination)
#
#
# print("Video has been successfully downloaded")