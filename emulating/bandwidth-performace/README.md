# Bandwidth Performace Emulating

Linux systems administrators and network administrators often find diagnosing network speed degradation complicated, as there are very few tools avaliable to diagnose these issues. Iperf is command-line tool used in the diagnostics of network speed issues.

Iperf measures the maximum network throughput a server can handle. It is particularly useful when experiencing network speed issues, as you can use Iperf to determine which server is unable to reach maximum throughput.

## Installing Iperf

> The installation section assumes that you are the root user. If you are not using the super user, you will need to use sudo before each command. Here I use Ubuntu or Debian OS.

You can use apt-get to install Iperf on Debian and Ubuntu:
     ```
     apt-get install iperf
     ```

## Using Iperf

Iperf must be installed on both computers you are testing the connection between. If you are using a Unix or Linux-based operating system on your personal computer, you may be able to install Iperf on your local machine. 

### TCP Clients&Servers 

Iperf requires two systems because one system must act as a server, while the other acts as a client. The client connects to the server you are testing the speed of. If you are testing the throughput of your Linode, however, it is better to use another server as the end point, as your local ISP may impose network restrictions that can affect the results of your test.

  1. On the Linode you wish to test, launch Iperf in server mode:
     ```
     iperf -s
     ```
     You should see output similar to:
     ```
     ------------------------------------------------------------
     Server listening on TCP port 5001
     TCP window size: 85.3 KByte (default)
     ------------------------------------------------------------
     ```

  2. On your second Linode, connect to the first. Replace 198.51.100.5 with the first Linode’s IP
     address.
     ```
     iperf -c 198.51.100.5
     ```
     The output should be similar to:
     ```
     ------------------------------------------------------------
     Client connecting to 198.51.100.5, TCP port 5001
     TCP window size: 45.0 KByte (default)
     ------------------------------------------------------------
     [  3] local 198.51.100.6 port 50616 connected with 198.51.100.5 port 5001
     [ ID] Interval       Transfer     Bandwidth
     [  3]  0.0-10.1 sec  1.27 GBytes  1.08 Gbits/sec
     ```

  3. You will also see the connection and results on your Iperf server. This will look similar to:
     ```
     ------------------------------------------------------------
     Server listening on TCP port 5001
     TCP window size: 85.3 KByte (default)
     ------------------------------------------------------------
     [  4] local 198.51.100.5 port 5001 connected with 198.51.100.6 port 50616
     [ ID] Interval       Transfer     Bandwidth
     [  4]  0.0-10.1 sec  1.27 GBytes  1.08 Gbits/sec
     ```

  4. To stop the Iperf server process, press CTRL + c.

## UDP Clients&Servers

Using Iperf, you can also test the maximum throughput achieved via UDP connections.

  1. Start a UDP Iperf server:
     ```
     iperf -s -u
     ```
     The output will be similar to:
     ```
     ------------------------------------------------------------
     Server listening on UDP port 5001
     Receiving 1470 byte datagrams
     UDP buffer size:  208 KByte (default)
     ------------------------------------------------------------
     ```

  2. Connect your client to your Iperf UDP server. Replace 198.51.100.5 with your IP address:
     ```
     iperf -c 198.51.100.5 -u
     ```
     The -u option we’ve passed tells Iperf that we are connecting via UDP. This is important, because we want to see the maximum throughput achieved via UDP. The output should be similar to:
     ```
     ------------------------------------------------------------
     Client connecting to 198.51.100.5, UDP port 5001
     Sending 1470 byte datagrams
     UDP buffer size:  208 KByte (default)
     ------------------------------------------------------------
     [  3] local 198.51.100.6 port 58070 connected with 198.51.100.5 port 5001
     [ ID] Interval       Transfer     Bandwidth
     [  3]  0.0-10.0 sec  1.25 MBytes  1.05 Mbits/sec
     [  3] Sent 893 datagrams
     [  3] Server Report:
     [  3]  0.0-10.0 sec  1.25 MBytes  1.05 Mbits/sec   0.084 ms    0/  893 (0%)

     ```
     Looking at the output we have received, 1.05 Mbits/sec is considerably less than what we received on the TCP tests. It is also considerably less than the maximum outbound bandwidth cap provided by the 1GB Linode. This is because Iperf limits the bandwidth for UDP clients to 1 Mbit per second by default.

  3. You can change this with the -b flag, replacing the number after with the maximum bandwidth rate you wish to test against. If you are testing for network speed, we recommend setting this number above the maximum bandwidth cap provided by Linode. For example, this test was run on a 1GB Linode:
     ```
     iperf -c 198.51.100.5 -u -b 1000m
     ```
     This tells the client that we want to achieve a maximum of 1000 Mbits per second if possible. The -b flag only works when using UDP connections, since Iperf does not set a bandwidth limit on the TCP clients.
     The output should be similar to:
     ```
     ------------------------------------------------------------
     Client connecting to 198.51.100.5, UDP port 5001
     Sending 1470 byte datagrams
     UDP buffer size:  208 KByte (default)
     ------------------------------------------------------------
     [  3] local 198.51.100.5 port 52308 connected with 198.51.100.5 port 5001
     [ ID] Interval       Transfer     Bandwidth
     [  3]  0.0-10.0 sec   966 MBytes   810 Mbits/sec
     [  3] Sent 688897 datagrams
     [  3] Server Report:
     [  3]  0.0-10.0 sec   966 MBytes   810 Mbits/sec   0.001 ms    0/688896 (0%)
     [  3]  0.0-10.0 sec  1 datagrams received out-of-order
     ```
     Now that is considerably better than the 1.05 Mbits/sec we were seeing earlier!




















