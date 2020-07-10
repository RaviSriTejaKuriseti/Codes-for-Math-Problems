#include <iostream>
#include <cmath>
typedef long long int ll;
using namespace std;

ll fpower(ll a,ll n){
	ll ans=0;
	if(n==0){
		return 1;
	}
	else{
		ans=fpower(a,n/2);
		if(n%2==0){
			return ans*ans;
		}
		else{
			return a*ans*ans;
		}
	}
}

bool binarysearch(ll left,ll right,ll m,ll n){
    ll mid=sqrt(left*right);
    if(left==n){
        return 1;
    }
    else if(right==n){
        return 1;
    }
    else if(mid==n){
        return 1;
    }
    else if(mid<n && n<right){
        return binarysearch(mid*m,right,m,n);
    }
    else if(left<n && n<mid){
        return binarysearch(left,mid/m,m,n);
    }
    else{
        return 0;
    }
}



bool ispower(ll m,ll n){
    if(m==n){
        return 1;
    }
    else if(n%m!=0){
        return 0;
    }
    else{
        return ispower(m,n/m);
    }

}

bool ispowerefficient(ll m,ll n){
    if(m==n){
        return 1;
    }
    else if(m>n){
        return 0;
    }
    else{
        ll x=m*m;
        while(x<n){
            x=x*x;            
        }
        ll y=sqrt(x);        
        return binarysearch(y,x,m,n);    


    }

}


int main(){
    ll x,z;
    cin>>x;
    cin>>z;
    bool y=ispowerefficient(x,z);
    cout<<y<<"\n";
}






