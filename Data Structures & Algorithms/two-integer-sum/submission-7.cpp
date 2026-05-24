class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<pair<int, int>> arr(n);
        
        for (int i = 0; i < n; i++) {
            arr[i] = {nums[i], i};
        }

        sort(arr.begin(), arr.end());

        int left = 0;
        int right = n - 1;

        while (left < right) {
            // Use long long to prevent any potential integer overflow
            long long current_sum = (long long)arr[left].first + arr[right].first;
            
            if (current_sum == target) {
                vector<int> res = {arr[left].second, arr[right].second};
                sort(res.begin(), res.end());
                return res;
            } else if (current_sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return {};
    }
};