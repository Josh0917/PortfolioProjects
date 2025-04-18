include <stdio.h>

struct addrinfo{
int                  ai_flags;                //AI_PASSIVE, AI_CANONNAME, etc.
int                  ai_family;               // AF_INT, AF_INET6, AF_UNSPEC
int                  ai_socktype;             //SOCK_STREAM, SOCK_DGRAM
int                  ai_protocol;             //use 0 for "any"
size_t               ai_addrlen;              //size of ai_addr in bytes
struct sockaddr     *ai_addr;   in or _in6;   //struct sockaddr_
char                *ai_canonname;            //full canonical hostname

struct  addrinfo    *ai_next;                 //linked list
};

struct sockaddr {
  unsigned short     sa_family;               //address family
  char               sa_data[14];             //14 bytes
};

struct sockaddr_in{
  short int          sin_family;              //Address family
  unsigned short int sin_port;                //Port Number
  struct in_addr     sin_addr;                //Internet address
  unsigned char      sin_zero[8];             //Same size as struct sockaddr
};

struct in_addr{
  uint32_t s_addr;                            //that's a 32-bit int(4-bytes)
};

struct sockaddr_in6{
  u_int16_t          sin6_family;             //address family
  u_int16_t          sin6_port;               //port number, Network Byte Order
  u_int32_t          sin6_flowinfo;           //IPv6 flow information
  struct in6_addr    sin6_addr;               //IPv6 address
  u_int32_t          sin6_scope_id;           //Scope ID
};

struct in6_addr{
  unsigned char     s6_addr[16];              //IPv6 address
};

struct sockaddr_storage{
  sa_family_t       ss_family;                //address family
  
  //padding
  char              __ss_pad1[_SS_PAD1SIZE];
  int64_t           __ss_align;
  char              __ss_pad2[_SS_PAD2SIZE];
};

struct sockaddr_in  sa;                       //IPv4
struct sockaddr_in6 sa6;                      //IPv6

inet_pton(AF_INET, "10.12.110.57", &(sa.sin_addr)); //IPv4
inet_pton(AF_INET6, "2001:db8:63b3:1::3490", &(sa6.sin6_addr)); //IPv6

//Ipv4

char ip4[INET_ADDRSTRLEN];                    //space to hold the Ipv4 string
struct sockaddr_in sa;                        //pretend this is loaded with something

inet_ntop(AF_INET, &(sa.sin_addr), ip4, INET_ADDRSTRLEN);

printf("The Ipv4 address is: %s\n", ip4);

// Ipv6;

char ip6[INET6_ADDRSTRLEN];                   //space to hold the IPv6 string
struct sockaddr_in6 sa6;                      //pretend this is loaded with something

inet_ntop(AF_INET6, &(sa6.sin6_addr), ip6, INET6_ADDRSTRLEN);

printf("The address is: %s\n", ip6);


int main(void){

return 0;
}
