class TextOperation:
   ADD = 'add'
   DELETE = 'delete'

   def __init__(self):
       self.text = ""
       self.operations = []

   def add_text(self, char):
       if not char:
           return
       self.text += char
       self.operations.append((self.ADD, char))

   def delete_text(self):
       if not self.text:
           return
       deleted_char = self.text[-1]
       self.text = self.text[:-1]
       self.operations.append((self.DELETE, deleted_char))

   def undo(self):
       if not self.operations:
           print("empty")
           return
       last_operation = self.operations.pop()
       operation_type, char = last_operation
       if operation_type == self.ADD:
           self.text = self.text[:-1]
       elif operation_type == self.DELETE:
           self.text += char

   def display(self):
       print(self.text)


operation = TextOperation()
operation.add_text('f')
operation.add_text('o')
operation.add_text('o')
operation.display()
operation.delete_text()
operation.display()
operation.undo()
operation.display()
operation.undo()
operation.display()
operation.undo()
operation.delete_text()

