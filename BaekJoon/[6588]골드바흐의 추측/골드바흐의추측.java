import java.io.*;
import java.util.ArrayList;

//에라토스테네스의 체


public class 골드바흐의추측 {

    public static final int MAX = 1000000;
    public static void main(String[] args) throws IOException {
//        Scanner sc=  new Scanner(System.in);
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));


//        int n=sc.nextInt();
        int n=Integer.parseInt(br.readLine());
        boolean[] checkedList=new boolean[MAX+1];    //만약을 대비해서 checkedList[0]=1 checkedList[1]=1 처리해주기
        ArrayList<Integer> prime = new ArrayList<Integer>();

        checkedList[0]=true;
        checkedList[1]=true;
        int pn=0; //소수의 갯수

        for (int i=2;i<=MAX;i++)
        {
            if (checkedList[i])   //true면 소수 아님
                continue;
            prime.add(i);
            for (int j=2*i;j<=MAX;j+=i)    // j= j + i
            {
                checkedList[j]=true;
            }
        }

        while (n!=0)
        {
            for (int i=0;i<prime.size();i++)
            {
                if (checkedList[n-prime.get(i)]==false)
                {
                    bw.write(n+" = "+prime.get(i)+" + "+(n-prime.get(i))+"\n");
                    break;
                }
            }
            n=Integer.parseInt(br.readLine());
//          n=sc.nextInt();
        }

        bw.flush();
    }
}
