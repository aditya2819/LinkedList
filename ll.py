class Node():
      def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
  def __init__(self):
    self.head = None

  def insertAtBegin(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
    else:
      newNode.next = self.head
      self.head = newNode
  
  def insertAtEnd(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
    else:
      currentNode = self.head
      while currentNode.next is not None:
        currentNode = currentNode.next
      currentNode.next = newNode
  
  def insertAtIndex(self, index, data):
    newNode = Node(data)
    position = 0
    currentNode = self.head
    if index >= 0:
      if index == 0:
        self.insertAtBegin(data)
      else:
        while currentNode is not None and position+1 != index:
          position += 1
          currentNode = currentNode.next
        if currentNode is not None:
          newNode.next = currentNode.next
          currentNode.next = newNode
        else:
          print("Index not found")
  
  def deleteAtBegin(self):
    if self.head is not None:
      currentNode = self.head
      if currentNode is not None:
        self.head = currentNode.next
        currentNode = None
    else:
      print("List is Empty")

  def deleteAtEnd(self):
    if self.head is not None:
      currentNode = self.head
      if currentNode.next == None:
        self.head = None
      else:
        while currentNode.next.next is not None:
          currentNode = currentNode.next
        currentNode.next = None
    else:
      print("List is empty")



  def deleteAtIndex(self, index):
    currentNode = self.head
    position = 0
    if index >= 0:
      if index == 0:
        self.deleteAtBegin()
      else:
        while currentNode is not None and position+1 != index:
          position += 1
          currentNode = currentNode.next
        if currentNode is not None:
          currentNode.next = currentNode.next.next
        else:
          print("Index not found")
    

  def deleteByValue(self, data):
    index = self.returnIndexAtValue(data)
    if index is not None:
      self.deleteAtIndex(index)
    else:
      print("Value not found")
  
  def updateAtIndex(self, index, data):
    if index < 0:
      print("Invalid index")
      return
    currentNode = self.head
    position = 0
    if index == 0:
      if currentNode is not None:
          currentNode.data = data
      else:
          print("Index not found")
    else:
      while currentNode is not None:
        if position == index:
          currentNode.data = data
          return
        position += 1
        currentNode = currentNode.next
      print("Index not found")

  def updateByValue(self, data, newdata):
    index = self.returnIndexAtValue(data)
    if index is not None:
      self.updateAtIndex(index)
    else:
      print("Value not found")
      
  def printLinkedListInListForm(self):
    currentNode = self.head
    temp = []
    while currentNode is not None:
      temp.append(currentNode.data)
      currentNode = currentNode.next
    print(temp)

  def printLinkedList(self):
    currentNode = self.head
    if currentNode is not None:
      while currentNode:
        print(currentNode.data)
        currentNode = currentNode.next
    else:
        print("Empty List")

  def returnValueAtIndex(self, index):
    currentNode = self.head
    position = 0
    while currentNode is not None:
      if position == index:
        return currentNode.data
      position += 1
      currentNode = currentNode.next
    return print("Index not found")
  
  def returnIndexAtValue(self, data):
    currentNode = self.head
    position = 0
    if currentNode is not None:
      while currentNode.data != data:
        position += 1
        currentNode = currentNode.next
      if currentNode is not None:
        return position
      else:
        return print("Value not present")
  
  def sizeOfLinkedList(self):
    size = 0
    if self.head is not None:
      currentNode = self.head
      while currentNode is not None:
        size += 1
        currentNode = currentNode.next
    return size
