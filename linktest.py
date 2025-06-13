class Node(object):
# 初始化节点
    def __init__(self, value):
        self.value = value # 数据域
        self.next = None # 地址域

class SinglelinkedList(object):
# 初始化链表
    def __init__(self, node=None):
        self.head = node # 头指针
        self.tail = node # 尾指针

# 判断链表是否为空
def is_empty(self):
    return self.head == None

# 链表长度
def length(self):
    # 记录当前节点
    cur = self.head
    # 记录长度
    count = 0
    # 判断节点是否为空
    while cur is not None:
        # 单次循环，节点计数+1
        count += 1
        # 移动到下一个节点
        cur = cur.next
    # 返回长度
    return count
# 遍历整个链表
def travel(self):
    # 记录当前节点
    cur = self.head
    # 判断节点是否为空
    while cur is not None:
        # 输出节点数据
        print(cur.value)
        # 移动到下一个节点
        cur = cur.next
# 链表头部添加元素
def add (self, value):
    # 创建新节点
    new_node = Node(value)
    # 将新节点的地址域指向头指针
    new_node.next = self.head
    # 将头指针指向新节点
    self.head = new_node

# 链表尾部添加元素
def append(self, value):
    # 创建新节点
    new_node = Node(value)
    # 判断链表是否为空
    if self.length() == 0:
        # 链表为空，则新节点直接为头
         self.head = new_node
    # 链表不为空，则尾指针指向新节点
    else:
        # 记录当前节点
        cur = self.head
        # 遍历链表，找到尾指针
        while cur.next is not None:
            # 移动到下一个节点
            cur = cur.next
            # 新节点地址指向尾节点
        cur.next=new_node
# 指定位置添加元素
def insert(self, pos, value):
    # 判断输入的位置是否小于等于0，若小于等于0，则直接添加到头部
    if pos <= 0:
        self.add(value)
    # 若输入的位置大于等于链表长度，则直接添加到尾部
    elif pos >= self.length():
        self.append(value)
    else:
        # 把要插入的元素转换成节点
        new_node = Node(value)
        # 定义变量cur,表示要插入位置的那个节点
        cur = self.head
        # 定义变量count,表示当前遍历的节点数
        count = 0
        # 遍历链表，找到要插入的位置
        while count < pos-1:
            # 移动到下一个节点
            cur = cur.next
            # 节点数+1
            count += 1
        # 新节点地址域指向要插入位置的节点的地址域
        new_node.next = cur.next
        # 要插入的位置节点地址域指向新节点
        cur.next = new_node
# 删除节点
def remove(self, value):
    # 记录当前节点
    cur = self.head
    # 定义计数器
    count = 0
    # 判断当前节点是否为空，若不为空则循环
    while cur is not None:
        # 若当前节点数据域等于要删除的节点数据域，则删除当前节点
        if cur.value == value:
            # 若当前节点是头节点，则头指针指向下一个节点
            if count == 0 :
                self.head = cur.next
            else:
                # 若当前节点不是头节点，则将前一个节点的地址域指向当前节点的下一个节点
                pre.next = cur.next
            # 若删除的是尾节点，则尾指针指向前None
            if cur.next is None:
                self.tail = None
            return True  # 删除成功
        # 移动到下一个节点
        pre = cur
        cur = cur.next
        # 节点计数+1
        count += 1
    # 若循环结束，则没有找到要删除的节点，返回False
    return False
# 查找节点是否存在
def search(self, value):
    # 记录当前节点
    cur = self.head
    # 定义count变量，记录当前遍历的节点数
    count = 0
    # 判断当前是否是否为空，如果不是，就循环
    while cur is not None:
        # 若当前节点数据域等于要查找的节点数据域，则返回True
        if cur.value == value:
            return True
        # 节点数+1
        count += 1
        # 移动到下一个节点
        cur = cur.next
    # 若循环结束，则没有找到要查找的节点，返回False
    return False


    # 创建链表
link = Node([1,2,3,4,5])
    # 输出节点信息
print(link)
    # 输出节点数据域信息
print(link.value)
    # 输出节点地址域信息
print(link.next)
    # 测试单向链表类
sll=SinglelinkedList(link)
    # 输出链表头指针信息
print("sss",sll.head)
    # 输出链表头节点数据域信息
print(sll.head.value)
print('-'*31)

19038760897