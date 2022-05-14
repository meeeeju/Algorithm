import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class 소수_1978 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));

        int N= sc.nextInt();
        int num,count=0;


        while (N-->0)
        {
            num=sc.nextInt();
            if (prime(num)){
                count ++;
            }
        }

        System.out.println(count);

    }


    static boolean prime(int n)
    {
        if (n<2)
            return false;
        else {
            for (int i=2;i*i<=n;i++)
            {
                if (n%i==0)
                    return false;
            }
            return true;
        }

    }

}
