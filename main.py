from tkinter import *
from tkinter.ttk import *
import pyperclip3

# 20220630v2 左键单击改双击了
# 20220630v1 单击复制后，window的title会提示复制的命令
# 程序的作用是，自动解析 .ssh/config文件，
# tree 可以排序
# 单击会复制 ssh your_host_config 到剪贴板；
# 右键单击，会Term中运行 ssh your_host_config

class Win:
    def __init__(self):
        self.root = self.__win()
        self.tk_button_search_btn = self.__tk_button_search_btn()
        self.tk_input_search_content = self.__tk_input_search_content()
        self.tk_label_tip = self.__tk_label_tip()
        # self.tk_list_box_listbox = self.__tk_list_box_listbox()
        self.ttk_tree_content = self.__ttk_tree()
        results = self.getSSHConfg()
        self.updateHost2Tree(results)
        self.ttk_tree_content.bind('<Double-Button-1>', self.treeviewClick)
        self.ttk_tree_content.bind('<ButtonRelease-2>', self.treeviewDoubleClick)
        self.tk_button_search_btn.bind('<Button-1>', self.search_Host)
        self.tk_input_search_content.bind('<Key-Return>', self.search_Host)

    def __win(self):
        root = Tk()
        root.title("我是标题 ~ TkinterHelper")
        # 设置大小 居中展示
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False, height=False)
        return root

    def show(self):
        self.root.mainloop()

    def __tk_button_search_btn(self):
        btn = Button(self.root, text="检索")
        btn.place(x=290, y=20, width=50, height=24)

        return btn

    def __tk_input_search_content(self):
        ipt = Entry(self.root)
        ipt.place(x=120, y=20, width=150, height=24)
        return ipt

    def __tk_label_tip(self):
        label = Label(self.root,text="选择")
        label.place(x=40, y=20, width=50, height=24)
        return label

    def __tk_list_box_listbox(self):
        lb = Listbox(self.root)
        lb.insert(END, "列表框")
        lb.insert(END, "Python")
        lb.insert(END, "Tkinter Helper")
        lb.place(x=40, y=60, width=528, height=428)
        return lb

    def treeview_sort_column(self,tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: \
            self.treeview_sort_column(tv, col, not reverse))
    def __ttk_tree(self):
        columns = ('Group', 'Host','tags', 'Hostname')
        # tree = Treeview(self.root, columns=['1', '2', '3'], show='headings')
        # tree.column('1', width=70, anchor='center')
        # tree.column('2', width=70, anchor='center')
        # tree.column('3', width=100, anchor='center')
        #
        # tree.heading('1', text='Group')
        # tree.heading('2', text="Host")
        # tree.heading('3', text='Hostname')

        tree = Treeview(self.root,columns = columns,  show='headings')
        for col in columns:
            tree.heading(col, text=col, command=lambda _col=col:self.treeview_sort_column(tree, _col, False))

        # self.addHost2Tree(self)

        tree.grid()

        tree.place(x=40, y=60, width=528, height=428)
        return tree

    def updateHost2Tree(self,hostDatas):

        for rs in hostDatas:
            print(rs)
            third = ""
            if "Hostname" in rs:
                third = rs['Hostname']
            if "Port" in rs:
                third = third + ":" + rs['Port']

            tags=""
            if "tags" in rs:
                tags=rs['tags']
            group = 'Default'
            if "Group" in rs:
                group = rs['Group']
            li = [group, rs["Host"], tags, third]
            if "color" in rs:
                self.ttk_tree_content.insert('', 'end', values=li, tags = (rs['color'],))
                colors = rs['color'].split(",",1)
                self.ttk_tree_content.tag_configure(rs['color'], background=colors[0])
            else:
                self.ttk_tree_content.insert('', 'end', values=li)


    def clearTree(self):
        x = self.ttk_tree_content.get_children()
        for item in x:
            self.ttk_tree_content.delete(item)

    def print_contents(self, event):
        print("okkkkk")

    def getSSHConfg(self):
        f = open("/Users/zhangyingchun/.ssh/config")
        neirong = f.read()
        f.close();
        所有结果列表 = []
        所有段落 = neirong.split('\n\n', -1)
        i = 0;

        for 每个段落 in 所有段落:
            # 去除 .ssh/config 文件的第一段
            if i == 0:
                i = i + 1
                continue
            i = i + 1
            # print(i,dl)
            # print(hangs)
            每个段落的所有行 = 每个段落.split("\n", -1)
            #
            # print(" ========")
            每个段落的解析结果列表 = {}
            isUsefule = False
            for 每一行 in 每个段落的所有行:
                分割后元素列表 = 每一行.split(" ", 1)
                # 处理 Host、Hostname、Port、#color、#tags 这个5个元素
                # print("中间调试信息 Host hang：", 每一行)
                if 每一行.startswith("Host "):
                    # 必须有Host的段落才会保存到 所有结果列表
                    isUsefule = True
                    每个段落的解析结果列表["Host"] = 分割后元素列表[1]
                elif 每一行.startswith("Hostname"):
                    每个段落的解析结果列表["Hostname"] = 分割后元素列表[1]
                elif 每一行.startswith("Port"):

                    每个段落的解析结果列表["Port"] = 分割后元素列表[1]
                elif 每一行.startswith("#tags"):
                    每个段落的解析结果列表["tags"] = 分割后元素列表[1]
                elif 每一行.startswith("#color"):
                    每个段落的解析结果列表["color"] = 分割后元素列表[1]
                elif 每一行.startswith("#group"):
                    每个段落的解析结果列表["Group"] = 分割后元素列表[1]
                    print("Group::: ",分割后元素列表[1])
            # print(jieguo)
            if isUsefule:
                所有结果列表.append(每个段落的解析结果列表)
        return 所有结果列表

    def treeviewClick(self,event):  # 单击
        print('单击')
        for item in self.ttk_tree_content.selection():
            item_text =  self.ttk_tree_content.item(item, "values")
            print(item_text[1])  # 输出所选行的第一列的值
            pyperclip3.copy("ssh "+item_text[1])
            self.root.title("复制—— ssh " + item_text[1])

    def treeviewDoubleClick(self,event):  # 单击
        print('右键单击')
        for item in self.ttk_tree_content.selection():
            item_text =  self.ttk_tree_content.item(item, "values")
            print(item_text[1])  # 输出所选行的第一列的值
            pyperclip3.copy("ssh "+item_text[1])
            # self.root.title("复制—— ssh "+item_text[1])

    def search_Host(self ,event):
        所有结果列表2 = self.getSSHConfg()
        要查找的字符=  self.tk_input_search_content.get()
        print("要查找的字符: ",要查找的字符)
        rs=[]
        if 要查找的字符 == "0":
            rs = 所有结果列表
        else:
            for 单个结果 in 所有结果列表2:
                    # field 是 jieguo 这个dict 的 key，用jieguo[field]获取对应的value
                    find = False
                    for field in 单个结果:
                        if 单个结果[field].find(要查找的字符) > -1:
                            find=True
                            break
                    if find:
                        rs.append(单个结果)
        for search_rs in rs:
            print("ssh", search_rs["Host"], " \t,", search_rs)
        self.clearTree()
        self.updateHost2Tree(rs)

if __name__ == "__main__":
    win = Win()
    所有结果列表 = win.getSSHConfg()
    # TODO 绑定点击事件或其他逻辑处理
    win.show()
#

