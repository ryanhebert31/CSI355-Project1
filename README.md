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
#### a 

#### b 

#### c


#### d

#### e 

### P28 


### 2 - Questions
#### a 


#### b 


#### c 
`255.255.248.0`

#### d 
`/19`

### 3 - Routing

### 4 - Command Line 
#### Get IP Address
``` 
ipconfig getifaddr en0
```
#### Get Hostname
```
hostname
````
###$ Get Subnet ID, Prefix, Subnet Mask
```
netstat -r 
```
#### Get Routing Table
```
netstat -r 
```
#### Get ARP Table
```
arp -a 
```

### 5 - Network Trace
#### a
The trace captures data flowing through the machine on the network. Each line corresponds to a packet of data with a source and a destination. 
#### b 
```
tcpdump
```
#### c 
The hostname is the host of the machine running the command. In this case, the IP address assigned to my computer. 
#### d 
By inspecting one packet, the destination was listed as `Destination: JuniperN_5a:d8:e0 (88:a2:5e:5a:d8:e0)`
#### e
? 

### Bonus
#### a 
On my iPhone, I was able to find the IP address `192.168.57.187`, Subnet Mask `255.255.255.0` and Subnet ID `192.168.57.1` via the cellular settings. I wasn't able to generate any tables from the phone. 
#### b
I was able to create a WireShark filter for only packets using TCP protocol. To do so I named a filter "Test TCP" and filtered on messages containing TCP tags. See the data tump attached. 
