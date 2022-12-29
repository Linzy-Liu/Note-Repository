# 1. Git的工作流

一图解：![git_command](git-command.jpg)
推荐看[这个博客](https://www.liaoxuefeng.com/wiki/896043488029600)

## 1.1 组成部分

* `WorkSpace`，即工作区，本地文件被建立、修改、删除的地方
* `Staging Area`，即暂存区，在文件被提交至本地仓库之前暂存的地方，就如同IO中的buffer一样
* `Local Repository`，即本地仓库，工作流程、提交后的文件在本地所存储的地方
* `Remote Repository`，即远程仓库，所有参与工作流程的人共有的仓库。在概念意义上，它是所有人共有的“本地”仓库；事实上，它存在于每个人的电脑之中。

`Git`作为分布式的文件管理系统，其分布式以及分布式的解决方式均体现在其层级分划之中。

## 1.2 基本操作

首先在一切开始之前，需要保证当前操作所在的环境是一个git仓库(git repository)
如果不在git仓库内，任何指令都无法进行。如果这个文件夹是一个git仓库，那么它应当有一个`.git`文件夹

**初始化**   
运用`git init`指令，创建`.git`目录。同时在`git config -- global`处设置`user.name`和`user.email`(这个信息是必要的，且以后的每次对git操作产生的记录都会包含这个个人信息)

**提交**   
它分为几个步骤，由上图可见，是：`git add`->`git commit`->`git push`，以下对三个步骤的作用稍作解释。
`git add` 将文件加入`Staging Area`中，将`Untracked files`加入到git所关注的文件列表之中。
`git commit` 意味着修改生效，将文件保存到了本地仓库中。
`git push` 将本地仓库的内容推到了远程仓库中。

**拉取**
基本上都是对应层级的逆操作：
`git pull` 将远程仓库的内容拉取到工作区
`git clone` \ `git fetch` 将远程仓库的内容同步到本地仓库
`git checkout` 将`Staging Area`中的指定文件修改内容撤销。

# Appendix 操作命令

## `Linux`操作命令

* `cd` Change directory
* `cd ..` Go back to parent directory
* `pwd` Print working directory
* `ls` List directory content
* `mkdir` Make directory 
* `touch` Make new file
* `mv` Move something to somewhere. For example, `mv test.txt test`
* `rm` Remove something.
* `clear` Clear

Want to know more, consider [Here](https://www.runoob.com/linux/linux-command-manual.html)

## `Git`操作指令

参考[这个链接](https://www.runoob.com/note/56524)

