time=$(date "+%Y-%m-%d %H:%M:%S")
echo PUSH TIME IS "${time}"
git status
git add .
git commit -m "commit at '${time}'."
git push
exit
