## Description
* The purpose of the program is to automatically parse the .ssh/config file and resolve the host
* Click on the header to sort
* Clicking on a line will copy the corresponding ssh your_host_config to the clipboard.
* TODO: right-click, will Term run ssh your_host_config, not implemented, for right-click, can automatically open term and run ssh your_host_config

## Features
* In the .ssh/config file, I added the tags #tags, #group #color.
* group is the group in the first column
* color is used to mark the color of that line
* tags are used to mark some auxiliary information

## Initial development intention
* The fields involved in the search, 'Group', 'Host', 'tags', 'Hostname', 'color' should all be included to match.
* The original intention of writing this software is because I have too many hosts in the config file, and every time I want to find a host, I have to think about what I wrote at the beginning, which is very troublesome. Then I switched to SecureCRT, which is not powerful enough for server management and retrieval, but I don't know how to get it, so I've been settling for it.
* One day I saw shuttle, where the menu bar is customized, the menu bar groups itself, custom commands, it feels quite convenient. But this program has a shortcoming, is that in addition to edit once ssh/config, also have to edit once shuttle configuration file.
* So I wanted to write a tool myself. I've never done it, but I took my son to play with it during the summer and taught him to practice, and he was so sleepy when he saw it, so I wrote it myself.

## Additional notes
* Netizen provided two good ideas.
* nightwitch a one-line command thing `ssh $(awk "/^Host \w/{print \$2}" ~/.ssh/config | fzf)`
* `ssh config editor` https://hejki.org/ssheditor/
* After reading your suggestions, my needs, is that host a lot, and sometimes can not completely remember what the keywords of the host, so need to need some additional information, tags is what I use to add information, host is niit, tags is Nanjing Industrial Vocational University, may be after a period of time, I can only think of the occupation two words.
## Update Description
* 20220630v2 Left-click to double-click now
* 20220630v1 After click copy, window title will prompt the copy command.

## Thanks to 
* Thanks to tkinterHelper, otherwise it wouldn't have been done so quickly.

Translated with www.DeepL.com/Translator (free version)

## ??????
* ????????????????????????????????? .ssh/config?????????????????? host
* ?????? ????????? ????????????
* ???????????? ?????????????????? ssh your_host_config ???????????????
* TODO: ?????????????????? Term ????????? ssh your_host_config ?????????????????????????????????????????????????????? term ?????????ssh your_host_config

## ??????
* .ssh/config ???????????????????????? #tags ???#group #color ???????????????
* group ????????????????????????
* color ??????????????????????????????
* tags ??????????????????????????????

## ????????????
* ????????????????????????'Group', 'Host','tags', 'Hostname','color' ??????????????????????????????
* ?????????????????????????????????????????? config ???????????? host ?????????????????????????????????????????????????????????????????????????????????????????????????????? SecureCRT ?????????????????????????????????????????????????????????????????????????????????????????????????????????
* ??????????????? shuttle ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? ssh/config ????????????????????? shuttle ??????????????????
* ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

## ????????????
* ??????????????????????????????????????????
* nightwitch ??????????????????  `ssh $(awk "/^Host \w/{print \$2}" ~/.ssh/config | fzf)`
* `ssh config editor` https://hejki.org/ssheditor/
* ?????????????????????????????????????????? host ?????????????????????????????????????????? host ???????????????????????????????????????????????????????????????tags ????????????????????????????????????host ??? niit ???tags ?????????????????????????????????????????????????????????????????????????????? ?????? ??????????????????
## ????????????
* 20220630v2 ????????????????????????
* 20220630v1 ??????????????????window???title????????????????????????

## ?????? 
* ??????tkinterHelper ?????????????????????????????????