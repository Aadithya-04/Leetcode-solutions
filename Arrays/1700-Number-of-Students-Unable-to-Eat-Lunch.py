from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = 0

        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0   #reset counter when a sandwich is eaten

            else:
                students.append(students.popleft())
                count += 1
            
            if count == len(students):
                break
        return len(students)
