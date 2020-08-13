// Given 2 year, month, day: Calculate number of days between them
// Author: Pavan Kumar Paluri

#include <iostream>
#include <vector>
using namespace std;
int leap_year_days(int year, int month)
{
  if(month <= 2)
  {
    year -= 1;
  }
  // a leap year if: A multiple of 4, A multiple of 400 and not a multiple of 100
  int extra_days = year/4;
  extra_days = extra_days-year/100;
  extra_days = extra_days+year/400;
  return extra_days;

}

int count_days_in_month(int year1, int month1,int day1, int year2, int month2, int day2)
{
  // Return number of days between given dates
  const int month_days[12] ={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  // calculate total number of days between def (0000-00-00) and given dates
  // if not a leap year:
  long int n1 = year1*365+day1;
  // now add months
  for(int i=0; i<month1-1; i++)
  {
    n1 += month_days[i]; 
  }

  // now leap years 
  n1 += leap_year_days(year1, month1);

  long int n2 = year2*365+day2;
  // now add months
  for(int i=0; i<month2-1; i++)
  {
    n2 += month_days[i]; 
  }

  // now leap years 
  n2 += leap_year_days(year2, month2);
  return n2-n1;        
}

int main() {
  // std::cout << "Hello World!\n";
  int no_days = count_days_in_month(2000, 2, 1, 2004, 2, 1);
  cout << no_days << endl;
}
