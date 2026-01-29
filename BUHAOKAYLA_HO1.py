
w = input("Enter a word: ")
nums = []

for i in range(len(w)):
    nums.append(int(input(f"Enter number {i+1}: ")))

avg = sum(nums) / len(nums)

print(nums)
print("The length of the word is", len(w))
print("The average of the numbers is", avg)

if len(w) < avg:
    print(f"The length of the word '{w}' is less than the average.")
