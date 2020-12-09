#                Assignment-1        (5065424,Rohit Adapa)
# Program composd by two processes using pipes
In this program the user inputs two numbers A and B, random signal is sent through the pipe, every time when a signal is sent it computes the sum  of A and B and increment with respect to last time and the out put is stored in a output file in xlsx format
# Installing and running
Before excuting the code Machine requires a python 3 installation in the machin and few libraries required they are pandas,time,datetime,random and string.

script to install required libraries (Copy paste the below line in the shell)

$ pip3 install pandas && pip3 install time && pip3 install datetime && pip3 install random && pip3 install string

Once the libraries are installed, run the script using (Copy paste the below line in the shell) 

$ python3 arp1.py
# Short explanation of the code
Two numbers a&b should be entered by the user manually  and the program generates the random letters using random letter genaerator , which we are using as signals for excuting the code . After generating of each letter a loop of program excutes and the sum of a&b are incermented, this loop continious until the random letter generates "z" or "Z". According to the user requirement the letter "Z" or "z" can be changed according to the user prefrences, but this letter shouls be replaced in the code it self which can be identified easily , once every thing is done program can be saved and excuted And the output of the program is displayed in shell and also stored in a .xlsx file.
