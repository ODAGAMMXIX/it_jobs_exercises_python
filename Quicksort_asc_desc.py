
def quick_sort_ascending(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_ascending(left) + middle + quick_sort_ascending(right)

def quick_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    
    return quick_sort_descending(left) + middle + quick_sort_descending(right)

# Read a list of numbers from the user
nums = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Perform quick sort in ascending and descending order
sorted_ascending = quick_sort_ascending(nums.copy())
sorted_descending = quick_sort_descending(nums.copy())

# Print the sorted lists
print("Ascending order:", sorted_ascending)
print("Descending order:", sorted_descending)

#https://www.google.com/search?client=ubuntu-sn&hs=Bve&sca_esv=558882007&channel=fs&sxsrf=AB5stBhKe6VtGZzdyeE4Yttsg70TUCa5NA:1692666873641&q=quicksort+visualization+video&tbm=vid&source=lnms&sa=X&ved=2ahUKEwiowue9i--AAxVVBbkGHbDiBKEQ0pQJegQIDBAB&biw=1536&bih=779&dpr=1.25#fpstate=ive&vld=cid:1f02e086,vid:pM-6r5xsNEY