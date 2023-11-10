from pytube import Youtube

link = input("Link Aqui:")
video = Youtube(link)
stream = video.streams.get_highest_resolution()
stream.download()