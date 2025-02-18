T.c - > O(n*2^n), s.c -> o(2^n)
initialize the powerset with an empty vector [], 
for every element in nums , 
  ->push the elements of the powerset again and then add the element at the end of these vectors;


```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
       int n= nums.size();
       vector<vector<int>> powerset = {{}};
       for(int num : nums){
        int n= powerset.size();
        for(int i=0; i<n; i++){
            powerset.push_back(powerset[i]);
            powerset.back().push_back(num);
        }
       }
       return powerset;
    }
};
```