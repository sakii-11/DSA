## Bubble Sort 
```cpp
void bubbleSort(vector<int>& arr) {
    int n= arr.size();
    for(int i=n-1; i>=0; i--){
        int didswap=0;
        for(int j=0; j<i; j++){
            if(arr[j]>arr[j+1])
            {
                swap(arr[j], arr[j+1]);
                didswap++;
            }
        }
        if(didswap ==0) break;
        
    }
}
```
T.C -> O(n2), S.C-> O(1)



## Insertion Sort 
```cpp
void insertionSort(vector<int>& arr) {
    int n= arr.size();
    for(int i=0; i<n; i++){
        int j =i;
        while(j>=0 && arr[j-1]>arr[j]){
            swap(arr[j], arr[j-1]);
            j--;
        }
    }
}
```


T.C -> O(n2), S.C-> O(1)


## Selection Sort
select the smallest ele in each iteration and swap it with arr[i] val.
```cpp
void selectionSort(vector<int> &arr) {
    int n= arr.size();
    for(int i=0; i<n-1; i++){
        int mini=i;
        for(int j=i+1; j<n; j++){
            if(arr[j]<arr[mini]){
                mini = j;
            }
        }
        int temp = arr[mini];
        arr[mini]= arr[i];
        arr[i]= temp;
    }
}

```
T.C -> O(n2), S.C-> O(1)


## Merge Sort 
```cpp
class Solution {
  public:
    void merge(vector<int>&arr, int low , int high , int mid){
        vector<int> temp;
        int left = low, right= mid+1;
        while(left<=mid && right<=high){
            if(arr[left]<=arr[right]){
                temp.push_back(arr[left]);
                left++;
            }
            else{
                temp.push_back(arr[right]);
                right++;
            }
        }
        while(left<=mid){
            temp.push_back(arr[left]);
            left++;
        }
        while(right<=high){
            temp.push_back(arr[right]);
            right++  ;        
        }
        
        for(int i=low; i<=high; i++){
            arr[i]= temp[i-low];
        }
    }
  
  
    void mergeSort(vector<int>& arr, int l, int r) {
        if(l>=r) return ;
        int mid = (l+r)/2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);
        merge(arr, l, r, mid);
    }
};
```


T.C -> O(nlogn), S.C-> O(n)



## Quick Sort
```cpp
class Solution
{
    public:
    void quickSort(int arr[], int low, int high)
    {
        if(low<high)
        {
            int p = partition(arr,low,high);
            quickSort(arr,low,p-1);
            quickSort(arr,p+1, high);
        }
    }
    
    public:
    int partition (int arr[], int low, int high)
    {
        int pivot= arr[high];
        int i= low-1;
        for(int j=low; j<=high-1; j++)
        {
            if(arr[j]<=pivot)
            {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i+1], arr[high]);
        return i+1;
    }
};
```
T.C -> O(nlogn), S.C-> O(n)
