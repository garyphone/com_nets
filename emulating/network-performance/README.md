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

## Delay distribution

Typically, the delay in a network is not uniform. It is more common to use a something like a normal distribution to describe the variation in delay. The netem discipline can take a table to specify a non-uniform distribution

   ```
   # tc qdisc change dev ens3 root netem delay 100ms 20ms distribution normal
   ```

The actual tables (normal, pareto, paretonormal) are generated as part of the iproute2 compilation and placed in /usr/lib/tc; so it is possible with some effort to make your own distribution on experimental data.

## Packet loss

Random packet loss is specified in the 'tc' command in percent. The smallest possible non-zero value is: 2^32 = 0.0000000232%

   ```
   # tc qdisc change dev ens3 root netem loss 0.1%
   ```

This causes 1/10th of a percent (i.e 1 out of 1000) packets to be randomly dropped.

An optional correlation may also be added. This causes the random number generator to be less random and can be used to emulate packet burst losses.

   ```
   # tc qdisc change dev ens3 root netem loss 0.3% 25%
   ```

This will cause 0.3% of packets to be lost, and each successive probability depends by a quarter on the last one.

Prob(n) = .25 * Prob(n-1) + .75 * Random

> Note: When loss is used locally (not on a bridge or router), the loss is reported to the upper level protocols. This may cause TCP to resend and behave as if there was no loss. When testing protocol reponse to loss it is best to use a netem on a bridge or router.








