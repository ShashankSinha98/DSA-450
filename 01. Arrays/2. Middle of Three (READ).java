// https://practice.geeksforgeeks.org/problems/middle-of-three2926/1

class Solution{
    int middle(int A, int B, int C){
        //code here
        
        int x = A-B;
        int y = B-C;
        int z = C-A;
        
        if(x*y>0) return B;
        
        if(y*z>0) return C;
        
        return A;
    }
}