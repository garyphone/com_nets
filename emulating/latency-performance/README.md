# Latency Performance

Iperf is not a tool to verify the latency in network performance situation. Thus, I should use **ping** as a tool to emulate the latency between two instances in the OpenStack. 

## w/o latency limit in network performance

Directly ping IP address for the server by using following command:
   ```
   ping 192.168.0.111
   ```
Then I can get the results of the network performance as following shows:
   ```
   --- 192.168.0.111 ping statistics ---
   5 packets transmitted, 5 received, 0% packet loss, time 4010ms
   rtt min/avg/max/mdev = 0.669/1.650/3.523/1.012 ms
   ```

## with latency limit by using tc command

With **tc** command I can set the latency limit in client by using following command:
   ```
   tc qdisc add dev ens3 root netem delay 100ms
   ```
> Note: Here I should firstly check the interface name by using command ```ifconfig```, the interface name is ens3, then I can set the latency in this specific interface.

The same results I can obtain as following shows:
   ```
   --- 192.168.0.111 ping statistics ---
   6 packets transmitted, 6 received, 0% packet loss, time 5007ms
   rtt min/avg/max/mdev = 101.774/102.278/102.498/0.441 ms
   ```
It can be verified that the network in such specific interface latency is 102ms.

In order to cancle the limit I should use that command:
   ```
   tc qdisc del dev ens3 root netem
   ```



