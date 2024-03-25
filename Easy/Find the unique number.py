# There is an array with some numbers. All numbers are equal except for one. Try to find it!
def find_uniq(arr):
    setArr = set(arr)
    NewSetArr = list(setArr)
    if arr.count(NewSetArr[0]) == 1:
        return NewSetArr[0]
    else:
        return NewSetArr[1]