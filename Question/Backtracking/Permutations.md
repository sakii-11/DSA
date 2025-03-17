Time complexity: O(n!∗n)

Space complexity: O(n!∗n) 

```cpp
class Solution {
public:
    vector<vector<int>> res;
    void backtrack(vector<int> &nums, int ind){
        if(ind==nums.size()){
            res.push_back(nums);
            return;
        }

        for(int i= ind; i<nums.size(); i++){
            swap(nums[i], nums[ind]);
            backtrack(nums, ind+1);
            swap(nums[i], nums[ind]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        backtrack(nums, 0) ;
        return res;
    }
    
};
```