# Creating and using OpenStack SSH keypairs on Linus

On standard cloud images of Linux operating systems like Ubuntu and Fedora SSH access is restricted to public key authentication. Instead of authenticating with a password you authenticate with a private key that corresponds to a public key that is installed on the instance.

## Creating a Keypair

If you haven’t created a key before, start with creating a Keypair in OpenStack:

  1. Go to ‘Access & Security’

  2. Open the ‘Keypairs’ tab 

  3. Click on the Create Keypair button

  4. Choose a Keypair Name
 
  5. You will now be asked to save a .pem file. Save the file on a convenient location. You won’t 
     be able to download it again

  6. Open a terminal

  7. Correct the file permissions of the .pem file
     ```
     chmod 600 <path/to/file.pem>
     ```

## Inserting a key in a new instance

In order to be able to use the key, you need to insert it in a new instance in OpenStack:

  1. Open the Instances menu on the left

  2. Click on Launch Instance

  3. Choose the relevant options in the Details tab

  4. Select the keypair that you just created

  5. Complete the rest of the wizard

## Associating a floating IP address

To be able to access an instance remotely, a floating IP address needs to be associated to the instance.

  1. Associate a Floating IP address to the instance, by clicking the 'Associate Floating IP' 
     option in the menu on the right

  2. Pick a Floating IP address from the drop down menu. If no address is available, add one by 
     clicking the + button

  3. After the upper steps, you should test, if your floating IP are avaliable. By pinging the 
     floating IP you can see the results

## Modifying the Security Groups

Sometimes the floating IP can not ping correctly, because the security groups can not recognize some rules. So we have to add some specific rules firstly.

  1. Go to ‘Access & Security’

  2. Open the ‘Security Groups’ tab 

  3. Choose the ‘default’ security groups and click on the Manage Rules button

  4. Click on the + Add Rule button
 
  5. Choose Rule as ‘All ICMP’, ‘All TCP’, ‘All UDP’ and click Add button

  6. After the upper steps, you should test, if your floating IP are avaliable. By pinging the 
     floating IP you can see the results

## Using the key with SSH

Now we've prepared a key, started an instance and associated a floating IP we can use the key to login the instance with SSH:

  1. Open a terminal

  2. Start a SSH connection with a command like the one below (default username depends on the 
     image, on Ubuntu the username is simply 'ubuntu'):
     ```
     ssh -i <path/to/file.pem> <username>@<hostname>
     ```
     For example:
     ```
     ssh -i df-kp.pem ubuntu@192.168.115.110
     ```

  3. If you have connected to a server with the same IP address before, you'll receive a message 
     like the one below
     ```
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
     Someone could be eavesdropping on you right now (man-in-the-middle attack)!
     It is also possible that a host key has just been changed.
     The fingerprint for the RSA key sent by the remote host is
     f3:76:dc:b5:cf:87:fc:f0:d9:1d:98:72:65:7f:82:3e.
     Please contact your system administrator.
     Add correct host key in /home/user/.ssh/known_hosts to get rid of this message.
     Offending RSA key in /home/user/.ssh/known_hosts:17
     RSA host key for 10.42.1.28 has changed and you have requested strict checking.
     Host key verification failed.
     ```
     When you're connecting to a new instance you can delete the offending key with this command 
     (change the line number to the one in the warning message):
     ```
     cd ~/.ssh >> 
     sudo gedit known_host
     ```
     You should delete all the things in known_host file

  4. When connecting for the first time you'll be asked the following question. Type 'yes' to 
     continue:
     ```
     The authenticity of host '10.42.1.22 (10.42.1.22)' can't be established.
     ECDSA key fingerprint is e1:92:be:c7:b8:e9:42:35:7a:c6:1f:ed:c1:98:7a:42.
     Are you sure you want to continue connecting (yes/no)?
     ```

  5. If everything works alright you’re now logged in



















