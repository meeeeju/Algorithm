package queue;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class queue {

    public static void main(String[] args) throws IOException {


        //라이브러리 사용 x
        Scanner sc= new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n= sc.nextInt();
        int[] queue = new int[n];
        int front=0,back=0;

        while (n-- >0)
        {
            String cmd=sc.next();
            if (cmd.equals("push")){
                queue[back++]=sc.nextInt();
            }
            else if (cmd.equals("pop")) {
                if (front == back)
                    bw.write("-1\n");
                else {
                    bw.write(queue[front++] + "\n");
                }
            }
            else if (cmd.equals("size"))
                bw.write(back-front+"\n");
            else if (cmd.equals("empty")) {
                if (front==back)
                    bw.write("1\n");
                else
                    bw.write("0\n");
            }
            else if (cmd.equals("front")) {
                if (front ==back)
                    bw.write("-1\n");
                else
                    bw.write(queue[front]+"\n");
            }
            else if (cmd.equals("back")) {
                if (front ==back)
                    bw.write("-1\n");
                else
                    bw.write(queue[back-1]+"\n");
            }

        }
        bw.flush();


        //////////////////////////////////////
        //라이브러리 사용 O
        Scanner sc2=new Scanner(System.in);
        int cnt= sc.nextInt();
        Queue<Integer> queue2= new LinkedList<>();

        for (int k=0;k<cnt;k++){
            String cmd=sc2.next();
            if (cmd.equals("push")){
                queue2.offer(sc2.nextInt());
            }
            else if (cmd.equals("front")) {
                if (queue2.isEmpty()) {
                    System.out.println("-1");
                } else {
                    System.out.println(queue2.peek());
                }
            } else if (cmd.equals("size")) {
                System.out.println(queue2.size());
            } else if (cmd.equals("empty")) {
                if (queue2.isEmpty()) {
                    System.out.println("1");
                } else {
                    System.out.println("0");
                }
            } else if (cmd.equals("pop")) {
                if (queue2.isEmpty()) {
                    System.out.println("-1");
                } else {
                    System.out.println(queue2.poll());
                }
            } else if (cmd.equals("back")) {
                if (queue2.isEmpty()) {
                    System.out.println("-1");
                } else {
                    System.out.println(((LinkedList<Integer>) queue2).get(back-1));
                    // ??? ?? ??... Queue? ??
                }
            }
        }

    }


}
