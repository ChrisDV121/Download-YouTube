from pytube import YouTube

link = input("Digite  seu url:")

try:
    yt: YouTube = YouTube(link)
except:
    print("Erro de download")

try:
    yt.streams.filter(progressive=True, file_extension="mp4").first().download()
except:
    print('Erro no download')
print("Download Completo!!")

