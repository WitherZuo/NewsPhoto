# Get current date and time
$current_datetime = Get-Date -UFormat '%Y%m%d-%H%M%S'

# Input commit text
Write-Host $current_datetime
$commit = Read-Host 'PLEASE ENTER COMMIT INFO'
Write-Output $commit

# Check files that will be uploaded
git status
git add -A
git status

# Ask question
$answer = Read-Host 'Do you want to sign commits and tags with GPG key? [Y/n]'

if ($answer -eq 'Y' -or $answer -eq 'y') {
    Write-Host "Signing commits and tags with GPG key."

    # Commit these files to origin/master, and create a new tag, with key.
    git commit -S -m "$commit"
    git tag -s -a NewsPhoto-$current_datetime -m "NewsPhoto: $current_datetime"
}
elseif ($answer -eq 'N' -or $answer -eq 'n') {
    Write-Host "Don't sign commits and tags with GPG key."

    # Commit these files to origin/master, and create a new tag.
    git commit -m "$commit"
    git tag -a NewsPhoto-$current_datetime -m "NewsPhoto: $current_datetime"
}
else {
    Write-Host "Invalid input value, dont't sign anything."

    # Commit these files to origin/master, and create a new tag.
    git commit -m "$commit"
    git tag -a NewsPhoto-$current_datetime -m "NewsPhoto: $current_datetime"
}

# Upload all commits and tags
git push origin master
git push origin NewsPhoto-$current_datetime