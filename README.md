# GibVitaDB
Very basic file dumper for https://vitadb.rinnegatamante.it/.<br />
Uses python3 to read the API JSON file from https://vitadb.rinnegatamante.it/#/api, passes the JSON and downloads all the files.<br />
Also saves metadeta like version number and discriptions from the JSON file into a info.txt file.<br />
Also also I know this thing contains a lot of jank and could be done better. Don't complain at me, make your own damn app then.<br />
Also also also I'm not on anyone's side here, I just gib roms....<br />

# 2020/05 Update
TL;DL to much BS and infighting. 
Cloudflare was applyed *site wide* to vitadb so my script can no longer auto generate the .json files from there api..
Right now there is no fix because I wrote this script really badley. You could remove the audo download and make the .json files bits from the script and then go to the api page, do the Cloudflare BS and then make the .json files by hand. If you don't remove the auto download bit from the script it will just replace the json files you put there..
IDK how to fix this script to work with Cloudflare sorry guys, Cloudflare is the bane of my existence.

# How to gib
Make a new folder called VitaDB on a drive that has more then 5GB of free space<br />
Download GibVitaDB.py to that new folder<br />
run python3 GibVitaDB.py<br />
profit ¯\\_(ツ)_/¯<br />

# ToDo
Make a download counter so you know how many files are left to download so it doesn't just say "OK"<br />
Fix data.zip download to save to homebrew folder without renaming the file and without doing os.move hackrey.<br />
Do some more checks to see if the script missed anything... But I think it gibs everething...<br />
