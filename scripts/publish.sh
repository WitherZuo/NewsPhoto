# 请注意：此发布脚本仅适用于主分支！

# 输入提交信息
read -r -p "请输入提交信息 / COMMIT INFO：" commit
echo $commit

# 检查和添加需要推送的文件
git status
git add -A
git status

# 提交暂存区文件
git commit -m "$commit"

# 推送到存储库
git push origin master
