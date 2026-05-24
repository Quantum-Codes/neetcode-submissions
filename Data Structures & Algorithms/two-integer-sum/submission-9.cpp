class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        unordered_map<int, int> x;
        x.reserve(nums.size() * 2);  // pre-allocate to avoid rehashing
        x.max_load_factor(0.25);     // reduce collisions
        
        for (int i = 0; i < (int)nums.size(); i++) {
            auto it = x.find(target - nums[i]);
            if (it != x.end()) return {it->second, i};
            x[nums[i]] = i;
        }
        return {};
    }
};