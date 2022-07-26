def find_longest_substring(s):
    i = 0
    max_length = 0
    for j, char in enumerate(s):
        while char in s[i:j]:
            i = i + 1
        max_length = max(max_length, j - i + 1)
    return max_length


# For some reason, the python solution above, when converted to its JS counterpart, runs slower
# and returns a `Your code took too long` error for the DSA Masterclass Udemy exercise
# The solution below is faster, and passes the Udemy exercise
# function findLongestSubstring(s){
#     // add whatever parameters you deem necessary - good luck!
#     let left = 0;
#     let longest_substr_length = 0;
#     while(left < s.length){
#         const hash_map = {};
#         let ptr = left;
#         while(!hash_map[s[ptr]]){
#             hash_map[s[ptr]] = 1;
#             ptr += 1;
#             if(ptr == s.length){
#                 break;
#             }
#         }
#         longest_substr_length = Math.max(longest_substr_length, ptr - left);
#         left += 1;
#     }
#     return longest_substr_length;
# }


print(find_longest_substring('')) # 0
print(find_longest_substring('bbbbbb')) # 1
print(find_longest_substring('rithmschool')) # 7
print(find_longest_substring('thisisawesome')) # 6
print(find_longest_substring('thecatinthehat')) # 7
print(find_longest_substring('thisishowwedoit')) # 6
print(find_longest_substring('longestsubstring')) # 8
