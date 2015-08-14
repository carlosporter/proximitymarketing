In this page you will find updates information.



# RC1 update (26th July 2010) #

On July 26 we officially released OpenProximity RC1 this new release includes a lots of new features like:
  * user plugins: now users can code they're own plugins to improve OP without having to worry about how the code works.
  * improved GUI: the GUI is now more friendly.
  * improved debugging: if you are a developer then you can know use the features described in this [video](http://youtu.be/j_lx7kyrXRs?a)
  * twitter integration: now you can keep up to date with our twitter from the main OpenProximity interface.
  * stability fixes: the core is way more stable now and has a few more features related to proximity marketing.

**[Changelog Entry](ChangeLog#RC1.md)**

**For SeverXR and VMWare users**
If you bought and brand new ServerXR, or are using the VMWare image and want to update to RC1, we made an easy to use script just run this:
```
sudo bash
apt-get install wget
wget http://proximitymarketing.googlecode.com/files/update-ebox.sh
bash -ex update-ebox.sh
```

In order to upgrade you have to run this process (this upgrade is not backwards compatible, it will delete your old database and all your settings)
```
sudo apt-get purge obexftpgit
sudo apt-get update
sudo rm -rf /opt/openproximity2
sudo apt-get upgrade
sudo apt-get install openproximity2
```

If you are planning on using OpenProximity2 in a production environment then it may be useful if you run the next code block, this will make sure BlueZ is always running, even when something goes wrong
```
sudo crontab -l > newcrontab
echo '* * * * * if pidof -s bluetoothd > /dev/null; then logger "BlueZ is running"; else /usr/sbin/bluetoothd; logger "BlueZ starting up"; fi' >> newcrontab
sudo crontab newcrontab
sudo rm newcrontab
```

## Release Notes ##
  * Time filters are still broken, the problem why we haven't fixed this yet is because Django has a bug in handling dates in the admin interface, the fix is not simple but we're working on it. Basically we need some javascript on the browser so we can tell which timezone the user is running when setting the time, and then fix the date/time before sending it to the server.
  * Rejected count = -1 is broken, making no uploads to happen at all.
  * If multiple campaigns are created then statistics will get broken.



# October Update #

On October 6 2009 we made a new release, as the previous release this one is not backward compatible because of some database changes. If you're using the ubuntu package then the system will delete the current database and create a new one. We suggest you backup your database just in case.

## Ubuntu Upgrade ##
If you're using the Ubuntu package then you will get a message in the bar telling there are updates available, if you don't get this message then you will need to do:
```
sudo apt-get update
sudo apt-get install openproximity2
```

_We recommend you run **sudo aptitude dist-upgrade** this time so you get BlueZ updated_

If after upgrading you get some errors like missing tables or fields in the database, then you need to login and do:
```
sudo bash
source /etc/openproximity2.conf
cd /opt/openproximity2
bash syncdb.sh
```

## Changelog ##
This new release gets a lot of new features specially related to GUI and stability.

Changes:
  * Translations are now possible! Spanish and English are available by default. If you want to help us translate then please follow our [translation guide:](http://openproximity.wikidot.com/translations)
  * AJAX gui. A new gui is now available this gui will update it self and show you what the system is doing in real time. It will also update the state of all the pieces automatically.
  * Stability has been improved, we have tested the system in large malls and it has became times more stable.
  * Moved from the testing server to a deployment server based on CherryPy.
  * The classes in serverXR are now aware of rpc server state and of bluez state avoiding restart loops.

# August Update #

On August 20th we made a new release, this new release is not backward compatible with the previous OpenProximity2 because of some databases changes, if you're using the ubuntu package then the system will delete the current database and create a new one. We suggest you backup your database just in case.

If you're using the Ubuntu package then you will get a message in the bar telling there are updates available, if you don't get this message then you will need to do:
```
sudo apt-get update
sudo apt-get install openproximity
```

If after upgrading you get some errors like missing tables or fields in the database, then you need to login and do:
```
sudo bash
source /etc/openproximity2.conf
cd /opt/openproximity2
bash syncdb.sh
```

Please get in touch with us if you find any more troubles.

ChangeLog