/*2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?

*/

#include <iostream>

int check_delimist(int num,int delt)
{	
	for(int i=1;i<=delt;i++)
	{
		if(num%i!=0)
		{
			return 1; // не делится
		}
	}
	return 0; // делится
}


int main()
{
	int num=0,delt,ans=1;
	std::cout<<"Введите максимальный делитель:";
	std::cin>>delt;
	std::cout<<"\n";
	
	while(ans!=0)
	{
		num=num+20;
		ans=check_delimist(num,delt);
		
	}

	std::cout<<"Самое маленькое число, которое делится на все числа от 1 до "<<delt<<":"<<num<<"\n";
	return 0;
}

