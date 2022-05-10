# Damn Vulnerable DeFi
[Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/) 是由@tinchoabbate設計出來的題目, 讓挑戰者挑戰從體目中尋找智能合約的漏洞, 進而了解如何寫出更安全的代碼

# 前言
原網站的做法是使用JavaScript運行, 因為最近開始學習solidity跟web3.py, 因此嘗試使用Python從部署到實作, 希望可以學習智能合約安全的撰寫方式也可以更了解完整的流程, 其中目前總共12題：
    1	Unstoppable
    2	Naive receiver
    3	Truster
    4	Side entrance
    5	The rewarder
    6	Selfie
    7	Compromised
    8	Puppet
    9	Puppet v2
    10	Free rider
    11	Backdoor
    12	Climber

## 環境(Env)
環境上使用Ganache建立虛擬的區塊, 以Python為基礎, 利用web3.py進行部署與智能合約的調用, 詳細內容如下：
- @openzeppelin模組
```commandline
>>cd contracts
>>git clone https://github.com/OpenZeppelin/openzeppelin-contracts.git
```
- web3
```commandline
pip install web3
```
* 安裝web3.py 時錯誤(mac): 
```commandline
xcode-select --install
```  
- (Ganache)[https://trufflesuite.com/ganache/]



