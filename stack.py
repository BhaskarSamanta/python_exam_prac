class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(self.stack)
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        print(self.stack)
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if stack is empty")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the element to push onto the stack: ")
        stack.push(item)
        print("Element", item, "pushed onto the stack.")
    elif choice == '2':
        print("Popped element:", stack.pop())
    elif choice == '3':
        print("Top element:", stack.peek())
    elif choice == '4':
        if stack.is_empty():
            print("Stack is empty")
        else:
            print("Stack is not empty")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    