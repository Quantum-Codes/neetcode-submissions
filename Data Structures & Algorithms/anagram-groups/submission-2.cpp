class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> groups;
        array<int, 26> counts;
        for (string word : strs) {
            fill(counts.begin(), counts.end(), 0);
            for (char c : word) {
                counts[c - 97]++;
            }
            groups[counts].push_back(word);
        }

        vector<vector<string>> soln;
        for (auto vec : groups) {
            soln.push_back(vec.second);
        }
        return soln;
    }
};
