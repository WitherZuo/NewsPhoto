pandoc --metadata title="thenews" --standalone --css ref/index.css news.md --output index.html
browser-sync start --server "G:\NewsPhoto" --config bs-config.js