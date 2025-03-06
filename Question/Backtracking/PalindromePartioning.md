

```cpp
class Solution {
public:

    bool isPali(int l, int r, string s){
        while(l<r){
            if(s[l]!=s[r]) return false;
            l++;
            r--;
        }
        return true;
    }

    void dfs(int i, string s, vector<string>&part, vector<vector<string>>&ans){
        if(i>= s.length()){
            ans.push_back(part);
            return;
        }

        int n = s.length();
        for(int j=i; j<n; j++){
            if(isPali(i,j,s)){
                part.push_back(s.substr(i,j-i+1));
                dfs(j+1, s, part, ans);
                part.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> part;
        dfs(0, s, part, ans);
        return ans;
    }
};
```