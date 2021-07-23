# usr/local/bin/python3.7
# -*-coding: utf-8 -*-
# Author: Felix
# FileName: linklist_to_leetcode2.py


# 节点类
class Student:

    def __init__(self, schnum, name, score):

        self.schnum = schnum
        self.name = name
        self.score = score
        self.next = None


# 链表类
class Link:
    # 链表类包含：头结点、尾节点、链表大小
    def __init__(self):

        self.head = Student(None, None, None)
        self.tail = self.head
        self.size = 1

    # 添加节点
    def add(self, schnum, name, score):

        stu = Student(schnum, name, score)  # 创建一个新节点
        self.tail.next = stu                # 尾节点的下一个节点为新节点
        self.tail = stu                     # 尾节点为新节点
        self.size = self.size + 1

    # 插入节点
    def insert(self, schnum, name, score, index):

        if index >= self.size:
            print('超出链表，请输入范围内的!')
        else:
            stu = self.head
            insert_stu = Student(schnum, name, score)
            for i in range(index-1):
                stu = stu.next
            insert_stu.next = stu.next
            stu.next = insert_stu
            self.size += 1

    # 删除节点
    def delete(self, index):
        if index >= self.size:
            print('超出链表，请输入范围内的!')
        else:
            stu = self.head
            for i in range(index-1):
                stu = stu.next
            temp = stu.next
            stu.next = temp.next
            self.size -= 1

    # 修改节点数据
    def change(self, schnum, name, score, index):
        if index >= self.size:
            print('超出链表，请输入范围内的!')
        else:
            stu = self.head
            for i in range(index):
                stu = stu.next
            stu.schnum = schnum
            stu.name = name
            stu.score = score

    # 返回指定节点数据
    def get_data(self, index):

        if index >= self.size:
            print('超出链表，请输入范围内的!')
        else:
            stu = self.head
            for i in range(index):
                stu = stu.next
            return [stu.schnum, stu.name, stu.score]

    # 返回链表大小
    def get_size(self):
        return self.size

    # 就地反转链表
    def jiudi_invert(self, head):

        dummy = Student(None, None, None)
        dummy.next = head
        prev = dummy.next
        pcur = prev.next

        i = 0
        while (pcur != None):           # 循环条件：直到尾节点结束
            prev.next = pcur.next       # prev连接下一次需要反转的节点
            pcur.next = dummy.next      # 反转
            dummy.next = pcur           # 纠正头节点的位置（将头节点向后移动一位）
            pcur = prev.next
            i += 1

        self.head = dummy.next
        print(i)


if __name__ == '__main__':

    link = Link()

    select = -1
    while select != 0:

        select = int(input('输入选择器，需数字: '))
        if select == 1:
            schnum = input('学号: ')
            name = input('姓名: ')
            score = input('成绩: ')
            link.add(schnum, name, score)
        if select == 2:
            schnum = input('学号: ')
            name = input('姓名: ')
            score = input('成绩: ')
            index = int(input('需插入位置: '))
            link.insert(schnum, name, score, index)
        if select == 3:
            index = int(input('需删除位置: '))
            link.delete(index)
        if select == 4:
            schnum = input('学号: ')
            name = input('姓名: ')
            score = input('成绩: ')
            index = int(input('需修改位置: '))
            link.change(schnum, name, score, index)
        elif select == 5:
            index = int(input('查看第几位同学信息: '))
            table_data = link.get_data(index)
            if table_data:
                print(table_data)
        elif select == 6:
            print(link.get_size())
        elif select == 7:
            link.jiudi_invert(link.head)
