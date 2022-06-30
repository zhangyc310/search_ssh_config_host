
## 说明
* 程序的作用是，自动解析 .ssh/config文件，解析出 host
* 单击 标题头 可以排序
* 单击行， 会复制相应的 ssh your_host_config 到剪贴板；
* TODO: 右键单击，会 Term 中运行 ssh your_host_config ，未实现，用于右键单击后，能自动打开 term 并运行ssh your_host_config

## 特色
* .ssh/config 文件中，我增加了 #tags 、#group #color 三个标签。
* group 就是第一列的分组
* color 用于标定那一行的颜色
* tags 用于标志一些辅助信息

## 开发初衷
* 参与检索的字段，'Group', 'Host','tags', 'Hostname','color' 都要包含都可以匹配。
* 写这个软件的初衷，是因为自己 config 文件里面 host 太多了，每次要找一个主机的时候，要想当初的写了啥，非常麻烦。后来改用 SecureCRT ，里面的服务器管理，检索功能不够强大，但也不知道怎么弄，就一直将就着。
* 有一天看到 shuttle ，菜单栏那里自定义，菜单栏自己分组，自定义命令，感觉挺方便的。但这个方案有个不足，就是除了要编辑一次 ssh/config ，还要编辑一次 shuttle 的配置文件。
* 于是想自己写一个工具。一直没有动手，暑假带儿子玩，教他练手，他一看到这个就困得不行，于是还是我自己写吧。

## 补充说明
* 网友提供了了两个很好的思路：
* nightwitch 一行指令的事  `ssh $(awk "/^Host \w/{print \$2}" ~/.ssh/config | fzf)`
* `ssh config editor` https://hejki.org/ssheditor/
* 看了你们的建议，我的需求，是 host 很多，而有时候并不能完全记得 host 的关键词是什么，所以需要需要一些补充信息，tags 就是是我用来补充信息的，host 是 niit ，tags 是南京工业职业技术大学，可能一段时间之后，我只想得起 职业 两个字。。。
## 更新说明
* 20220630v2 左键单击改双击了
* 20220630v1 单击复制后，window的title会提示复制的命令

## 感谢 
* 感谢tkinterHelper ，否则还没这么快完成。