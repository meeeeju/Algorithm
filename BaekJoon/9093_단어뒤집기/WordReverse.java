//단어 뒤집기 (스택을 사용하자)

import java.io.*;
import java.util.Scanner;
import java.util.Stack;

public class WordReverse {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int t= Integer.parseInt(bf.readLine());  //몇줄 받을 것인지

        while (t-->0)
        {
            String str=bf.readLine()+"\n";
            Stack<Character> s= new Stack<>();
            for (char ch: str.toCharArray()){
                if (ch =='\n' | ch==' ')
                {
                    while(!s.isEmpty())       //isEmpty == empty()
                        bw.write(s.pop());
                    bw.write(ch);
                }
                s.push(ch);
            }
        }
        bw.flush();
    }
}
