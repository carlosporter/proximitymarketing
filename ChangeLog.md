Resume of Changes between versions



# RC1 #
  * **Web GUI**: OpenProximity can be configured through it's web interface, making user interaction easier as it can run in headless systems. OpenProximity2 RC1 made a breakthrough in it's own interface making it even easier and more useful than previous releases. Only a computer with a compatible browser like Firefox, Chrome, Safari, or Internet Explorer is needed to interface with it. (Firefox and Chrome are supported officially, the rest may have some problems).

  * **Headless operation**: OpenProximity runs as a service in a linux box, it can run without any user interaction, by default when the computer is turned on OpenProximity2 starts up and can start delivering your content over Bluetooth.

  * **Stability**: Most of the known stability issues had been solved, so now you don't have to worry any more about rebooting your computer when you add dongles, or some services stop working. OpenProximity will still be there.

  * **Twitter integration**: Now you can be up to date with OpenProximity development thanks to it's twitter client integrated into the main interface.

  * **Extensible**: OpenProximity is not only OpenSource which means you can modify the code and make it fit your needs you can also extend it through plugins. OpenProximity exposes an easy to use API that allow any user to extend OpenProximity without compromising the core functionalities. Full customization can be achieved, including: web interface changes, improved statistics gathering, new ways of working, Bluetooth sensors reading (www.opensensors.org), etc, your imagination is the limit.

  * **Translations**: OpenProximity is multilanguage, from factory it includes: English, Spanish and Italian, users can help the project translating the application through it's easy to use web interface.

  * **Online Documentation**: One click lets you get right into OpenProximity users contributed documentation (the link is active, but there's no documentation there yet).

  * **Automatic dongle detection**: You don't longer need to setup your dongles, dongles will be setup on the first detection automatically. AIRcable dongles are configured as Scanners and Uploaders while third parties are configured as Scanners. This means when you get a system based on OpenProximity you setup your campaign and you're done, no need for any complex setup.

  * **Last seen window**: With just one click you can check see all the devices that were found during the last 15 minutes, and you can checkwhat happened to it.

  * **Realtime verbose message**: OpenProximity tries and verbose to the user as possible, the main web interface shows you what's it's doing in realtime through it's AJAX interface.

  * **Database treeview**: By using some third parties code and our own we have created a nice tree like gadget that lets you go through the database and check what happened with your campaign.




# August 20 Release #

This new release includes a few new nice features:
  * Better integration of web admin interface, now creating new campaigns doesn't request you to go through 3 web pages.
  * Plugins systems, this version includes the first release of the plugins API, this API is still evolving and might change, but you can start creating your plugins in the mean time.
  * Basic pairing manager can be enabled, default pin is **1234** if you want to change the pin you need to modify openproximity/pair.py. Future releases will get pairing integrated into the admin interface, possibly as a plugin.
  * Upload process has been unified.
  * Remote scanner is available, this scanner allows to use AIRcableOS devices as scanners, which connects to the local dongle trough SPP.
  * Migrated to django 1.1
  * DB schema re-engineered.
  * Reset statics now works with raw SQL making it times faster.
  * Instead of fork with & use exec on some of the bash scripts.
  * Some RPC changes, specially to make all calls async.