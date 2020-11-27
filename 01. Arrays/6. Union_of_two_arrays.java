package arrays;
import java.util.*;
public class Union_of_two_arrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		
		while(t--!=0) {
			int arr_1_len = s.nextInt();
			int arr_2_len = s.nextInt();
			
			HashSet<Integer> set = new HashSet<>();
			
			for(int i=0;i<arr_1_len; i++) {
				set.add(s.nextInt());
			}
			
			for(int i=0; i<arr_2_len; i++) {
				set.add(s.nextInt());
			}
			
			System.out.println(set.size());
		}

	}

}
