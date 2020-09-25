<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import sys
import asyncio
import random
import string
import json,time
import requests
from os import mkdir, chdir, listdir, path, getcwd
import os
import subprocess
import sys
from datetime import datetime as D


def getHarFile():
    files = listdir()
    cwd = getcwd()
    for file in files:
        if '.har' in file:
            return file


HAR_FILE = getHarFile()
HOME_DIR = getcwd()
now = 0
cwd = ""

print(HAR_FILE)


def getURLs():
    URLs = []
    print(getcwd())
    print(listdir())
    with open(HAR_FILE, 'r', errors='ignore') as f:
        data = {}
        data = json.loads(f.read())
        entries = data['log']['entries']
        for entry in entries:
            url = entry['request']['url']
            if '.ts' in url and 'https://' in url:
                URLs.append(url)
    return URLs


def randString(length): return ''.join(random.choice(
    string.ascii_letters + string.digits) for i in range(length))


def setup():
    global now
    if not 'scraped' in listdir():
        mkdir('scraped')
    chdir('scraped')

    now = ((D.now().strftime("%Y%m%d%H%M%S")))
    # now = str(20200925030822)
    try:
        mkdir(now)
    except:
        pass
    chdir(now)

    return print("Ready to start downloading")


def writeTS(url, counter):
    local_filename = str(counter).zfill(5) + '-' + randString(5) + '.ts'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


async def writeFiles():
    URLs = getURLs()
    urlListLen = len(URLs)
    counter = 0
    setup()
    for url in URLs:
        writeTS(url, counter)
        counter += 1
        print(f'{counter}/{urlListLen} - {round(counter / urlListLen * 100, 2)}%')
    print('Done Downloading')
    # return await mergeFiles()


def deleteTS():
    global cwd
    os.chdir(cwd)
    os.remove(os.path.join(cwd, 'mylist.txt'))
    for item in os.listdir():
        if item.endswith('.ts'):
            os.remove(os.path.join(cwd, item))


async def mergeFiles():
    print("Start merging")
    global cwd
    cwd = getcwd()
    print(cwd)

    os.chdir(cwd)

    cmd1 = r"(for %i in (*.ts) do @echo file '%i') > mylist.txt"
    cmd2 = r"echo Starting ffmpeg conversion"
    cmd3 = r"ffmpeg -f concat -safe 0 -i mylist.txt -c copy Combined.mp4"

    proc1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
    proc1.communicate()
    proc2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
    proc2.communicate()
    time.sleep(3)
    proc3 = subprocess.Popen(cmd3, stdout=subprocess.PIPE, shell=True)
    proc3.communicate()

    deleteTS()

    print("Removed ts")

    print('Done')


async def main():
    await writeFiles()
    await mergeFiles()
    chdir(HOME_DIR)
=======
=======
>>>>>>> parent of 24ae7d8... first version done
=======
>>>>>>> parent of 24ae7d8... first version done
import sys, requests, random, string,json
from os import mkdir, chdir,listdir

getHarFile = lambda: listdir()

HAR_FILE = getHarFile()

print(HAR_FILE)

def getURLs():
    URLs = []
    with open('members.adulttime.com.har', 'r', errors='ignore') as f:
      data = {}
      data = json.loads(f.read())
      entries = data['log']['entries']
      for entry in entries:
        url = entry['request']['url']
        if '.ts' in url and 'https://' in url:
          URLs.append(url)
    return URLs

      
randString=lambda length:''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

def setup():




def writeTS(url, counter):
  local_filename = counter + '-' + randString(5) + '.ts'
  with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
  return local_filename

def writeFiles():
  URLs = getURLs()
  counter = 0
  for url in URLs:
    writeTS(url, counter)
    counter += 1
    print(counter)
  print('Done')

def main():
  return 0

<<<<<<< HEAD
<<<<<<< HEAD
main()
>>>>>>> parent of 24ae7d8... first version done
=======
main()
>>>>>>> parent of 24ae7d8... first version done
=======
main()
>>>>>>> parent of 24ae7d8... first version done
