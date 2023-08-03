# Leap Year Checker
This program determines if a given year, and a range of years thereafter, are leap years.

How It Works

The program asks for two inputs:

1) A starting year
2) A range (in number of years) to check

It will then loop through each year in that range, determining if each year is a leap year.

The leap year check is done using a binary operation. This operation checks whether the last two bits in the binary representation of the year are unset. This method is adopted from this GeeksforGeeks article, which suggests that this is the most efficient way of checking if a number is a multiple of 4.

Installation

To use this program, simply download the Python file and run it in your Python environment.

Requirements

This program was written in Python and requires Python to run.

Usage

After starting the program, it will ask you for a year to start with. Input the desired year. Then, it will ask you for how many years you want to check. Input the desired range. The program will then print out whether each year in that range is a leap year.

Please note, this program checks leap years based on the Gregorian calendar. According to this calendar, a leap year is any year that is exactly divisible by 4, except for end-of-century years which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

License

This project is licensed under the MIT License.

Acknowledgements
GeeksforGeeks for the method to check if a number is a multiple of 4.
