import sys

class Heading:
  def __init__(self, weight, text):
    self.weight = weight
    self.text = text

class Node:
  def __init__(self, heading, children):
    self.heading = heading
    self.children = children

def to_outline(headings):
  """Converts a list of input headings into nested nodes"""

  # Implement this function. Sample code below builds an 
  # outline of only the first heading
  # Append a dummy node in the beginning and call helper function
  return get_node_helper(0, [Heading(0, "")] + headings)[1]

# Gets all the nodes and its respective childrens
def get_node_helper(parent_index, headings):
  parent_header, children = headings[parent_index], []
  parent_node = Node(parent_header, children)
  
  # Start from index after the parent's
  index = parent_index + 1
  while index < len(headings):
    current_header = headings[index]
    # If the current header's weight is more than the parent's, then its a child
    if current_header.weight > parent_header.weight:
      index, current_node = get_node_helper(index, headings)
      children.append(current_node)
    # Otherwise its not a child, stop at the previous index
    else:
      return index - 1, parent_node
    
    # Always remember to increment
    index += 1
  return index, parent_node

def parse(record):
  """Parses a line of input. 
  This implementation is correct for all predefined test cases."""
  (hlevel, text) = record.split(" ", 1)
  return Heading(int(hlevel[1:]), text.strip())

def to_html(node):
  """Converts a node to HTML. 
  This implementation is correct for all predefined test cases."""
  child_html = "<ol>" + "\n".join(
    ["<li>" + to_html(child) + "</li>" for child in node.children]
  ) + "</ol>" if node.children else ""

  return (node.heading.text and node.heading.text + "\n") + child_html

headings = [parse(line) for line in sys.stdin.readlines()]
outline = to_outline(headings)
html = to_html(outline)
print html
