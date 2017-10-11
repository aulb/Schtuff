def reverseBetween(head, m, n):
  x, y = min(m, n), max(m, n)
  d = y - x
  i = 0

  current = head
  # Find starting point
  for i in range(1, x):
    prev = current
    current = current.next
    
  last = prev

  i = 0
  # From the starting point just reverse the .next to like the previous one
  for i in range(d + 1):
    prev, current.next = current.next, prev
    prev, current = current, prev

  # Once I'm at the end starting is equal to the 
	last.next = current
  return head
