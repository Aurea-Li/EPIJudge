
def multiply(nums1, nums2):

    result = [0] * (len(nums1) + len(nums2))
    for i in reversed(range(len(nums1))):
        for j in reversed(range(len(nums2))):
            result[i + j + 1] += (nums1[i] * nums2[j])
            result[i + j] += (result[i + j + 1] // 10)
            result[i + j + 1] %= 10


    for i in range(len(result)):
        if result[i] != 0:
            return result[i:]


print(multiply([1],[3,4]))
