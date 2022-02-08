# git常用指令

### 删除远程分支branch1
```
git push origin --delete branch1
```

### 删除远程tag
```
git push origin --delete branch1
```

### 将本地分支跟远程分支建立关联
```
git branch --set-upstream-to=origin/v1.12 v1.12
```

### 修改git远程仓库地址
```
  ## 查看旧的gitlab仓库的remote url
  git remote -v 
  origin  ssh://git@119.3.60.230:1622/hardware/<your project>.git (fetch)
    origin  ssh://git@119.3.60.230:1622/hardware/<your project>.git (push)
  ## 更改新的URL。注意，项目名称后面不要带后缀".git"

  git remote set-url origin ssh://<your name>@122.112.250.28:29418/android/<your project>


```