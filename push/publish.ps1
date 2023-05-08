# Get current date and time
$current_datetime = Get-Date -UFormat "%Y%m%d-%H%M%S"

# Input commit text
Write-Host $current_datetime
$commit = Read-Host "PLEASE ENTER COMMIT INFO"
Write-Output $commit

# Check files that will be uploaded
git status
git add -A
git status

# Commit these files to origin/master
git commit -m "$commit"
git push origin master

# Tag and upload this tag
git tag -a NewsPhoto-$current_datetime -m "NewsPhoto: $current_datetime"
git push origin NewsPhoto-$current_datetime
