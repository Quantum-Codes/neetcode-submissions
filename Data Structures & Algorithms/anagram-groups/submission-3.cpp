class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 1. Switch to unordered_map to drop the tree search overhead from O(N log M) to O(N) average
        unordered_map<string, vector<string>> groups;
        
        // 2. Use 'const string&' to avoid making a copy of 'word' at the start of the loop
        for (const string& word : strs) {
            string key = word; // This copy is necessary because we need to sort it
            sort(key.begin(), key.end());
            groups[key].push_back(word);
        }

        vector<vector<string>> soln;
        soln.reserve(groups.size()); // Pre-allocate outer vector
        
        for (auto& pair : groups) {  // 3. Use reference to avoid copying the vectors
            soln.push_back(move(pair.second)); // 4. Use move to pilfer the inner vector's data instantly
        }
        return soln;
    }
};