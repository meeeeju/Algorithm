import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;

//에라토스테네스의 체

public class 소수구하기_1929 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
        int M= sc.nextInt();
        int N= sc.nextInt();
        boolean[] checkedList=new boolean[N+1];    //만약을 대비해서 checkedList[0]=1 checkedList[1]=1 처리해주기

        int [] prime= new int[N];
        int pn=0; //소수의 갯수


        for (int i=2;i<=N;i++)
        {
            if (!checkedList[i])
                prime[pn++]=i;
            for (int j=2*i;j<=N;j+=i)    // j= i +i
            {
                checkedList[j]=true;
            }
        }

        for (int i=0;i<pn;i++)
        {
            if (prime[i]>=M)
            {
                System.out.println(prime[i]);
            }
        }

    }

}
