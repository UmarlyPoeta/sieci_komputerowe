# Patryk Kozłowski nr. albumu 422434 gr. IV

# nmap
1. wymień 3 dowolne skanowania:
- sV - scanuje i podaje wersje usług
- sn - scanuje i pinguje czy są UP czy DOWN
- sO - scanuje i sprawdza jakie mają OS

2. wymień 4 znanych portów:
- 20/21 FTP TCP
- 25 SMTP TCP
- 22 SSH TCP
- 80 HTTP TCP


# nat
1. czym jest nat:
NAT zamienia adresy prywatne na adresy publiczne, co pozwala zaoszczędzić liczną ilość adresów w sieci, co było problemem z IPv4. Tak naprawdę NATem dzisiaj nazywamy NAPT, który tak samo mógł zmieniać porty

2. adres publiczny a prywatny, przedstaw przykładowe pule adresów prywatnych:

adresy publiczne różnią się od adresów prywatnych tym, że adresy prywatne mogą się powtarzać w sieci

pule adresów prywatnych:
192.168.0.0 /16 
172.16.0.0 / 16
10.0.0.0 / 8

# wireshark

1. za co odpowiada pole TTL w nagłówku datagramu IP:
TTL czyli time to live to pole, które stwierdza ile hopów pakiet będzie przesyłany między routerami.
Za każdym razem jak router dostaje pakiet, dekrementuje ttl zanim go prześle dalej.


2. Co to jest socket, co się na niego składa:
Socket to dana usługa zbudowana z adresu i portu oraz usługi którą świadczy, która za pomocą port forwardingu ma dostęp do internetu.