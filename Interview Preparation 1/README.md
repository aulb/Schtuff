# Miscellaneous Technical Questions
### Todo
- LRU Cache
- Island in matrix, number of island *
- Rotate matrix * 
- Longest palindrome
- Stock price best time to buy & sell
- Task scheduler
- Implement hash table
- Median from data stream
- Median from two sorted array

### Done With:
- First missing positive
- Power set : OPTIMIZATION NEEDED
- Word break
- Linked List sum
- Search in rotated 
- Max sum of non adjacent elements 
- Implement data structure "Map" storing pairs of integers (key, value) and define following member functions in O(1) runtime: void insert(key, value), void delete(key), int get(key), int getRandomKey(). 
**Answer**: The idea is...
 
# Technical Questions
1) Given the travel time of each customer. Find the driver with the longest chain of trips, which means there is always at least one person on the car.  

2) Assume you have some labor for labeling training data, what data will you collect and what model will you use to building a self-driving car system.  

3) Find and return the first duplicate integer in an array in O(n) time and O(1) space. Assume there will always be at least one duplicated integer in the array. 
4) Write a function that can break a large SMS message string given a length limit per substring. Words must stay together. If a word is longer than the limit, use the word in a new substring and split it as relevant.
```python
def sms_messages(sms_text_str, limit_int):
    return split_messages_list
```
```
Example input: "Joe is the funniest guy", 6
Example output: ["Joe is", "the", "funnie", "st guy"]
```

5) Write an algorithm to check whether a sudoku board is valid/complete.  
```
for x = 0 to 3
	y = 0 to 3
		for i = x to 2
			j = y to 2

counter, vertical_pad, horizontal_pad = 0
while counter < 81:
for i in range(0, 3):
	vertical_pad = 0
	for j in range(0, 3):
		matrix[i][j]
		counter += 1
```
Example answer:
```python
def isValidSudoku(self, board):
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(c,j),(i,c),(i/3,j/3,c)]
    return len(seen) == len(set(seen))

    int [] vset = new int [9];
    int [] hset = new int [9];
    int [] bckt = new int [9];
    int idx = 0;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] != '.') {
                idx = 1 << (board[i][j] - '0') ;
                if ((hset[i] & idx) > 0 ||
                    (vset[j] & idx) > 0 ||
                    (bckt[(i / 3) * 3 + j / 3] & idx) > 0) return false;
                hset[i] |= idx;
                vset[j] |= idx;
                bckt[(i / 3) * 3 + j / 3] |= idx;
            }
        }
    }
    return True;
```

6) (Whiteboard question, written in C): You have a homogeneous fixed-size data structure ("arena") to house structs that should do X (vague description). Define the struct, a function that stores it in the arena, and a function that retrieves it from the arena.  

7) Design an alarm system for driverless car

8) Design an elevator

9) Given a string A and B, find the smallest substring of A that contains all the characters from B. (implement solution in O(n), keep in mind chars in B can repeat)  
http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

10) Given a picture of square with a bunch of horizontal and vertical lines in it (lines are not necessarily spanning the full square length, in other words think of a fine grid with many holes in it), design data structure(s) representing the data and a function that returns a number of squares pictured. (actual implementation expected)  

11) How would you design Youtube (need for low latency, robustness against data loss, ...) (no implementation necessary)  
# Behaviour
- Why do you wanna work with...
- Tell me about a time that you worked on a project in a group setting.
- Sketch design of a project you participated in. (on whiteboard)
