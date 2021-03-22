Reverse SSH Tunneling
===
# 1. SSH(Secure Shell)
 보안을 염두해두고 만든 서버-클라이언트 네트워크 프로토콜

# 2. 터널링
<img src="https://www.hanbit.co.kr/data/editor/20160921142829_uiritvqg.gif" width="450px" height="300px" alt="tunneling"/>

+ Host A(클라이언트)에서 Host B(서버)에 접속할 때 보안을 위해 SSH를 통해서 접속함. 
+ 이때 만들어진 연결 통로를 터널이라고 하고 이 과정을 터널링이라고 부름. 
+ 로컬터널링과 리모트 터널링으로 구분됨. 
+ 터널링을 위해서는 SSH가 실행되고 있어야 한다.

## 2.1. 로컬 터널링
### 2.1.1. 개념
<img src="https://www.hanbit.co.kr/data/editor/20160921142857_stfgabxd.gif" width="450px" height="300px" alt="localTunneling"/>   

    $ ssh -L포트번호1:호스트명:포트번호2 서버명

+ 포트번호1 : SSH 클라이언트가 검사하고 있을 포트번호 (application client의 화살표가 가리키고 있는 포트의 번호)
+ 호스트명 : 서버 입장에서의 호스트명 (HostA)
+ 포트번호2 : SSH 서버가 데이터를 보낼 포트번호 (SSH Server의 화살표가 가리키고 있는 포트의 번호)
+ 서버명 : 서버의 이름(HostB)

***
### 2.1.2. 예시 

<img src="https://devbin.kr/wp-content/uploads/2019/12/local-port-forwarding-example.png" width="450px" height="300px" alt="localTunneling"/>

+ 로컬의 8000번 포트를 서버의 80번 포트와 ssh를 통해 연결 시킴.
+ “http://localhost:8000″ 를 통해 서버의 80번 포트와 연결 가능 

***
## 2.2. 리모트 터널링(= 리버스 터널링)
### 2.2.1 개념
<img src="https://www.hanbit.co.kr/data/editor/20160921142913_tqgsllyz.gif" width="450px" height="300px" alt="RemoteTunneling"/>

    $ ssh -R포트번호1:호스트명:포트번호2 서버명

+ 포트번호1 : SSH 서버가 검사하고 있을 포트번호 (application client의 화살표가 가리키고 있는 포트의 번호)
+ 호스트명 : 서버 입장에서의 호스트명 (HostA)
+ 포트번호2 : SSH 클라이언트가 데이터를 보낼 포트번호 (SSH Client의 화살표가 가리키고 있는 포트의 번호)
+ 서버명 : 서버의 이름(HostA)
***
### 2.2.2. 예시
<img src="https://devbin.kr/wp-content/uploads/2019/12/remote-port-forwarding-example.png" width="450px" height="300px" alt="localTunneling"/>

+ 서버의 8000번 포트에 로컬의 80번 포트를 터널링하여 연결시킴.
+ “http://localhost:80″를 통해 서버의 8000번 포트와 연결 가능 
***
### 출처
+ https://devbin.kr/ssh-tunneling-%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-port-forwarding%EC%9D%84-%ED%95%B4%EB%B3%B4%EC%9E%90/
+ https://www.hanbit.co.kr/network/category/category_view.html?cms_code=CMS5064906327
