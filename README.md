# Homework 1
## Ryan Hebert & Ben Kohler
### 09.07.2021
Problem Set 1

### 1 - Chapter 1
#### R16 
Processing, Queuing, Transmission, Propogation. Constant variables include processing, propogation and transmission while queuing is constant. 
#### R22 
Tasks include error and flow control, segmentation and reassembly, multiplexing, and connection setup. Some tasks are able to be completed at multiple levels. For example, error control is often completed at more than one layer. 
### P25
R = 2 000 000bps       Prop speed = 2.5 * 10^8m/s      Distance (Link Length) = 20 000 000m
#### a 
`2,000,000 * (20,000,000)/(2.5*10^8) = 160,000 bits`

#### b
`160,000 bits` as the bandwith delay product is the maximum number of bits to be transported at one time.

#### c
The maximum number of bits that can be on the link at one time. 

#### d
125 m
`(20,000,000)/(160,000) = 125m`
125m > 92m (size of football field in meters)

#### e 
`Bit width = Distance/(Bandwidth Delay Product) = m/(R*m/s) = 1/(R*1/s) = s/R`

### P28 
#### a
Time without delay = `(File size)/Rate = (800,000)/(2,000,000) = 0.4s`
Time of delay = `(Bandwidth delay product)/Rate = (160,000)/(2,000,000) = 0.08s`
Time taken =  `0.4 * 0.08 = 0.48s`

#### b 
Time per packet without delay = `(40,000)/(2,000,000) = 0.02s1
Total time = 1num_packets * (time_without_delay + delay) = 20 * (0.02 + 0.08) = 20 * 0.1 = 2s`

#### c 
Breaking up data into multiple packets took longer in this example than transferring it continuously because of each packet's propagation delay and validation step. 

### 2 - Questions
#### a 
`137.146.12.192 - 137.146.12.207`

#### b 
`/25` 
Given 128 addresses cover the range `10.20.30.12 - 10.20.30.123` and `2^7 = 128` and `32-7 = 25`

#### c 
`255.255.248.0`
Given `32 - x = 21, x = 11`, therefore `11111111 11111111 11111000 00000000` writen in decimal is `255.255.248.0`

#### d 
`/19`
Given `255.255.224.0` written in binary is `11111111 11111111 11100000 00000000` and `32 - 13 = 19`. 

### 3 - Routing
A `132.177.21.0/24` = `11111111 11111111 11111111 00000000`
B `132.177.20.0/22` = `11111111 11111111 11111100 00000000`
C `132.177.0.0/16` = `11111111 11111111 00000000 00000000`
D `0.0.0.0/0` = `00000000 00000000 00000000 00000000`

#### 132.176.20.1
Binary: `10000100 10110000 00010100 00000001`
Routs to: `D`

#### 132.177.20.2
Binary: `10000100 10110001 00010100 00000010`
Routs to: `B`

#### 132.177.21.3
Binary: `10000100 10110001 00010101 00000011`
Routs to: `A`

#### 132.177.22.4
Binary: `10000100 10110001 00010110 00000100`
Routs to: `B`

#### 132.177.37.5
Binary: `10000100 10110001 00100101 00000101`
Routs to: `C`

### 4 - Command Line 
```
(base) ryanhebert@Ryans-MBP-2 ~ % ipconfig getifaddr en0
192.168.1.55
(base) ryanhebert@Ryans-MBP-2 ~ % dig +short -x 192.168.1.55
Ryans-MBP-2.
(base) ryanhebert@Ryans-MBP-2 ~ % arp -a
g3100.myfiosgateway.com (192.168.1.1) at b8:f8:53:6e:38:d9 on en0 ifscope [ethernet]
esp_f9fc9a (192.168.1.34) at 10:52:1c:f9:fc:9a on en0 ifscope [ethernet]
christiplewatch (192.168.1.53) at 40:70:f5:f:7a:96 on en0 ifscope [ethernet]
christinsiphone (192.168.1.98) at 92:58:85:37:97:6a on en0 ifscope [ethernet]
quinns-iphone (192.168.1.99) at 1a:38:93:f8:7:b7 on en0 ifscope [ethernet]
samsung (192.168.1.156) at 2:f:b5:72:99:70 on en0 ifscope [ethernet]
iphone (192.168.1.195) at da:b2:4b:81:88:14 on en0 ifscope [ethernet]
? (192.168.1.213) at 16:f6:5d:77:1:74 on en0 ifscope [ethernet]
wills-mbp (192.168.1.217) at 14:7d:da:75:e9:9f on en0 ifscope [ethernet]
jennifersiphone (192.168.1.223) at 2:f:b5:c2:ba:c1 on en0 ifscope [ethernet]
brianmaosiphone (192.168.1.231) at 72:d4:d1:63:6:70 on en0 ifscope [ethernet]
ex6120 (192.168.1.250) at 2:f:b5:45:26:4a on en0 ifscope [ethernet]
? (192.168.1.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
(base) ryanhebert@Ryans-MBP-2 ~ % curl ifconfig.me
100.19.28.89%  

Routing tables

Internet:
Destination        Gateway            Flags        Netif Expire
default            g3100.myfiosgatewa UGScg          en0       
127                localhost          UCS            lo0       
localhost          localhost          UH             lo0       
169.254            link#12            UCS            en0      !
192.168.1          link#12            UCS            en0      !
192.168.1.1/32     link#12            UCS            en0      !
g3100.myfiosgatewa b8:f8:53:6e:38:d9  UHLWIir        en0   1192
esp_f9fc9a         10:52:1c:f9:fc:9a  UHLWI          en0   1195
christiplewatch    40:70:f5:f:7a:96   UHLWI          en0    132
192.168.1.55/32    link#12            UCS            en0      !
christinsiphone    92:58:85:37:97:6a  UHLWIi         en0    105
quinns-iphone      1a:38:93:f8:7:b7   UHLWI          en0    543
samsung            2:f:b5:72:99:70    UHLWI          en0     26
iphone             da:b2:4b:81:88:14  UHLWI          en0    477
192.168.1.213      16:f6:5d:77:1:74   UHLWI          en0   1019
wills-mbp          14:7d:da:75:e9:9f  UHLWI          en0   1125
jennifersiphone    2:f:b5:c2:ba:c1    UHLWI          en0      !
brianmaosiphone    72:d4:d1:63:6:70   UHLWI          en0    507
ex6120             2:f:b5:45:26:4a    UHLWI          en0     88
192.168.1.255      ff:ff:ff:ff:ff:ff  UHLWbI         en0      !
224.0.0/4          link#12            UmCS           en0      !
224.0.0.251        1:0:5e:0:0:fb      UHmLWI         en0       
255.255.255.255/32 link#12            UCS            en0      !
```

### 5 - Network Trace
#### a
The trace captures data flowing through the machine on the network. Each line corresponds to a packet of data with a source and a destination. 
#### b 
```
tcpdump
```
#### c 
The hostname is the host of the machine running the command. In this case, the IP address assigned to my computer has the assigned hostname Ryan-mac. 
#### d 
Using a DHCP filter, there's a hostname field. Tracing my network traffic did not yield any packets that matched this field. [This article](https://unit42.paloaltonetworks.com/using-wireshark-identifying-hosts-and-users/) shows the steps to find hostname.
#### e
Manufacture card is available in the EthernetII dropdown under Source. Ours says `Source: Apple_ae:da:21 (c4:91:0c:ae:da:21)`. 

### Bonus
#### a 
On my iPhone, I was able to find the IP address `192.168.57.187`, Subnet Mask `255.255.255.0` and Subnet ID `192.168.57.1` via the cellular settings. I wasn't able to generate any tables from the phone. 
#### b
I was able to create a WireShark filter for only packets using TCP protocol. To do so I named a filter "Test TCP" and filtered on messages containing TCP tags. See the data dump attached. 
