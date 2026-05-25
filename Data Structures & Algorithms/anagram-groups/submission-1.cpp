class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> groups;
        string key;
        for (string word : strs) {
            key = word;
            sort(key.begin(), key.end());
            groups[key].push_back(word);
        }

        vector<vector<string>> soln;
        for (auto vec : groups) {
            soln.push_back(vec.second);
        }
        return soln;
    }
};
