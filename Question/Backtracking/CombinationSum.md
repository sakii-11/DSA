-> t.c -> O(2^t/m), t=target , m = mini val ele
-> s.c -> O(t/m) 
-> two choices include the ele , don't include the ele 



```cpp
class Solution {
public:
    vector<vector<int>> res;

    void bt(vector<int> &arr, int tar, int i, vector<int> &curr){
        if(tar==0){
            res.push_back(curr);
            return ;
        }
        if(i>=arr.size() || tar < 0) return ;

        //Adding the ele
        curr.push_back(arr[i]);
        //here the i is not increased since the elements can be repeated 
        bt(arr, tar-arr[i], i,curr);
        curr.pop_back();
        // not adding the ele 
        bt(arr, tar, i+1, curr);
    }
    vector<vector<int>> combinationSum(vector<int>& arr, int tar) {
        vector<int> curr;
        bt(arr, tar, 0, curr);
        return res;
    }
};
```