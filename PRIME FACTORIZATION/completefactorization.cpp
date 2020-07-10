#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <map>
#include <utility>
typedef  long long int ll;
using namespace std;

ll fpower(ll a,ll n){
	ll ans=0;
	if(n==0){
		return 1;
	}
    else if(n==1){
        return a;
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

void concat(vector<ll>&u,vector<ll>&v){
    for(auto x:v){
        u.push_back(x);
    }
    v.clear();
}

ll binexp(ll a,ll n,ll p){
    ll ans=0;
    ll temp=0;
    if(n==1){
        return (a%p+p)%p;
    }
    else{
        ans=binexp(a,n/2,p);
        if(n%2==0){
            return (ans*ans+p)%p;
        }
        else{
            temp=(ans*ans+p)%p;
            return (a*temp+p)%p;
        }

    }
}

string miller_rabintest(ll n,ll a){
    ll z=n-1;
    ll d=z;
    ll x=0;
    ll r=0;
    while(d%2==0){
        d=d/2;
    }
    if(binexp(a,d,n)!=1){
        x=d;
        while(x<n){
            r=binexp(a,x,n);
            if(r==n-1){
                return "Probable Prime";
            }
            else{
                x=2*x;
            }

        }
        return "Composite";
    }
    else{
        return "Probable Prime";
    }

}

bool isprime(ll n){
    vector<int>v;
    if(n%2==0 && n>2){
        return 0;
    }
    else if(n==2){
        return 1;
    }
    else{
        if(n<2047){
            v={2};
        }
        else if(n<1373653){
            v={2,3};
        }
        else if(n<25326001){
            v={2,3,5};
        }
        else if(n<3215031751){
            v={2,3,5,7};
        }
        else if(n<2152302898747){
            v={2,3,5,7,11};
        }
        else if(n<3474749660383){
            v={2,3,5,7,11,13};
        }
         else if(n<341550071728321){
            v={2,3,5,7,11,13,17};
        }
         else if(n<3825123056546413051){
            v={2,3,5,7,11,13,17,19,23};
        }
        else{
            v={2,3,5,7,11,13,17,19,23,29,31,37};

        }
        int i=0;
        while(i<v.size()){
            if(miller_rabintest(n,v[i])=="Probable Prime"){
                i+=1;
            }
            else{
                return 0;
            }

        }
        return 1;
   }
}

ll gcd(ll a,ll b){
    if(a%b==0){
        return b;
    }
    else{
        return gcd(b,a%b);
    }
}

ll pollardrho(ll n){
    if(isprime(n)){
        return n;
    }
    else{
        int a=1+rand();
        ll x=a*a;
        ll y=x;
        ll d=1;
        while(d==1){
             x=(binexp(x,2,n)+1)%n;
             y=(binexp(y,2,n)+1)%n;
             y=(binexp(y,2,n)+1)%n;
             d=gcd(abs(x-y),n);          
             
        }
        if(d==n){
            return pollardrho(n);
        }
        else{
            return d;
        }
    }
}

vector<int> sieveoferathosthenes(int n=1e6+10){
    vector<bool>vec(n+1,1);
    vector<int>primes;
    int j=2;
    int k=0;
    vec[0]=vec[1]=0;
    while(j*j<n+1){
        if(vec[j]){
            k=j*j;
            while(k<n){
                vec[k]=0;
                k+=j;
            }
        }
        j+=1;
    }
    for(int j=0;j<n;j++){
        if(vec[j]){
            primes.push_back(j);
        }

    }
    return primes;
}

vector<ll> factorize(ll n){
    vector<ll>factors;
    if(n==1){
        return factors;
    }
    else if(isprime(n)){
        return {n};
    }
    else{
        ll x=trunc(sqrt(n))+2;
        ll y=1e6+10;
        ll z=min(x,y);
        vector<int>p=sieveoferathosthenes(z);
        for(auto x:p){
            if(n%x==0){
                while(n%x==0){
                    n=n/x;
                    factors.push_back(x);                    
                }
            }
        }
        if(n==1){
            return factors;
        }
        else if(isprime(n)){
            factors.push_back(n);
            return factors;
        }
        else{
            ll fact=pollardrho(n);
            if(isprime(fact)){
                 factors.push_back(fact);
                 factors.push_back(n/fact);
                 return factors;
            }
            else{
                ll temp=fact;
				ll temp1=pollardrho(fact);
				factors.push_back(temp1);
                factors.push_back(fact/temp1);
                factors.push_back(n/fact);
            }
            return factors;
        }


    }
}

map<ll,int>primefactorize(ll n){
    vector<ll> v=factorize(n);
    map<ll,int> pf;
    pair<ll,int>pp;
    for(int i=0;i<v.size();i++){
        if(pf.find(v[i])==pf.end()){
            pp.first=v[i];
            pp.second=1;
            pf.insert(pp);
        }
        else{
            pf[v[i]]+=1;
        }

    }
    return pf;
}

vector<ll>factorsarray(ll n){
    map<ll,int>pfm=primefactorize(n);
    vector<ll>factors;
    vector<ll>ext;
    factors.push_back(1);
    ll ans=0;
    for(auto x:pfm){
       for(int i=1;i<=x.second;i++){
           for(auto y:factors){
                ans=y*fpower(x.first,i);
                ext.push_back(ans);
            }

        }
        concat(factors,ext);

    }
    return factors;

}

int main(){
    ll n;
    cin>>n;
    vector<ll>x=factorsarray(n);
    for(auto i:x){
        cout<<i<<'\t';
    }
}

