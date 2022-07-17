/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring =     function (s){
    // add whatever parameters you deem necessary - good luck!
    let left = 0;
    let longest_substr_length = 0;
    while(left < s.length){
        const hash_map = {};
        let ptr = left;
        while(!hash_map[s[ptr]]){
            hash_map[s[ptr]] = 1;
            ptr += 1;
            if(ptr == s.length){
                break;
            }
        }
        longest_substr_length = Math.max(longest_substr_length, ptr - left);
        left += 1;
    }
    return longest_substr_length;
}