public class LinearSearch{
    
    static int search(int arr[],int n,int x){
        
        for(int i=0;i<n;i++){
            
            if(arr[i]==x){
                return i;
            }
        }
        return -1;
        
    }
    public static void main(String args[]) {
     int[] arr={5,3,7,6,4,1};
     int n=arr.length;
     int x=7;
    
    int ans=search(arr,n,x);
    if(ans==-1){
      System.out.println("Element not found");  
    } else{
        System.out.println("Element found at "+ans);
    }
    }
}
