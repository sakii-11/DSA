```cpp
class Solution {
public:
    vector<vector<int>> res;
    void bt(vector<int>&nums, int ind){
        if(ind == nums.size()){
            res.push_back(nums);
            return;
        }
        set<int> st;
        for(int i=ind; i<nums.size(); i++){
            if(st.count(nums[i])==1) continue; //can't use checking for same ele here since the list is swapped so it doesn't remain sorted 
            st.insert(nums[i]);
            swap(nums[ind], nums[i]);
            bt(nums, ind+1);
            swap(nums[ind], nums[i]);
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        bt(nums,0);
        return res;
    }
};
```