pandoc --metadata title="thenews" --standalone --self-contained --css index.css news.md --output index.html
browser-sync start --server --config bs-config.js