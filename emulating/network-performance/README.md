# Network Performance

**netem** provides Network Emulating functionality for testing protocols by emulating the properties of wide area networks. The current version emulates variable delay, loss, duplication and re-ordering.

Netem is controlled by the command line tool 'tc' which is part of the iproute2 package of tools. The ```tc``` command uses shared libraries and data files in the /usr/lib/tc directory.

## Emulating wide area network delays

This is the simplest example, it just add a fixed amount of delay to all packets going out of the local Ethernet.

   ```
   # tc qdisc add dev ens3 root netem delay 100ms
   ```

Now a simple ping test to host on the local network should show an increase of 100 milliseconds. The delay is limited by the clock resolution of the kernel (HZ). On most 2.4 systems, the system clock runs at 100hz which allows delays in increments of 10ms. On 2.6, the value is a configuration parameter from 1000 to 100 hz.

Later examples just change parameters without reloading the qdisc.

Real wide area networks show variability so it is possible to add random variation.

   ```
   # tc qdisc change dev ens3 root netem delay 100ms 10ms
   ```

This causes the added delay to be 100ms +/- 10ms. Network delay variation is not purely random, so to emulate that there is a correlation value as well.

   ```
   # tc qdisc change dev ens3 root netem delay 100ms 10ms 25%
   ```

This causes the added delay to be 100ms +/- 10ms with the next random elment depending 25% on the last on. This is not true statistical correlation, but an approximation.


