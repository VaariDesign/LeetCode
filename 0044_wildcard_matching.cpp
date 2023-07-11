class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0;
        int j = 0;
        int star = -1;
        int lastI = -1;
        while (i < s.length()) {
            if (j < p.length() && (s[i] == p[j] || p[j] == '?')) { ++i; ++j; }
            else if (j < p.length() && p[j] == '*') { star = j++; lastI = i; }
            else if (star != -1) { i = lastI++; j = star + 1; } // if can't find a match and currently have a current *, 
                                                                // restore pointer i and j and use * to consume s 
            else { return false; }
        }
        while (j < p.length() && p[j] == '*') { ++j; }
        return j == p.length();
    }
};
