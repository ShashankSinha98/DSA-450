package arrays;
import java.util.*;

/**
 *   Need Optimization!
 * 
 * */

public class Kth_smallest_element {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		while(t--!=0) {
			
			int n = s.nextInt();
			int[] arr = new int[n];
			int k = s.nextInt();
			
			for(int i=0; i<n; i++) {
				arr[i] = s.nextInt();
			}
			
			int ans = kthSmallest(arr,0,n,k);
			System.out.println(ans);
			
			
		}
	}
	
	public static int kthSmallest(int[] arr, int l, int r, int k) 
	{ 
	    Arrays.sort(arr);
	    return arr[k-1];
	} 

}
