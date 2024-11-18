# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    return lst[::-1]  

    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    pass  # Implement this



def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    pass  # Implement this

def get_keys_with_value(dct, value):
    keys_with_value = []
    for key, val in dct.items():
        if val == value:
            keys_with_value.append(key)
    return keys_with_value


    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    pass  # Implement this

def merge_sorted_lists(lst1, lst2):
    merged_list = []  
    i, j = 0, 0      

    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1  
        else:
            merged_list.append(lst2[j])
            j += 1  

    
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1

   
    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1

    return merged_list

    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    pass  # Implement this

def find_second_largest(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    
    
    first = second = None
    
    for number in unique_numbers:
        
        if first is None or number > first:
            second = first  
            first = number
        elif second is None or number > second:
            second = number
    
    return second 
    
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    pass  # Implement this


def flatten_list(nested_list):
    flat_list = []  
    stack = list(nested_list)  
    while stack:
        current = stack.pop(0)  
        if isinstance(current, list):
            stack = current + stack  
        else:
            flat_list.append(current)

    return flat_list
    
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    pass  # Implement this


def remove_duplicates(lst):
    seen = set()  
    result = []   

    for item in lst:
        if item not in seen:
            seen.add(item)   
            result.append(item)  
    
    return result


    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    pass  # Implement this

def find_common_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    
    common_elements = set1.intersection(set2)
    return list(common_elements)
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    pass  # Implement this