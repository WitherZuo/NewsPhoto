$current_datetime = Get-Date -UFormat "%Y%m%d-%H%M%S"

Write-Host $current_datetime

git status
git add -A
git status
git commit -m "Update NewsPhoto."
git tag -a NewsPhoto-$current_datetime -m "NewsPhoto: $current_datetime"
git push origin NewsPhoto-$current_datetime
