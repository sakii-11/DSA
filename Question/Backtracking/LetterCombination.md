map every num tp string, start curr =", 
base case-> if curr.size is equal to digit size add to ans and return ,
for every char of the string for the digit , backtrack

```cpp
class Solution {
public:
    vector<string> ans;
    vector<string> digitsToChar = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    void backtrack(int i, string curr, string digits){
        if(curr.size() == digits.size()){
            ans.push_back(curr);
            return ;
        }

        string chars= digitsToChar[digits[i]-'0'];
        for(auto c: chars )
         backtrack(i+1, curr+ c, digits);

    }

    vector<string> letterCombinations(string digits) {
        if(digits.size()==0) return ans;
        backtrack(0,"",digits);
        return ans;
    }
};
```