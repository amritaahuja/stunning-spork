#include<fstream.h>
#include<string.h>
#include<stdio.h>
#include<conio.h>

struct replies
{
	char keyword[10];
	char aioutput[200];
}s;

void input()
{
	cout<<"\n Enter keyword: ";
	cin>>s.keyword;
	cout<<"\n Enter phrase: ";
	gets(s.aioutput);
}
void output()
{
	cout<<"\n Keyword: "<<s.keyword;
	cout<<"\n Phrase: "<<s.aioutput;
}

void writedata()
{
	ofstream ofile("memory.dat",ios::app|ios::binary);
	input();
	ofile.write((char*)&s,sizeof(s));
	ofile.close();
}

void readdata()
{
	ifstream ifile("memory.dat",ios::binary);
	while(ifile.read((char*)&s,sizeof(s)))
	    output();

	ifile.close();
}

void modifydata()
{
	char tword[10];
	int found=0;
	ofstream ofile("temp.dat",ios::binary);
	ifstream ifile("memory.dat",ios::binary);
	cout<<"\n Enter keyword to modify: ";
	cin>>tword;
	while(ifile.read((char*)&s,sizeof(s)))
	  {
		 if(strcmpi(tword,s.keyword)==0)
		    {
				input();
				found++;
			}
		ofile.write((char*)&s,sizeof(s));
	  }
	ifile.close();
	ofile.close();

	remove("memory.dat");
	rename("temp.dat","memory.dat");

	if(found!=0)
		cout<<"\n Keyword Modified";
	else
		cout<<"\n Keyword does not exist";
}


void deletedata()
{
	char tword[10];
	int found=0;
	ofstream ofile("temp.dat",ios::binary);
	ifstream ifile("memory.dat",ios::binary);
	cout<<"\n Enter keyword to delete: ";
	cin>>tword;
	while(ifile.read((char*)&s,sizeof(s)))
	  {
		 if(strcmpi(tword,s.keyword)!=0)
				{
					found++;
					ofile.write((char*)&s,sizeof(s));
				}
	  }
	ifile.close();
	ofile.close();

	remove("memory.dat");
	rename("temp.dat","memory.dat");

	if(found!=0)
		cout<<"\n Keyword deleted";
	else
		cout<<"\n Keyword does not exist";
}


void main()
{
	clrscr();

	int choice;
	do{
		cout<<"\n\n\n\n\t\t\t File operations";
		cout<<"\n\n\t\t\t1.	Add New Record";
		cout<<"\n\n\t\t\t2.	Modify Record";
		cout<<"\n\n\t\t\t3.	Delete Record";
		cout<<"\n\n\t\t\t4.	Display Records";
		cout<<"\n\n\t\t\t5.	Quit";
		cout<<"\n\n\n\n\t\t Enter your choice: ";
		cin>>choice;
		switch(choice)
		 {
			case 1:
						writedata();
						break;
			case 2:
						modifydata();
						break;
			case 3:
						deletedata();
						break;
			case 4:
						readdata();
						getch();
						break;
			case 5:
						break;
			default:
						cout<<"\n Wrong Choice, please try again";
						getch();
		 }
	}while(choice!=5);
}