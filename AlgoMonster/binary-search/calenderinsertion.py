class MyCalendar:

    def __init__(self):
        self.calendar = [[10, 15], [20, 30], [30, 35], [35, 40], [50, 60]]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        left_i = 0
        right_i = len(self.calendar) - 1
        insertion_i = len(
            self.calendar
        )  # very important initialization, see explanation below in green

        while left_i <= right_i:
            mid_i = (left_i + right_i) // 2
            # assume that it all fits neatly into the calender i.e. no overlap -> focus on just start or end
            if self.calendar[mid_i][0] > start:
                insertion_i = mid_i
                # check on towards left by narrowind down right end
                right_i = mid_i - 1
            else:
                left_i = mid_i + 1

        # once binary search is completed, we check the end part as well for overlaps
        # edge case: insertion i is 0 -> we know that we don't have to compare the start with the end of a previous event
        # edge case: inerstion i = len(self.calender) -> we append it to the calender and don't need to check if our end is larger than the
        # in both edge cases no checks are needed
        # normal case:
        if (insertion_i > 0 and self.calendar[insertion_i - 1][1] > start) or (
            insertion_i < len(self.calendar) and end > self.calendar[insertion_i][0]
        ):
            return False
        # insert it into calender but it is not needed:
        self.calendar.insert(insertion_i, [start, end])

        return True


calendar1 = MyCalendar()

print(calendar1.book(70, 80))
print(calendar1.book(34, 40))

"""
Before the binary search starts, idx is set to the length of the self.calendar list. 
This effectively sets a default value for idx that points to the end of the list, 
which is one index beyond the last valid index of the list.
This initialization is crucial because, if the binary search loop exits 
without updating idx (meaning the new event should be placed after all existing events in the calendar), 
idx will already be correctly set to append the new event at the end.
"""


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
