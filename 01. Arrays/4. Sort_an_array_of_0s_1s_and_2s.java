package arrays;
import java.util.*;

public class Sort_an_array_of_0s_1s_and_2s {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		while(t--!=0) {
			
			int n = s.nextInt();
			int[] arr = new int[n];
			
			for(int i=0; i<n; i++) {
				arr[i] = s.nextInt();
			}
			
			sort012(arr, n);
			
			for(int i=0; i<n; i++) {
				System.out.print(arr[i]+" ");
			}
			System.out.println();
		}
		
	}
	
	public static void sort012(int arr[], int n){
	    // code here 
	    int zero=0,one=0,two=0;
				
				for(int i=0; i<n; i++) {
					switch(arr[i]) {
					case 0:zero+=1;
					break;
					
					case 1:one+=1;
					break;
					
					case 2:two+=1;
					break;
					}
				}
				
				for(int i=0; i<n; i++) {
					if(zero>0) {
						arr[i]=0;
						zero-=1;
					} else if(one>0) {
						arr[i]=1;
						one-=1;
					} else {
						arr[i] = 2;
						two-=1;
					}
				}
	}

}
