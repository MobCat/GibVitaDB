#rinnegatamante.it/vitadb Dumper
#Programed by MobCat
#Don't ask why or question my motives, i'm not on anyones side just gib rom
#Also thanks to spaz for the help <3, idk if he wants to be crededited soo spaz is all you get..
#
#2020/01/02

import json
import os
import sys
import requests
import logging

logging.getLogger().setLevel(logging.WARNING )
#logging.getLogger().setLevel(logging.INFO )

logging.warn('Gib all Homebrews from VitaDB meow')
#Init setup for folder
os.mkdir('Homebrews')
os.mkdir('Plugins')
os.mkdir('PC Tools')

#Download latest json from vitadb
logging.warn('Loading Homebrews JSON file')
r = requests.get("http://rinnegatamante.it/vitadb/list_hbs_json.php")
f = open("VitaDBHomebrews.json", "wb")
f.write(r.content)
f.close()

#load said latest json into our script
with open('VitaDBHomebrews.json', 'r') as f:
    distros_dict = json.load(f)
    
for distro in distros_dict:
    #make new dir for each game
    #and check if dir is already there
    if not os.path.exists('Homebrews/'+ distro['name']): # should only create a new folder if none exist, not if one does exist
        logging.warn('Making new folder for '+ distro['name'])
        os.mkdir('Homebrews/'+ distro['name'])
    else: # else shouldn't be indented
        logging.error('ERROR: Folder already exists! Please remove the '+ distro['name']+ ' folder and run HomebrewDump.py again to update this game folder')

    #Make a new info.txt in each game folder
    sys.stdout=open('Homebrews/'+ distro['name']+"/info.txt","w")
    
    
    #Print game info from json
    logging.warn('Saving '+ distro['name']+ ' metadata txt')
    print('Name: '+ distro['name'])
    print('Icon: '+ 'https://rinnegatamante.it/vitadb/icons/'+ distro['icon'])
    print('Version: '+ distro['version'])
    print('Author: '+ distro['author'])
    print('Type: '+ distro['type'])
    print('Description: '+ distro['description'])
    print('ID: '+ distro['id'])
    print('Data: '+ distro['data'])
    print('Date: '+ distro['date'])
    print('TitleID: '+ distro['titleid'])
    
    #Don't set HTTP string if no screenshot in json
    if distro['screenshots'] == "":
        print('Screenshots: ')
    else:
        print('Screenshots: '+ 'https://vitadb.rinnegatamante.it/'+ distro['screenshots'])
    
    print('Long Description: '+ distro['long_description'])
    print('Downloads: '+ distro['downloads'])
    print('Status: '+ distro['status'])
    print('Source: '+ distro['source'])
    print('Release Page: '+ distro['release_page'])
    print('Trailer: '+ distro['trailer'])
    print('Size: '+ distro['size'])
    print('Data Size: '+ distro['data_size'])
    print('Download URL: '+ distro['url'])
    
    #Save print info and close txt file
    sys.stdout.close()
    
    #Download game (v.1.0).pkg
    logging.warn('Downloading '+ distro['name']+ ' ('+ distro['version']+ ')'+ '.pkg')
    r = requests.get(distro['url'])
    f = open('Homebrews/'+ distro['name']+'/'+distro['name']+ ' ('+ distro['version']+ ')'+ '.pkg', 'wb')
    f.write(r.content)
    f.close()
    
    #Download data.zip file if there is any to download but dont rename the data
    #But idk how to download it and save to a difrent dir with out renaming it or doing some os.move shit soo yeah this will has to do
    #may also try if distro['data'] == ".zip":
    #and gib error for non standed url.. soo if someone uploads data to gdrive or mega..
    if distro['data'] == "":
        logging.info('No data to download, moving on')
    else:
        logging.warn('Downloading '+ distro['name']+ ' data zip')
        r = requests.get(distro['data'])
        f = open('Homebrews/'+ distro['name']+'/'+distro['name']+ ' ('+ distro['version']+ ')'+ '.zip', 'wb')
        #f = open('Homebrews/'+ distro['name']+ '/'+ distro['data'], 'wb')
        f.write(r.content)
        f.close()
    
    #Download icon.png
    logging.warn('Downloading '+ distro['name']+ ' icon.png')
    r = requests.get('https://rinnegatamante.it/vitadb/icons/'+ distro['icon'])
    f = open('Homebrews/'+ distro['name']+'/icon.png', 'wb')
    f.write(r.content)
    f.close()
    
    #Download screebshots into a screebshots folder if there are any
    #I wanted to just save it all in the one folder but the json comes preformatted with a screenshots/ dir -__-'
    #If screenshots string contains multibel screenshots seprated by ; then make a list of them and download each of them one at a time
    if ';' in distro['screenshots']:
        logging.info('No, fuck your ; im out')
        #make new folder for screenshot because the stupid string comes preformatted with a folder so I has to use said folder
        os.mkdir('Homebrews/'+ distro['name']+'/screenshots')
        
        #make list out of string, make new line in list at everey ;
        bslst = distro['screenshots'].split(';')
        scrcnt = 0
        for lnk in bslst:
            logging.warn('Downloading '+ distro['name']+ ' Screenshot '+ str(scrcnt))
            r = requests.get('https://vitadb.rinnegatamante.it/'+ lnk)
            f = open('Homebrews/'+ distro['name']+ '/'+ lnk, 'wb')
            f.write(r.content)
            f.close()
            scrcnt = scrcnt + 1
    
    #If screenshots string only has one screenshot in it then only download that one screenshot.. no need for stupid split list
    elif distro['screenshots'] != "":
        logging.warn('Downloading '+ distro['name']+ ' Screenshot')
        os.mkdir('Homebrews/'+ distro['name']+'/screenshots')
        r = requests.get('https://vitadb.rinnegatamante.it/'+ distro['screenshots'])
        f = open('Homebrews/'+ distro['name']+ '/'+ distro['screenshots'], 'wb')
        f.write(r.content)
        f.close()
    #if no screenshot then no download anything...
    else:
        logging.info('No Screenshots to save...')
        
    scrcnt = 0
    logging.warn('OK')
    
#Clean up
os.remove('VitaDBHomebrews.json')


logging.warn('Gib all Plugins from VitaDB meow')
#From here on out is just going to copy past of the Homebrew script
#I could just work out how to plug difrent JSON files into first script and set the print metadata func
#acordleing but meh...

#Download latest json from vitadb
logging.warn('Loading Plugins JSON file')
r = requests.get("http://rinnegatamante.it/vitadb/list_plugins_json.php")
f = open("VitaDBPlugins.json", "wb")
f.write(r.content)
f.close()

#load said latest json into our script
with open('VitaDBPlugins.json', 'r') as f:
    distros_dict = json.load(f)
    
for distro in distros_dict:
    #make new dir for each game
    #and check if dir is already there
    if not os.path.exists('Plugins/'+ distro['name']): # should only create a new folder if none exist, not if one does exist
        logging.warn('Making new folder for '+ distro['name'])
        os.mkdir('Plugins/'+ distro['name'])
    else: # else shouldn't be indented
        logging.error('ERROR: Folder already exists! Please remove the '+ distro['name']+ ' folder and run HomebrewDump.py again to update this game folder')

    #Make a new info.txt in each game folder
    sys.stdout=open('Plugins/'+ distro['name']+"/info.txt","w")
   
       #Print plugin info from json
    logging.warn('Saving '+ distro['name']+ ' metadata txt')
    print('Name: '+ distro['name'])
    print('Version: '+ distro['version'])
    print('Author: '+ distro['author'])
    print('Description: '+ distro['description'])
    print('ID: '+ distro['id'])
    print('Date: '+ distro['date'])
    
    #Don't set HTTP string if no screenshot in json
    if distro['screenshots'] == "":
        print('Screenshots: ')
    else:
        print('Screenshots: '+ 'https://vitadb.rinnegatamante.it/'+ distro['screenshots'])
    
    print('Long Description: '+ distro['long_description'])
    print('Downloads: '+ distro['downloads'])
    print('Status: '+ distro['status'])
    print('Source: '+ distro['source'])
    print('Release Page: '+ distro['release_page'])
    print('Trailer: '+ distro['trailer'])
    print('Size: '+ distro['size'])
    print('Data Size: '+ distro['data_size'])
    print('Download URL: '+ distro['url'])
    
    #Save print info and close txt file
    sys.stdout.close()
    
    #Download plugin (v.1.0).suprx
    logging.warn('Downloading '+ distro['name']+ ' ('+ distro['version']+ ')'+ '.suprx')
    r = requests.get(distro['url'])
    f = open('Plugins/'+ distro['name']+'/'+distro['name']+ ' ('+ distro['version']+ ')'+ '.suprx', 'wb')
    f.write(r.content)
    f.close()
    
    if ';' in distro['screenshots']:
        #make new folder for screenshot because the stupid string comes preformatted with a folder so I has to use said folder
        os.mkdir('Plugins/'+ distro['name']+'/screenshots')
        
        #make list out of string, make new line in list at everey ;
        bslst = distro['screenshots'].split(';')
        scrcnt = 0
        for lnk in bslst:
            logging.warn('Downloading '+ distro['name']+ ' Screenshot '+ str(scrcnt))
            r = requests.get('https://vitadb.rinnegatamante.it/'+ lnk)
            f = open('Plugins/'+ distro['name']+ '/'+ lnk, 'wb')
            f.write(r.content)
            f.close()
            scrcnt = scrcnt + 1
    
    #If screenshots string only has one screenshot in it then only download that one screenshot.. no need for stupid split list
    elif distro['screenshots'] != "":
        logging.warn('Downloading '+ distro['name']+ ' Screenshot')
        os.mkdir('Plugins/'+ distro['name']+'/screenshots')
        r = requests.get('https://vitadb.rinnegatamante.it/'+ distro['screenshots'])
        f = open('Plugins/'+ distro['name']+ '/'+ distro['screenshots'], 'wb')
        f.write(r.content)
        f.close()
    #if no screenshot then no download anything...
    else:
        logging.info('No Screenshots to save...')
        
    scrcnt = 0
    logging.warn('OK')
    
#Clean up
os.remove('VitaDBPlugins.json')


logging.warn('Gib all PC Tools from VitaDB meow')

#Download latest json from vitadb
logging.warn('Loading PC Tools JSON file')
r = requests.get("http://rinnegatamante.it/vitadb/list_tools_json.php")
f = open("VitaDBPCTools.json", "wb")
f.write(r.content)
f.close()

#load said latest json into our script
with open('VitaDBPCTools.json', 'r') as f:
    distros_dict = json.load(f)
    
for distro in distros_dict:
    #make new dir for each game
    #and check if dir is already there
    if not os.path.exists('PC Tools/'+ distro['name']): # should only create a new folder if none exist, not if one does exist
        logging.warn('Making new folder for '+ distro['name'])
        os.mkdir('PC Tools/'+ distro['name'])
    else: # else shouldn't be indented
        logging.error('ERROR: Folder already exists! Please remove the '+ distro['name']+ ' folder and run HomebrewDump.py again to update this game folder')

    #Make a new info.txt in each game folder
    sys.stdout=open('PC Tools/'+ distro['name']+"/info.txt","w")
   
       #Print plugin info from json
    logging.warn('Saving '+ distro['name']+ ' metadata txt')
    print('Name: '+ distro['name'])
    print('Version: '+ distro['version'])
    print('Author: '+ distro['author'])
    print('Description: '+ distro['description'])
    print('ID: '+ distro['id'])
    print('Date: '+ distro['date'])
    
    #Don't set HTTP string if no screenshot in json
    if distro['screenshots'] == "":
        print('Screenshots: ')
    else:
        print('Screenshots: '+ 'https://vitadb.rinnegatamante.it/'+ distro['screenshots'])
    
    print('Long Description: '+ distro['long_description'])
    print('Downloads: '+ distro['downloads'])
    print('Status: '+ distro['status'])
    print('Source: '+ distro['source'])
    print('Release Page: '+ distro['release_page'])
    print('Trailer: '+ distro['trailer'])
    print('Size: '+ distro['size'])
    print('Data Size: '+ distro['data_size'])
    print('Download URL: '+ distro['url'])
    
    #Save print info and close txt file
    sys.stdout.close()
    
    #Download plugin (v.1.0).suprx
    logging.warn('Downloading '+ distro['name']+ ' ('+ distro['version']+ ')'+ '.suprx')
    r = requests.get(distro['url'])
    f = open('PC Tools/'+ distro['name']+'/'+distro['name']+ ' ('+ distro['version']+ ')'+ '.suprx', 'wb')
    f.write(r.content)
    f.close()
    
    if ';' in distro['screenshots']:
        #make new folder for screenshot because the stupid string comes preformatted with a folder so I has to use said folder
        os.mkdir('PC Tools/'+ distro['name']+'/screenshots')
        
        #make list out of string, make new line in list at everey ;
        bslst = distro['screenshots'].split(';')
        scrcnt = 0
        for lnk in bslst:
            logging.warn('Downloading '+ distro['name']+ ' Screenshot '+ str(scrcnt))
            r = requests.get('https://vitadb.rinnegatamante.it/'+ lnk)
            f = open('PC Tools/'+ distro['name']+ '/'+ lnk, 'wb')
            f.write(r.content)
            f.close()
            scrcnt = scrcnt + 1
    
    #If screenshots string only has one screenshot in it then only download that one screenshot.. no need for stupid split list
    elif distro['screenshots'] != "":
        logging.warn('Downloading '+ distro['name']+ ' Screenshot')
        os.mkdir('PC Tools/'+ distro['name']+'/screenshots')
        r = requests.get('https://vitadb.rinnegatamante.it/'+ distro['screenshots'])
        f = open('PC Tools/'+ distro['name']+ '/'+ distro['screenshots'], 'wb')
        f.write(r.content)
        f.close()
    #if no screenshot then no download anything...
    else:
        logging.info('No Screenshots to save...')
        
    scrcnt = 0
    logging.warn('OK')
    
#Clean up
os.remove('VitaDBPCTools.json')

logging.error('OK. All files and metadata should be dumped now from VitaDB ^__^/')
