//Iterative sol 


```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> ans = {{}};
        sort(nums.begin(), nums.end());
        int prevInd = 0, ind=0, n= nums.size();
        for(int i=0; i<n; i++){
            ind = (i >=1 && nums[i]==nums[i-1]) ? prevInd : 0;
            prevInd = ans.size();
            for(int j=ind; j<prevInd; j++){
                ans.push_back(ans[j]);
                ans.back().push_back(nums[i]);
            }
        }
        return ans;
    }
};
```