class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> x;
        x.reserve(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            int item = nums[i];
            if (x.find(target - item) != x.end()) {
                return {x[target - item], i};
            }
            x[item] = i;
        }
    }
};
