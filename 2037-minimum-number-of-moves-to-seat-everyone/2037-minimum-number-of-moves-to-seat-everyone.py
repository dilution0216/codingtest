class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total_count=0
        for i in range(len(seats)):
            if seats[i]<=students[i]:
                total_count += students[i]-seats[i]
            else:
                total_count += seats[i]-students[i]
        return total_count