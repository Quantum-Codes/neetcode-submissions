// 1. Turn off I/O sync
auto init = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> x;
        // 2. Prevent rehashing
        x.reserve(nums.size()); 
        
        for (int i = 0; i < nums.size(); i++) {
            int item = nums[i];
            int complement = target - item;
            
            // 3. Single lookup using the iterator
            auto it = x.find(complement);
            if (it != x.end()) {
                return {it->second, i};
            }
            
            x[item] = i;
        }
        
        return {};
    }
};