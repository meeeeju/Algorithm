### 분류 : DP
### 문제이름 : [1로 만들기](https://www.acmicpc.net/problem/1463) 
</br>

### 로직 : 
문제에서 주어진 조건대로 점화식을 잘 세우면 된다. DP의 의미를 잘 생각해보자.  

    D[n]= m(D[n-1],D[n/2],D[n/3])+1
 
 
 ### RV : 
  입력값의 범위를 잘 보자, 문제에서 1부터 10^6이라고 했으니 정수 배열 D를 n+1 까지 받아주던가 아님 D[1000001] 까지 만들어줘야한다.
         이상한 곳에서 오류를 만들어내지 말자 ㅠ
