python .\main.py && `
pandoc --metadata title='NewsPhoto' --embed-resources --standalone --template='template/newsphoto.html5' --css sources/styles/index.css sources/index.md --output sources/index.html && `
python .\browser-autotest.py
