class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# def rever(number, digits, count, string, list):
#     if count == len(digits):
#         return
#     if len(string).__eq__(len(digits)):
#         list.append(string)
#     print(number[digits[count]].split())
#     for value in number[digits[count]].split():
#         rever(number, digits, count + 1, string + value, list)
#




if __name__ == '__main__':

    f=open("README.md","r")
    f2=open("SAVE_README.md","w")
    string=f.read()
    f2.write(string)
    string=string.split("***")
    title=string.pop(0)
    li=[]
    mapper={}
    for i in string:
        sum=0
        s=i.replace("#","").lstrip()

        for j in s:
            if not j.isdigit():
                break
            sum=sum*10+int(j)

        mapper[sum]="***\n"+i.lstrip().rstrip()+"\n***\n"
        li.append(sum)
    max=max(mapper.keys())
    # print(len(mapper))
    file=open("README.md","w")
    file.write(title)
    for i in range(1,max+1):
        if i in mapper.keys():
            file.write(mapper[i])
    # for i in mapper.keys():
        # print(mapper[i])
    # file=open("test.md","w")

#     #     print(uniquePathsWithObstacles([
#     #   [0,0,0],
#     #   [0,1,0],
#     #   [0,0,0]
#     # ]))
#     l = [-1, -2, -3, -4]
#     # print(letterCombinations("234"))
#     l1 = ListNode(1)
#     l1.next = ListNode(1)
#     l1.next.next = ListNode(1)
#     l1.next.next.next = ListNode(1)
#     l1.next.next.next.next = ListNode(1)
#     l1.next.next.next.next.next = ListNode(6)
#     l1.next.next.next.next.next.next = ListNode(7)
#     l1.next.next.next.next.next.next.next = ListNode(8)
#
#     l2 = TreeNode(-2)
#     l2.right = TreeNode(-3)
#
#     # l3=ListNode(0)
#     # l3.next=rotateRight(l1,2)
#     # while l3:
#     #     print(l3.val)
#     #     l3=l3.next
#
#     l1 = TreeNode(1)
#     l1.left = TreeNode(2)
#     l1.right = TreeNode(2)
#     l1.right.left = TreeNode(3)
#     l1.right.right = TreeNode(4)
#     l1.left.left = TreeNode(4)
#     l1.left.right = TreeNode(3)
#     # l2 = TreeNode(1)
#     # l2.left = TreeNode(2)
#     # l2.right = TreeNode(3)
#     # l2.right.left = TreeNode(5)
#     # l2.right.left.left = TreeNode(5)
