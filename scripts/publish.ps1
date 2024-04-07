# Input commit text
Write-Host $current_datetime
$commit = Read-Host 'PLEASE ENTER COMMIT INFO'
Write-Output $commit

# Check files that will be uploaded
git status
git add -A
git status

# Commit these files to origin/master, and create a new tag.
git commit -m "$commit"

# Upload all commits and tags
git push origin master
