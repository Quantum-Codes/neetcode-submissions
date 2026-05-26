class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            if (s[i] >= 'A' && s[i] <= 'Z') {
                s[i] = s[i] + 'a' - 'A';
            }
            if ((s[i] > 'z')||(s[i] < 'a' && s[i] > '9')||(s[i] < '0')) {
                i++;
                continue;
            }

            if (s[j] >= 'A' && s[j] <= 'Z') {
                s[j] = s[j] + 'a' - 'A';
            }
            if ((s[j] > 'z')||(s[j] < 'a' && s[j] > '9')||(s[j] < '0')) {
                j--;
                continue;
            }

            if (s[i] != s[j]) {
                return false;
            }
            i++; j--;
        }
        return true;
    }
};
