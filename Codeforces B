#include <iostream>
/*
#include <string>
#include <deque>
#include "strtk.hpp"
*/
using namespace std;

int main(){
	int n;
	bool r=true;
	
	cin>>n;
	int p[n];int count[n];
	string m[n];

	for(int i=0;i<n;i++){
		cin>>p[i];
		count[i]=0;
	}
	cin.ignore();

	for(int i=0;i<n;i++)
	{
		getline (cin, m[i]);
		for(int j=0;j<m[i].length();j++){
			if(m[i][j]=='a'||m[i][j]=='e'||m[i][j]=='o'||m[i][j]=='u'||m[i][j]=='y'||m[i][j]=='i')
				count[i]++;
		}
		if(count[i] != p[i])
			r=false; 
	}
	if(r)
		cout<<"YES"<<endl;
	else
		cout<<"NO"<<endl;
	return 0;
}
