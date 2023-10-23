class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = None

class LinkedList():
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
        currentNode.next
      currentNode.next = newNode
  
  def insertAtIndex(self, index, data):
    newNode = Node(data)
    position = 0
    currentNode = self.head
    if position == index:
      self.insertAtBegin()
    else:
      while currentNode is not None and position+1 != index:
        position += 1
        currentNode = currentNode.next
      newNode.next = currentNode.next
      currentNode.next = newNode
  
  def deleteAtBegin(self):
    if self.head is not None:
      currentNode = self.head
      if currentNode.next is not None:
        self.head = currentNode.next
        currentNode = None
      else:
        currentNode = None

  def deleteAtEnd(self):
    currentNode = self.head
    if currentNode.next is not None:
      while currentNode.next is not None:
      currentNode = None
    else:
      currentNode = None

  def deleteAtIndex(self, index):
    currentNode = self.head
    position = 0
    if currentNode.next is not None:
      while currentNode.next is not None and position+1 != index:
        position += 1
        currentNode = currentNode.next
      currentNode = (currentNode.next).next
      currentNode.next = None
    else:
      self.deleteAtBegin()

  def deleteByValue(self, data):
    currentNode = self.head
    if currentNode.data == data:
      self.head = currentNode.next
      currentNode = None
    else:
      position = 0
      while currentNode.data != data:
        currentNode.next
        position += 1
      self.deleteAtIndex(position)
  
  def updateAtIndex(self, index, data):
    currentNode = self.head
    position = 0
    if position == index:
      currentNode.data = data
    else:
      while currentNode.next is not None and position+1 != index:
        position += 1
        currentNode = currentNode.next
      currentNode.data = data
  
  def printLinkedListInListForm(self):
    currentNode = self.head
    temp = []
    if currentNode is not None:
      while currentNode.next != None:
        temp.append(currentNode.data)
        currentNode = currentNode.next
      print(temp)
    else:
      print(temp)

  def printLinkedList(self):
    currentNode = self.head
    if currentNode is not None:
      while currentNode.next != None:
        print(currentNode.data)
        currentNode = currentNode.next

  def printValueAtIndex(self, index):
    currentNode = self.head
    position = 0
    if currentNode is not None:
      if position == index:
        print(currentNode.data)
      else:
        while currentNode.next is not None and position+1 != index:
          position += 1
          currentNode = currentNode.next
        print(currentNode.data)
  
  def returnIndexAtValue(self, data):
    currentNode = self.head
    position = 0
    if currentNode is not None:
      while currentNode.data != data:
        position += 1
        currentNode = currentNode.next
      return position
