@echo off
echo PUSH TIME IS %date% %time%
git status
git add .
git commit -m "commit at %date% %time%."
git push
exit