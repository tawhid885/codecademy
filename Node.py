class Node:
    def __init__(self,value,link_node=None):
        self.value=value
        self.link_node=link_node
        
    def set_link_node(self,link_node):
        self.link_node=link_node
    
    def get_link_node(self):
        return self.link_node
    
    def get_value(self):
        return self.value

node1=Node('My name')
node2=Node("is")
node3=Node("shakil")

node1.set_link_node(node2)
node2.set_link_node(node3)
node3.set_link_node(node1)
res1=node1.get_link_node().get_value()
res2=node2.get_link_node().get_value()
res3=node3.get_link_node().get_value()
print(res1)
print(res2)
print(res3)
