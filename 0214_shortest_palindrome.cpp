class Solution {
public:
    string shortestPalindrome(string s) {
        int n = s.size();
        
        int MOD = 1e9+7;
        int len = 0;
        //all variable used in multiplication should be declared as "long long"
        long long p;
        long long B = 29;
        long long hash1 = 0, hash2 = 0;
        
        for(int i = 0, p = 1L; i < n; ++i, p = (p * B) % MOD){
            //all variable used in multiplication should be declared as "long long"
            long long d = s[i]-'a';
            hash1 = (hash1 * B + d) % MOD;
            hash2 = (hash2 + d * p) % MOD;
            //the length of palindrome
            if(hash1 == hash2) len = i+1;
        }
        
        string prepend = s.substr(len);
        reverse(prepend.begin(), prepend.end());
        
        return prepend + s; 
    }
};

