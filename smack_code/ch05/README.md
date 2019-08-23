
```bash
$ vagrant up MACHINE01  
$ vagrant ssh MACHINE01 -- -l hduser
```

The password of *hduser* is `hduser`.
You're good to go!

## For learning Cassandra, below are the hardware requirements:

http://cassandra.apache.org/doc/latest/operating/hardware.html

1. Minimum Processor (i7 2300) or above Per a Node required: 2 core (Cassandra using CPU heavily during compaction process, compression, if enabled, reading data (more if compressed) etc. Try to get more cores if you can)
1. Minimum RAM Per a Node required: 4GB (Suggested: Minimum of 16 GB to a maximum of 96 GB of RAM per machine)
1. Minimum Free Disk Space Per a Node: 60GB 
1. Operating System of 64bit (Suggested)



## Clone a new VM from Master box file

```bash
[hadoop-single-node-vagrant]$ vagrant halt MACHINE01
[hadoop-single-node-vagrant]$ vagrant package MACHINE01  --output master.box
[hadoop-single-node-vagrant]$ vagrant box add robert-cassandra-box master.box
```

Now you can create virtual machines from this box by simply giving the name of the box in the Vagrantfile, like

```yaml
config.vm.box = "robert-cassandra-box"
```
