import subprocess, os

cwd = ('E:/Users/Test/Desktop/remix os/python_scraper/scraped/20200925042803 copy')


def deleteTS():
    global cwd
    os.chdir(cwd)
    for item in os.listdir():
        if item.endswith('.ts'):
            os.remove(os.path.join(cwd, item))

deleteTS()