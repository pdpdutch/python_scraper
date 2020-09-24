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

main()