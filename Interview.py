from tracemalloc import start
    
# max subarray    
# continuous series of numbers (pos or negative)
# return the subarray that has the highest sum 
# the subarray has to be continuous
# write an example input, expected output
# [-1, 1, 2, 3]
# [1, 2, 3]
# [-5, -4, -3]
# [1, 100 , -99,1000]
# [1, 100,-10000,1000]

def find_all_subarrays(arr):
    # create a set to add all the subarrays to
    all_arrays = []

    # find all subarrays
    for start_index, each_value in enumerate(arr):
        end_index = start_index+1
        while end_index <= len(arr):
            new_arr = arr[start_index:end_index]
            all_arrays.append(new_arr)
            end_index+=1
    return all_arrays

def pick_largest_subarray(all_arrays):
        # find largest subarray
    max_array = []
    max_sum = 0
    # loop through all subarrays
    for each_array in all_arrays:
        array_sum = 0
        # compute sum for each subarray --> array_sum
        for each_value in each_array:
            array_sum = each_value+array_sum
        # if sum of array is greater than max, update array and max
        if array_sum > max_sum:
            # update array
            max_array = each_array
            # update max
            max_sum = array_sum
            # print("max array is: {}".format(max_array))
            # print("array sum is {}".format(array_sum))
    return max_array




if __name__ == '__main__':
    print("------ Main -------")
    print("Hello World!")

    arr = [1, 100 , -99,1000]
    all_arrays = find_all_subarrays(arr)
    largest_subarray = pick_largest_subarray(all_arrays)
    print(all_arrays)
    print(largest_subarray)
    