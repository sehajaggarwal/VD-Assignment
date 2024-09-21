#QUESTION 6
#----------------

def find_duplicate(nums):
    # Initalise 2 pointers
    slow = nums[0]
    fast = nums[0]
    
    # Loop runs till first intersection 
    while True:
        slow = nums[slow]  
        fast = nums[nums[fast]]  
        if slow == fast:
            break
    
    # Start slow pointer from the start and move both at the same pace till second intersection
    slow = nums[0]
    while slow != fast:
        slow = nums[slow] 
        fast = nums[fast]
    
    return slow

#Test the solution
if __name__ == "__main__":
    input_array = [1, 3, 4, 1, 2, 5]
    result = find_duplicate(input_array)
    print(result)


