class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def getObjects(self):
        for item in self.items:
            return f"{item['String']} \n"