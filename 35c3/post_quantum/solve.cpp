#include<bits/stdc++.h>
using namespace std;
typedef unsigned char byte;
typedef bitset<16> lbs;
typedef bitset<24> bs;
typedef bitset<48> bbs;
typedef unsigned int uint;

bbs multi(bbs column[], bs key){
  bbs ans(0);
  for(int i=0;i<24;i++){
    if(key[23-i]) ans^=column[i];
  }
  return ans;
}

bbs encode(bbs a){
	bbs ans(0);
  for(int i=0;i<16;i++){
    ans[3*i] = a[i];
    ans[3*i+1] = a[i];
    ans[3*i+2] = a[i];
  }
	return ans;
}

lbs xor3(bbs v){
  lbs ans(0);
  for(int i=0;i<16;i++){
    ans[i] = v[3*i]^v[3*i+1]^v[3*i+2];
  }
  return ans;
}

pair<lbs,lbs> func(int v,bbs pt,bbs ct,bbs column[]) {
  bs key(v);
  bbs res1 = multi(column,key);
  res1 ^= pt;
  lbs k1 = xor3(res1); 
  bbs res2 = multi(column+24,key);
  res2 ^= ct;
  lbs k2 = xor3(res2);
  lbs z(65535);
  k2 ^= z;
  return make_pair(k1,k2);
}


bbs b2b(byte *data,int numBytes){
    bbs b;
    for(int i = 0; i < numBytes; ++i){
        byte cur = data[i];
        int offset = (numBytes-1-i)*8;
        for(int bit = 0; bit<8; ++bit){
            b[offset] = cur & 1;
            ++offset;   // Move to next bit in b
            cur >>= 1;  // Move to next bit in array
        }
    }
    return b;
}



unordered_map<bitset<160>,int> dt1,dt2;
unordered_set<bitset<160>> st1,st2;

bbs pts[2000];
bbs cts[2000];
bbs col[2000][48];

int main() {
  for(int idx=0;idx<1500;idx++){
    FILE *file;
    char name[1000];
    sprintf(name,"data/plaintext_%03d",idx);
    file = fopen(name,"rb");
    unsigned char pt[2],ct[294];
    fread(pt,2,1,file);
    fclose(file);
    sprintf(name,"data/ciphertext_%03d",idx);
    file = fopen(name,"rb");
    fread(ct,294,1,file);
    fclose(file);
    pts[idx] = encode(b2b(pt,2));
    for(int i=0;i<48;i++) {	
      col[idx][i] = b2b(ct+6*i,6);
    }
    cts[idx] = b2b(ct+288,6);
  }
  
  for(int i=0;i<16777216;i++){
    if(i%10000==0) cout<<i<<endl;
    bitset<160>v1(0),v2(0);
    for(int j=0;j<10;j++){
      pair<lbs,lbs>res = func(i,pts[j],cts[j],col[j]); 
      for(int k=0;k<16;k++) v1[16*j+k] = res.first[k];
      for(int k=0;k<16;k++) v2[16*j+k] = res.second[k];
    }
    dt1[v1] = i;
    dt2[v2] = i;
    st1.insert(v1);
    st2.insert(v2);
  }
  int ans=0;
  for(auto x:st1){
    if(st2.find(x)!=st2.end()){
      ans++;
      cout<<dt1[x]<<endl;
      cout<<dt2[x]<<endl;
    }
  }
  cout<<ans<<endl;
}

