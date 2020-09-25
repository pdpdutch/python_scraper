#!/bin/bash
githubfolder='/mnt/e/Users/Test/Desktop/remix os/python_scraper/scraped'
cd "$githubfolder"
stackfolder="/mnt/c/Users/Test/stack/compilations"
allMp4=$(find . -iname "*.mp4" -print)
echo "$allMp4"
for mp4 in ${allMp4[@]}; do
    from="$(pwd)${mp4:1}"
    to="$stackfolder${mp4:1:15}${mp4:25}"
    sudo mv "$from" "$to" -f
done

sudo rm -rf 
