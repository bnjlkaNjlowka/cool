#include <iostream>
#include <string>

/* Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

*/

int check_palindrom(int num1)
{	
	std::string str_num1;
	str_num1=std::to_string(num1);
	int kolvo=str_num1.size();

	for(int i=0;i<=kolvo/2;i++)
	{
		if(str_num1[i]!=str_num1[kolvo-1-i])
		{
			return 1;
		}

	}

	return 0;
}

int main()
{
	int max_palindrom=0;

	for(int i1=100;i1<1000;i1++)
	{
		for(int i2=100;i2<1000;i2++)
		{
			int num=i1*i2;
			int check=check_palindrom(num);
			
			if(check==0 && max_palindrom<num)
			{
				max_palindrom=num;
			}
		}
	}
	std::cout<<"Самый большой палиндром, полученный умножением двух трехзначных чисел: "<<max_palindrom<<"\n";
	return 0;
}
