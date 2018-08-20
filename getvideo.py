from pytube import YouTube

def download(link,name):
    test = YouTube(link)
    test_stream = test.streams.filter(file_extension='mp4').first()
    test_stream.download()
    os.rename(test_stream.default_filename, '{}.mp4'.format(name))

download(https://youtu.be/ZJuxdR0KH-s,'Wario')
download(https://youtu.be/lXMJt5PP3kM,'Mario')