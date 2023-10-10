"""    //max split
     
    Read the input string s.
     
    Initialize variables L and R to 0. These variables will keep track of the number of 'L's and 'R's encountered so far.
     
    Initialize an empty list ans to store the segments.
     
    Initialize an empty string a to accumulate characters until the count of 'L's and 'R's becomes equal for a segment.
     
    Iterate through each character c in the string s:
     
    If c is 'L', increment L by 1.
    If c is 'R', increment R by 1.
    Append c to the string a.
    Check if L is equal to R. If they are equal, it means a segment is complete. Append the string a to the ans list, reset a to an empty string, and reset L and R to 0.
     
    Continue this process until you have processed all characters in the string s.
     
    After processing the entire string, ans will contain all the segments, and its length will be the count of segments.
     
    Print the length of ans.
     
    Iterate through each segment in ans and print each segment."""
a = ''
s = input()
lc = 0
lr = 0
ans = []
for i in s:
    if i == 'L':
        lc += 1
        a += i
    elif i == 'R':
        lr += 1
        a += i
    if lc == lr:
        ans.append(a)
        a = ''
        lc = 0
        lr = 0

print(len(ans))

for i in ans:
    print(i)
