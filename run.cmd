pandoc --metadata title="thenews" --standalone --css index.css news.md --output index.html
browser-sync start --server "G:\NewsPhoto" --config bs-config.js