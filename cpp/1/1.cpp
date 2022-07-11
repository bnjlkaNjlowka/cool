#include <iostream>

int main()
{	int sum=0, n;
	std::cout<<"Введите число:";
	std::cin>>n;
	
	for(int i=1; i<n; i++)
	{
		if(i%3==0||i%5==0)
		{
			sum=sum+i;

		}
	}
	std::cout<<"Сумма чисел кратных 3 и 5 меньше "<<n<<":"<<sum << std::endl;
	return 0;

}
