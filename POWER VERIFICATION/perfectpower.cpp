#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include<utility>
typedef  long long int ll;
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

pair<ll,ll> binarysearch(ll left,ll right,ll b,ll n){
    ll mid=(left+right)/2;
    ll l=fpower(left,b);
    ll r=fpower(right,b);
    ll m=fpower(mid,b);
    if(l==n){
        return {left,b};
    }
    else if(r==n){
        return {right,b};
    }
    else if(m==n){
        return {mid,b};
    }
    else if(m<n && n<r){
        return binarysearch(mid+1,right,b,n);
    }
    else if(l<n && n<m){
        return binarysearch(left,mid-1,b,n);
    }
    else{
        pair<ll,ll>p;
        p.first=-1;
        p.second=-1;
        return p;
    }
}

pair<ll,ll>checkperfectpower(ll n){

    ll x=trunc(log(n)/log(2))+1;
    ll y=trunc(sqrt(n))+1;
    ll i=2;
    while(i<x){
        pair<ll,ll>vec=binarysearch(2,y,i,n);
        if(vec.first==-1 && vec.second==-1){
            i+=1;
        }
        else{
            return binarysearch(2,y,i,n);
        }
    }
    pair<ll,ll>q;
        q.first=-1;
        q.second=-1;
        return q;
    return q;

}

string perfectpower(ll n){
    pair<ll,ll>v=checkperfectpower(n);
    string s;
    if(v.first==-1 && v.second==-1){
        s="Not Perfect Power";
    }
    else{
        s="("+to_string(v.first)+","+to_string(v.second)+")";
    }
    return s;
}

int main(){
    ll n=1024;
    cout<<perfectpower(n)<<"\n";
}



    




