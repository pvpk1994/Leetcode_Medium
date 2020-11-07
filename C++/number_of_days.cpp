// Count number of days between two given dates - Should return exact number of days 
// Author: Pavan Kumar Paluri
#include <iostream>
#include <vector>
using namespace std;
struct date{
	int day;
	int month;
	int year;
};

const int monthDays[12]
    = { 31, 28, 31, 30, 31, 30, 
       31, 31, 30, 31, 30, 31 };

int count_leap_year_days(date d)
{
	// if current year's month is less than february, just dont include it in the count
	if(d.month <= 2)
		d.year-= 1;
	int result = int(d.year/4)+int(d.year/400)-int(d.year/100);
	return result;
}

int number_days(date date1, date date2){
	// logic here is to count days passed since the beginning 00/00/0000
	int days_passed1 = date1.year*365+date1.day;
	for(int i=0; i<date1.month-1;i++)
		days_passed1 += monthDays[i];
	days_passed1 += count_leap_year_days(date1);

	// for date-2
	int days_passed2 = date2.year*365+date2.day;
	for(int i=0; i<date2.month-1;i++)
		days_passed2 += monthDays[i];
	days_passed2 += count_leap_year_days(date2);
	return (days_passed2-days_passed1);

}

int main()
{
	date d1,d2;
	d1.day = 10;
	d1.month = 2;
	d1.year = 2014;

	d2.day = 10;
	d2.month = 3;
	d2.year = 2015;
	cout << number_days(d1, d2) << endl;
	return 0;
}