import ll

testll = ll.LinkedList()
l = [5,4,2,7,8]
for i in range(len(l)):
	testll.insertAtEnd(l[i])
testll.printLinkedListInListForm()
testll.printLinkedList()
testll.deleteAtBegin()
testll.deleteAtEnd()
testll.insertAtBegin(5)
testll.insertAtIndex(4, 8)
print(testll.returnValueAtIndex(4))
testll.deleteByValue(2)
print(testll.returnIndexAtValue(8))
testll.deleteAtIndex(2)
testll.printLinkedListInListForm()
print(testll.sizeOfLinkedList())