//스택 구현 (라이브러리 사용 x, 라이브러리 사용 o)
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Stack {


    public static void main(String args[]) throws IOException {


        // 라이브러리 사용 x
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = sc.nextInt();
        int[] stack = new int[n];
        int size = 0;
        while (n-- > 0) {
            String cmd = sc.next();
            if (cmd.equals("push")) {
                int num = Integer.parseInt(sc.next());
                stack[size++] = num;
            } else if (cmd.equals("top")) {
                if (size == 0) {
                    bw.write("-1\n");
                } else
                    bw.write(stack[size - 1] + "\n");
            } else if (cmd.equals("size")) {
                bw.write(size + "\n");
            } else if (cmd.equals("empty")) {
                if (size == 0) {
                    bw.write("1\n");
                } else {
                    bw.write("0\n");
                }
            } else if (cmd.equals("pop")) {
                if (size == 0) {
                    bw.write("-1\n");
                } else {
                    bw.write(stack[size - 1] + "\n");
                    size -= 1;
                }
            }
        }
        bw.flush();


        //라이브러리 사용 o
        Scanner sc2= new Scanner(System.in);
        BufferedWriter bw2=new BufferedWriter(new OutputStreamWriter(System.out));
        int n2=sc.nextInt();
        java.util.Stack<Integer> stack2= new java.util.Stack<Integer>();
        for (int k=0;k<n;k++)
        {
            String cmd=sc.next();
            if (cmd.equals("push")){
                int num=Integer.parseInt(sc2.next());
                stack2.push(num);
            }
            else if (cmd.equals("top")){
                if (stack2.empty())
                    bw.write("-1\n");
                else
                    bw.write(stack2.peek()+"\n");
            }
            else if (cmd.equals("size")){
                bw.write(stack2.size()+"\n");
            }
            else if (cmd.equals("empty")){
                if (stack2.empty()){
                    bw.write("1\n");
                }
                else{
                    bw.write("0\n");
                }
            }
            else if (cmd.equals("pop")){
                if (stack2.empty()){
                    bw.write("-1\n");
                }else
                    bw.write(stack2.pop()+"\n");
            }
        }



    }

}

