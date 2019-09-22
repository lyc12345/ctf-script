#include <openssl/evp.h>

#include <unordered_set>
#include <iostream>
#include <fstream>

#include <unistd.h>

#define EVP_CREATE_FN() EVP_MD_CTX_create()
#define EVP_DESTROY_FN(x) EVP_MD_CTX_cleanup(x)
typedef std::unordered_set<std::string> stringset;
std::unordered_set<std::string> values;
stringset::hasher fn;

std::string sha512sum(const std::string& name, const std::string& password) {
  const EVP_MD *md;
  unsigned int md_len;

  md = EVP_get_digestbyname("sha512");

  // Do two sha512 rounds to double the number of security.
  EVP_MD_CTX *mdctx0;
  unsigned char md_value0[EVP_MAX_MD_SIZE];
  mdctx0 = EVP_CREATE_FN();
  EVP_MD_CTX_init(mdctx0);
  EVP_DigestInit_ex(mdctx0, md, NULL);
  EVP_DigestUpdate(mdctx0, name.c_str(), name.size());
  EVP_DigestFinal_ex(mdctx0, md_value0, &md_len);
  EVP_DESTROY_FN(mdctx0);

  unsigned char md_value1[EVP_MAX_MD_SIZE];
  EVP_MD_CTX *mdctx1;
  mdctx1 = EVP_CREATE_FN();
  EVP_MD_CTX_init(mdctx1);
  EVP_DigestInit_ex(mdctx1, md, NULL);
  EVP_DigestUpdate(mdctx1, md_value0, md_len);
  EVP_DigestUpdate(mdctx1, password.c_str(), password.size());
  EVP_DigestFinal_ex(mdctx1, md_value1, &md_len);
  EVP_DESTROY_FN(mdctx1);

  return std::string(reinterpret_cast<char*>(md_value1), md_len);
}


int bucket(std::string a, std::string b){
  std::string digest = sha512sum(a,b);
  return fn(digest)%15173;
}
using namespace std;
int main() {
  int cnt = 0;
	OpenSSL_add_all_digests();
	values.reserve(15000);
  fn = values.hash_function();
	int a = bucket("root", "a");
  for(int i=0;i<16000000;i++){
    int b = bucket("a",std::to_string(i));
    if(b==a) {
      std::cout << i << std::endl;
      cnt += 1;
    }
  }
  cout << cnt << endl;
}
