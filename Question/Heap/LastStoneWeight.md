We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

do as the ques says , create a max Heap , take the top two items perfrom the steps 

```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap(stones.begin(), stones.end());
        int x,y;
        while(maxHeap.size()>1){
            y = maxHeap.top();
            maxHeap.pop();
            x = maxHeap.top();
            maxHeap.pop();
            if(x!=y){maxHeap.push(y-x);}

        }
        return maxHeap.size()==0 ? 0 : maxHeap.top();
    }
};
```