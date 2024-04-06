python .\main.py && `
pandoc --metadata title='NewsPhoto' --embed-resources --standalone --css sources/styles/index.css sources/index.md --output outputs/index.html && `
python .\save-as-image.py
