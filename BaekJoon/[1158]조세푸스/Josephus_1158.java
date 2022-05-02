import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Josephus_1158 {
    public static void main(String[] args) throws IOException {
        Scanner sc= new Scanner(System.in);
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
        int n= sc.nextInt();
        int number=sc.nextInt();
        Queue<Integer> queue=new LinkedList<Integer>();
        for (int i=1;i<=n;i++){
            queue.offer(i);
        }

        bw.write("<");
        int count=1;
        while(!queue.isEmpty()){

            int value=queue.poll();
            if (count==number){
                if (queue.size()==0)
                    bw.write(value+">");
                else
                    bw.write(value+", ");
                count=1;
            }
            else{
                queue.offer(value);
                count++;
            }
        }
        bw.flush();
    }
}
