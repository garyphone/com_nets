# Creating and using OpenStack SSH keypairs on Linus

On standard cloud images of Linux operating systems like Ubuntu and Fedora SSH access is restricted to public key authentication. Instead of authenticating with a password you authenticate with a private key that corresponds to a public key that is installed on the instance.

## Creating a Keypair

If you haven’t created a key before, start with creating a Keypair in OpenStack:

  1. Go to ‘Access & Security’

  2. Open the ‘Keypairs’ tab 

  3. Click on the Create Keypair button

  4. Choose a Keypair Name
 
  5. You will now be asked to save a .pem file. Save the file on a convenient location. You won’t 
     be able to download it again.

  6. Open a terminal

  7. Correct the file permissions of the .pem file
     '''
     chmod 600 <path/to/file.pem>
     '''


