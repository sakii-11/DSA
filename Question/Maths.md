//count the number of digits of n that divides n completely 

```cpp
class Solution {
  public:
    // Function to count the number of digits in n that evenly divide n
    int evenlyDivides(int n) {
        int cnt=0, t=n, p=0;
        while(n){
            p= n%10;
            n= n/10;
            if(p!=0 && t%p==0)
            cnt++;
        }
        return cnt;
    }
};
```


// Reverse a number for signed and unsigned integer 

```cpp
class Solution {
public:
    int reverse(int x) {
        long ans =0;
        while(x){

            ans = ans * 10 + x%10;
            x /=10;
        }
        if(ans<INT_MIN || ans> INT_MAX) return 0; //question specific cond 
        else return ans;
    }
};
```

// check palindrome for a string 
```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int i=0, j= s.length()-1;
        while(i<j){
            if(s[i]!=s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
};
```

// check palindrome for signed and unsigned int 
```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        long rev=0, t=x;
        while(x>0){
            rev = rev*10 + (x%10);
            x /=10;
        }
        return t == rev;
    }
};
```

// lcm and gcd , lcm = a*b/gcd
```cpp
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int gcd(int a, int b){
        while(a>0 && b>0){
            if(a>b) a%=b;
            else b %=a;
        }
        return a==0? b: a;
    }
  
    vector<int> lcmAndGcd(int a, int b) {
        int g = gcd(a,b);
        int lcm = a*b/g;
        return {lcm, g};
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        int A, B;

        cin >> A >> B;

        Solution ob;
        vector<int> ans = ob.lcmAndGcd(A, B);
        cout << ans[0] << " " << ans[1] << endl;
        cout << "~" << endl;
    }
    return 0;
}

```

// Armstrong number ->  153 is an Armstrong number since 13 + 53 + 33 = 153. 
```cpp
class Solution {
  public:
    bool armstrongNumber(int n) {
        int ans=0, t=n;
        while(n){
            int k = n%10;
            n /=10;
            ans += k*k*k;
        }
        return ans==t;
    }
};
```

// find all divisor 
```cpp
vector<int> findDivisors(int n) {
    vector<int> divisors; 
    int sqrtN = sqrt(n); 
    for (int i = 1; i <= sqrtN; ++i) { 
        if (n % i == 0) { 
            divisors.push_back(i); 
            if (i != n / i) {
                divisors.push_back(n / i); 
            }
        }
    }
    return divisors; 
}

```

//check for prime num
```cpp
class Solution {
  public:
    bool isPrime(int n) {
        if(n<=1) return false;
        else if(n==2 || n==3) return true;
        else if(n%2==0 || n%3==0) return false;
        for(int i=5; i*i<=n; i+=6){
            if(n% i==0 || n%(i+2)==0) return false;
        }
        return true;
    }
};
```

fibonacci
```cpp
int fibonacci(int N){

   if(N <= 1)
   {
       return N;
   }

   int last = fibonacci(N-1);
   int slast = fibonacci(N-2);
   
   return last + slast;

}
```

factorial 
```cpp
int factorial(int n){
      if(n == 0)
   {
       return 1;
   }
   return n * factorial(n-1);

}
```