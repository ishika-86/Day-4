def reverseListSpecificPosition(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst


OrgList = [12, 14, 23, 65, 21, 85, 46]
start = int(input())
end = int(input())
print(OrgList)
print(reverseListSpecificPosition(OrgList, start, end))
