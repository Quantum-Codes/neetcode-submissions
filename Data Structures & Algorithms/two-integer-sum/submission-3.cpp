class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> x;
        
        for (int i = 0; i < nums.size(); i++) {
            int item = nums[i];
            int complement = target - item;
            
            auto it = x.find(complement);
            if (it != x.end()) {
                return {it->second, i};
            }
            x[item] = i;
        }
        
        return {};
    }
};