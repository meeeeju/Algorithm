import java.util.Scanner;

public class main {

   // static int MAX =100000;
    //static int[] d= new int[MAX];
    static int []d;

    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);
        int cnt= sc.nextInt();
        d=new  int[cnt+1];
        System.out.println(make2(cnt));



    }

    static int make1(int n)  //topdown recursion 방식
    {
        if (n==1)      //예외처리
            return 0;
        if (d[n]>0) return d[n];   //메모니제이션(중복 낭비 방지)
        d[n]=make1(n-1) +1;
        if(n%2==0){
            int temp=make1(n/2)+1;
            if (d[n]>temp) d[n]=temp;
        }
        if (n%3==0){
            int temp=make1(n/3)+1;
            if (d[n]>temp) d[n]=temp;
        }

        return d[n];
    }

    static int make2(int n)  //bottomup iteration 방식
    {
        d[1]=0;
        for (int i=2;i<=n;i++)
        {
            d[i]=d[i-1]+1;
            if (i%2==0 && d[i]> d[i/2]+1)
            {
                d[i] = d[i/2] + 1;
            }
            if (i%3==0 && d[i]> d[i/3]+1)
            {
                d[i] = d[i/3] + 1;
            }

        }
        return d[n];
    }




}
