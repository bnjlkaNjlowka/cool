#include <iostream>

/*Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом? */


int main()
{
	int delt=2,max_delt=0;
	unsigned long long ans;

	std::cout<<"Введите число:";
	std::cin>>ans;
	std::cout<<"\n";

	while(ans!=1)
	{
		if(ans%delt!=0)
		{
			delt=delt+1;
		}
		else
		{
			ans=ans/delt;

			if(delt>max_delt)
			{
				max_delt=delt;
			
			}
		
		}
	}
	
	std::cout<<max_delt<<"\n";
	return 0;
}
