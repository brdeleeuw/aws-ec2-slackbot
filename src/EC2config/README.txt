# The ec2-config.sh script automates the configuration of an already launched EC2 instance
# First, adjust the desired packages, directories, repos etc. to install in the .sh file
# Then copy ec2-config.sh to the remote instance (e.g. by using Filezilla) 
# Run it by typing `sh ec2-config.sh` in the command line of the instance 

# If you require different configurations per project/instance, you can simply make a .sh file for each configuration