/*
 * Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

*/


#include <iostream>

int main()
{
	int num1,num2,temp_num,n,sum=0;

	std::cout<<"Введите число:";
	std::cin>>n;
	std::cout<<"\n";

	num1=1;
	num2=2;

	while(num2<n)
	{
		temp_num=num2;
		num2=num2+num1;
		num1=temp_num;

		if(num2%2==0)
		{
			sum=sum+num2;

		}
		
	
	}
	
	std::cout<<sum+2<<"\n";

	return 0;
	
}
