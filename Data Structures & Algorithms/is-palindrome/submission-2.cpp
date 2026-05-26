class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.length() - 1;
        
        while (i < j) {
            // If the left character isn't a letter or digit, skip it
            if (!isalnum(s[i])) {
                i++;
            } 
            // If the right character isn't a letter or digit, skip it
            else if (!isalnum(s[j])) {
                j--;
            } 
            // Both are valid alphanumeric characters, so compare them
            else {
                if (tolower(s[i]) != tolower(s[j])) {
                    return false;
                }
                i++;
                j--;
            }
        }
        return true;
    }
};