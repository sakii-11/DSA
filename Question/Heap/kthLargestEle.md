```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        //using min heap;
        priority_queue<int, vector<int>, greater<int>> min_heap;

        for(auto n : nums){
            min_heap.push(n);
            if(min_heap.size()>k){
                min_heap.pop();
            }
        }
        return min_heap.top();
    }
};
```


Kth largest element in a stream 
```cpp
class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for(auto n : nums){
            minHeap.push(n);
            if(minHeap.size()> k){
                minHeap.pop();
            }
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        if(minHeap.size()> k){
            minHeap.pop();
        }
        return minHeap.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
```