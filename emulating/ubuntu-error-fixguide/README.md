# Ubuntu Error Fixguide

In this guide I would like to write down some ubuntu system errors and try to fix them.

## Reading package lists Error

When I run 
   ```
   sudo apt-get install iperf
   ```
I get this error:
   ```
   Reading package lists... Error!
   E: Unable to parse package file /var/lib/dpkg/status (1)
   E: The package lists or status file could not be parsed or opened.
   ```

Solution:

   ```
   sudo rm /var/lib/apt/lists/* -vf
   sudo apt-get clean
   sudo apt-get update
   ```
