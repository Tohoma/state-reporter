# state-reporter
A simple web app to generate independent contract reports

This is simply a Web Application extension of a state-reporter script I wrote [here](https://github.com/Tohoma/python-scripts/tree/master/state-reporter).
Being a python script I choose to write the web application using Flask. Aside from Flask the only real dependency is openpyxl.

#What is it?
During my brief stint as an Administrative Assistant for LMU's Controllers office one of my responsiblities were too generate independent contract reports.
Simply every month I would have to create a list of new independent contractors that have conducted business with Loyola Marymount University and send it to the state.
Before I wrote the script I would print up a list of monthly transactions and add them to a different list if the vendor was not previously
reported, their yearly total transaction is over $600 and if they have a valid SSN instead of an Employee Identification Number. I would
then run the list through Word Mailings, print it out and mail it to the state.
Unfortunately LMU deals with hundreds of independent contractors and the task took around 3-4 hours in the past. Now the task
takes about 10-20 minutes due to manually fixing errors.

#Errors?
Unfortunately the format of the list of vendors can be inconsistant somtimes like the following:

     Cross, Peyton K
     123-45-6789            1234 Main St.`
     123456                PASADENA  CA 123456

            XXXXXXLMU                        27-JUL-16           $4,550
                                          YTD Total:       $27,589.48
     Cross-K, Peyton
     123-45-6789            1234 Main St. Apt #5
     123456                PASADENA  CA 123456

            XXXXXXLMU                        27-JUL-16           $4,550
                                          YTD Total:       $27,589.48       
     Cross Industries
     123-45-6789            1234 Main St. A
     123456                PASADENA  CA 123456-3456

            XXXXXXLMU                        27-JUL-16           $4,550
                                             YTD Total:       $27,589.48 
     Cross Brothers
     123-45-6789            1234 Main St. 1/2
     123456                PASADENA  CA 123456

            XXXXXXLMU                        27-JUL-16           $4,550
                                             YTD Total:       $27,589.48 
     Peyton Cross
     123-45-6789            PO BOX 2345
     123456                PASADENA  CA 123456

            XXXXXXLMU                        27-JUL-16           $4,550
                                             YTD Total:       $27,589.48   
                                             
To maintain my sanity and not come up with insanely long regular expressions, whenever the program cannot match the expression
it outputs "ERROR" and I would simply look up the entry manually and enter in the correct information. Also the indpendent report
requires the person's first and lastname not the company. I would have to look that information up anyway.
