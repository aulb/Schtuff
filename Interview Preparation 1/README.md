###### **Important TODO** Set aside a day to go through resume
# Miscellaneous Technical Questions
### Todo
- Task scheduler
- LRU Cache
- Island in matrix, number of island
- Rotate matrix
- Longest palindrome
- Task scheduler
- Implement hash table
- Median from two sorted array
- Median from an unsorted array
- Text Justification
- Search in rotated, **TODO ONE MORE TIME**
- Exponent/Power function
- Valid Sudoku
- Find k smallest value from BST, go over the constant space
- Leetcode 10
- Binary search again

### Done With:
- Largest rectangle from histogram, understanding + 1
- Stock price best time to buy and sell
- Median from data stream
- Stock span
- First missing positive
- Power set, OPTIMIZATION NEEDED
- Word break
- Linked List sum
- Max sum of non adjacent elements
- Implement data structure "Map" storing pairs of integers (key, value) and define following member functions in O(1) runtime: void insert(key, value), void delete(key), int get(key), int getRandomKey(). 
**Answer**: The idea is...
 
# Technical Questions
1) Given the travel time of each customer. Find the driver with the longest chain of trips, which means there is always at least one person on the car.  

2) Assume you have some labor for labeling training data, what data will you collect and what model will you use to building a self-driving car system.  

3) Find and return the first duplicate integer in an array in O(n) time and O(1) space. Assume there will always be at least one duplicated integer in the array. 
4) Write a function that can break a large SMS message string given a length limit per substring. Words must stay together. If a word is longer than the limit, use the word in a new substring and split it as relevant.
**TODO**
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

8) Design an elevator **TODO**

9) Given a string A and B, find the smallest substring of A that contains all the characters from B. (implement solution in O(n), keep in mind chars in B can repeat)  
http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

10) Given a picture of square with a bunch of horizontal and vertical lines in it (lines are not necessarily spanning the full square length, in other words think of a fine grid with many holes in it), design data structure(s) representing the data and a function that returns a number of squares pictured. (actual implementation expected)  

11) How would you design Youtube (need for low latency, robustness against data loss, ...) (no implementation necessary)  

12) String similarities -> DP, edit distance

13) Distance between siblings in trees

14) Max number in a list of numbers... ?

15) Design Uber/Lyft, design nearby drivers (shortest distance): **Video Watched** Need to recap

16) Implement a timer using queue

17) Implement substring

18) You have a dictionary of words. Create a matrix of letters such that each row of the matrix is a word and each column of the matrix is a word. Kind of like a very dense crossword puzzle.  

19) Reverse words in string. Some questions about distributed system.  

20) Search and delete BST

21) Map using BST, get set size

22) Coin change

23) LCA BST

24) Design a spreadsheet application

25) Flatten JSON `{x:1, y:1, z:{a:1,b:2}} flattens to {x:1, y:1, z.a:1, z.b: 2}`

26) Rate limiter for API, web service

# Behaviour
- Why do you wanna work with...
- What would you do to improve ...?
- What would you bring to the team?
- Tell me about a time that you worked on a project in a group setting.
- Sketch design of a project you participated in. (on whiteboard)
- General culture fit question...
- Whats your biggest failure
- Describe a difficult engineering challenge you worked on in your current job.
- Projects...
- What are purposes of a heap
- Big endian little endian
- Talk about former work
- Pros and cons agile
- What have you been doing in your current job
- Whats to stop you from packing up and leaving in four years?
