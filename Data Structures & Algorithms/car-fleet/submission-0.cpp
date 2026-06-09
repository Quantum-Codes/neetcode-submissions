class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<int, int> cars;
        stack<float> fleets;

        for (int i = 0; i < position.size(); i++) {
            cars[position[i]] = speed[i];
        }
        // built map in O(nlogn)

        // now.. we traverse
        for (auto it : cars) {
            // ummm... i forgot. <thinks 5s> oh i gotta calculate time.
            // uhh <thinks 5s, idk why>
            float time = (target - it.first) / (float) it.second;
            while (!fleets.empty() && fleets.top() <= time) {
                // this means merging logic
                // changed if to while
                fleets.pop();
            }
            // now add the item
            fleets.push(time);
        }

        return fleets.size();
    }
};
