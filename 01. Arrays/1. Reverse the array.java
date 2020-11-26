class Reverse
{
    // Complete the function
    // str: input string
    public static String reverseWord(String str)
    {
        char[] ch = str.toCharArray();
        int left = 0;
        int right = ch.length-1;
        
        while(left<right){
            char temp = ch[left];
            ch[left] = ch[right];
            ch[right] = temp;
            
            left++;
            right--;
        }
        return new String(ch);
    }
}