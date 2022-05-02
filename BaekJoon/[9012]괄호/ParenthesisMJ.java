//괄호문제 (스택사용하자)
// 1. 닫는 괄호( ')' )를 만났는데, 스택이 비었는 경우 2. 끝났는데 스택이 비지 않았을 경우

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;


public class ParenthesisMJ {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=sc.nextInt();

        while (n-- >0)
        {
            String cmd=sc.next()+"\n";
            int top=0;
            for (char ch: cmd.toCharArray())
            {
                if (ch=='(')
                    top++;
                else if (ch==')')
                {
                    if (top<=0)
                    {
                        bw.write("NO\n");
                        break;
                    }
                    top--;
                }
                else if (ch=='\n')
                {
                    if (top==0)
                        bw.write("YES\n");
                    else
                        bw.write("NO\n");
                }
            }

        }
        bw.flush();
        bw.close();
    }
}


