import java.io.*;

class sol {
    public static int facingSeat(int div,int mod,int n){
	int result=0;
	if(div%2==0){
		if(mod==0)
		{result = n-11;}
		else if(mod==1)
		{result = n+11;}
		else if(mod==2)
		{result = n+9;}		
		else if(mod==3)
		{result = n+7;}
		else if(mod==4)
		{result = n+5;}
		else{result = n+3;}
	}
	else{
		if(mod==0)
		{result = n+1;}
		else if(mod==1)
		{result = n-1;}
		else if(mod==2)
		{result = n-3;}		
		else if(mod==3)
		{result = n-5;}
		else if(mod==4)
		{result = n-7;}
		else{result = n-9;}
	}
	return result;
    }
    public static void main(String args[] ) throws Exception {
	int t,n,facing_seat;
	String seat_position ="";      
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	t = Integer.parseInt(br.readLine());
	for(int i=0;i<t;i++){
		n = Integer.parseInt(br.readLine());
		if(n%6==1||n%6==0)
		{seat_position = "WS";}
		else if(n%6==2||n%6==5)
		{seat_position = "MS";}
		else{seat_position = "AS";}
		if(n==6)
		{facing_seat = n+1;}
		else
		{facing_seat = facingSeat(n/6,n%6,n);}
		System.out.println(facing_seat+" "+seat_position);
	}
    }
}

