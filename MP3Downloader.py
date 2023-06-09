import datetime
import pytube
import os



#DICHIARAZIONE VARIABILI
print('/////////////////////\n')
print('//YT MP3 DOWNLOADER//\n')
print('/////////////////////\n\n')
confirm= False
yt=[]
counter=0

#LISTA CANZONI
while confirm == False:
    link = input('Inserisci il link del video:\n')
    yt.append(pytube.YouTube(link))
    counter=counter+1
    exitConfirm=input('Sono finite le canzoni?(Y/N):\n')
    if exitConfirm=='Y':
        confirm=True

path=input('Inserisci il percorso dove inserire il file:\n')

#DOWNLOAD
os.chdir(path)
for j in yt:
    j.streams.first().download()
    print('downloading...')


#FORMATTAZIONE NOME FILE E CONVERSIONE
filename=[]
for x in yt:
    filename.append(x.title.replace('\\', ''))
for z in filename:
    z=z.replace('/','')
    z=z.replace(':','')
    z=z.replace('*','')
    z=z.replace('?','')
    z=z.replace('\"','')
    z=z.replace('<','')
    z=z.replace('>','')
    z=z.replace('|','')
    os.rename((z+'.3gpp'),(z+'.mp3'))
    #os.remove((filename+'.3gpp'))
    print('File ottenuto: ',z)

print('////////////////////\n')
print('//FILE DOWNLOADED!//\n')
print('////////////////////\n\n')
