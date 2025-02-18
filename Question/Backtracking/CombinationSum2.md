return unique subsets with no repeations with the target sum 
t.c && s.c -> O(n*2^n)

```cpp
class Solution {
public:
    vector<vector<int>> res;
    void dfs(vector<int>&arr, vector<int>&curr, int target, int ind){
        if(target == 0){
            res.push_back(curr);
            return;
        }
        //to ensure unique ele 
        for(int i = ind; i<arr.size() && target >= arr[i]; i++){
            if(i>ind && arr[i]==arr[i-1]) continue;
            curr.push_back(arr[i]);
            dfs(arr, curr, target-arr[i], i+1);
            curr.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& arr, int target) {
        sort(arr.begin(), arr.end()); //impp
        vector<int> curr;
        dfs(arr, curr, target, 0);
        return res;
    }
};
```





```cpp
class Solution {
public:
    vector<vector<int>> res;
    set<vector<int>> s;
    void bt(vector<int> &arr, vector<int>&curr, int tar, int st){
        if(tar == 0){
            s.insert(curr);
            return;
        }
        if(st>=arr.size() || tar<0 ) return;

        //Adding the ele but dosen't repeat
        curr.push_back(arr[st]);
        bt(arr, curr, tar-arr[st], st+1);
        curr.pop_back();
        int i=st;
        while(i<arr.size() && arr[st]== arr[i]) i++;
        bt(arr, curr, tar, i);

    }

    vector<vector<int>> combinationSum2(vector<int>& arr, int tar) {
        res.clear();
       vector<int> curr;
       sort(arr.begin(), arr.end());
       bt(arr, curr, tar, 0);
       for(auto it: s){
        res.push_back(it);
       }
       return res;

    }
};
```