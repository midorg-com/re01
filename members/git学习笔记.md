# 如何在vscode上使用git学习笔记
## 基本操作
<font size=5/>

- pwd：显示当前终端会话所在的目录位置
- ls(lsit file):显示当前目录下的所有文件名
- cd:切换目录 cd .. 切换到上一级 cd xx 是下一级
- git version 查询版本（确认是否已经安装git）
- git config --global user.name "用户名"  
git config --global user.email "邮箱" 
两者都是第一次设置完就行了
- git init 初始化当前的文件夹，创建.git隐藏文件夹，文件夹内会保存每一个git版本记录和变化
- git add . 提交所有的文件， git add xxx 提交某一个文件。其实是把他放入暂存区
- git commit -m "提交说明"  （到这一步就代表了提交完成，git会报错本次提交的信息）
- git log  显示当前的提交信息
- 新增插件，git history diff， 可以看到所有的历史提交和文件前后区别等（右键，GitHD:View File History)
- 回退版本 git reset --hard xxx(commit ID) 除了hard 还有mixed 等模式
- 不同版本切换，用branch分支
## 参与开源项目
 1. 开源项目地址，点击fork，生成自己的仓库
 2. 使用git clone 下载到本地
 3. git remote -v 发现只有自己的仓库 
 4. 回到上游仓库，采用git remote add upstream 链接添加上游代码库，再remote就可以发现上游仓库
 5. 如果需要给别人加功能，可以先创建一个分支 git checkout -b kwc 创建并切换到kwc这个分支
 6. 
 