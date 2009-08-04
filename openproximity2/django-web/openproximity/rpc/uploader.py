#    OpenProximity2.0 is a proximity marketing OpenSource system.
#    Copyright (C) 2009,2008 Naranjo Manuel Francisco <manuel@aircable.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
from net.aircable.openproximity.signals import uploader as signals
from openproximity.models import *

from common import get_uploader, do_upload

import traceback

def handle(services, signal, uploader, args, kwargs):
    print "uploader signal", signals.TEXT[signal], args, kwargs
    
    if signal == signals.SDP_RESOLVED:
	handle_sdp_resolved(kwargs['dongle'], kwargs['address'], kwargs['port'])
    elif signal == signals.SDP_NORECORD:
	handle_sdp_norecord(kwargs['dongle'], kwargs['address'], 
	    kwargs['pending'])
    elif signal == signals.SDP_TIMEOUT:
	handle_sdp_timeout(kwargs['dongle'], kwargs['address'], 
	    kwargs['pending'])
    elif signal == signals.FILE_UPLOADED:
	handle_file_uploaded(kwargs['dongle'], kwargs['address'], 
	    kwargs['pending'], kwargs['port'], kwargs['files'])
    elif signal == signals.FILE_FAILED:
	handle_file_failed(kwargs['dongle'], kwargs['address'], 
	    kwargs['pending'], kwargs['port'], kwargs['files'], kwargs['ret'], 
	    kwargs['stderr'], services)
    else:
	print "signal ignored"
    

def get_dongles(dongles):
    out = list()
    
    for address in dongles:
        print address
        try:
    	    dongle = UploaderBluetoothDongle.objects.get(address=address, enabled=True)
            out.append( (address, dongle.max_conn, dongle.name) )
        except Exception, err:
            print err
    return out

def handle_sdp_resolved(dongle, remote, channel):
    print "Valid SDP:", dongle, remote, channel
    remote=RemoteDevice.objects.filter(address=remote).get()
    if RemoteBluetoothDeviceSDP.objects.filter(remote=remote).count() == 0:
	print "New SDP result"
	record = RemoteBluetoothDeviceSDP()
	record.dongle = UploaderBluetoothDongle.objects.get(address=dongle)
	record.channel = channel
	record.remote = remote
        record.save()

def handle_sdp_norecord(dongle, remote, pending):
    print "No SDP:", dongle, remote
    pending.remove(remote)
    remote=RemoteDevice.objects.filter(address=remote).get()
    if RemoteBluetoothDeviceNoSDP.objects.filter(remote=remote).count() == 0:
	record = RemoteBluetoothDeviceNoSDP()
        record.dongle = UploaderBluetoothDongle.objects.get(address=dongle)
	record.remote = remote
        record.save()
    
def handle_sdp_timeout(dongle, remote, pending):
    print "SDP timeout:", dongle, remote    
    pending.remove(remote)
    record = RemoteBluetoothDeviceSDPTimeout()
    record.dongle = UploaderBluetoothDongle.objects.get(address=dongle)
    record.setRemoteDevice(remote)
    record.save()

def handle_file_uploaded(dongle, remote, pending, channel, files):
    print "files uploaded:", dongle, remote, channel, files
    pending.remove(remote)
    record = RemoteBluetoothDeviceFilesSuccess()
    record.dongle = UploaderBluetoothDongle.objects.get(address=dongle)
    record.campaign = get_campaign_rule(files)
    record.setRemoteDevice(remote)
    record.save()

def handle_file_failed(dongle, remote, pending, channel, files, ret, err, services):
	print "handle file failed", dongle, remote, channel, files	
	print err
    	
	try:
	    record = RemoteBluetoothDeviceFilesRejected()
	    record.dongle = UploaderBluetoothDongle.objects.get(address=dongle)
	    rule = get_campaign_rule(files)
	    if rule is None:
		raise Exception("Couldn't find rule")
	    record.campaign = rule
	    record.ret_value = ret
	    record.setRemoteDevice(remote)
	    record.save()
	    
	    # from here we try again either on timeout or if rejected count is 
	    # smaller than filter
	    try_again = rule.tryAgain(record)
		
	    print "try again: %s" % try_again
	    if try_again:
		uploader = get_uploader(services)
		if uploader:
		    print "trying again"
		    do_upload(uploader, files, remote)
    		else:
    		    print "no uploader registered"
	    else:
		pending.remove(remote)
	except Exception, err:
		print "OOPS!!!!!", err
		traceback.print_exc()
		pending.remove(remote)
