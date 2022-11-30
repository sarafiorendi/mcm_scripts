
import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False)

# Script clones a request to other campaign.
# Fefine list of modifications
# If member_of_campaign is different, it will clone to other campaign
# modifications = {'dataset_name': "TPhiTo2Chi_MPhi1000_MChi1000_TuneCP5_13TeV-amcatnlo-pythia8",
#                  'cross_section': [0,0189],
#                  }
# 

mylist = [
'SUS-RunIISummer20UL16wmLHEGENAPV-00118',
'SUS-RunIISummer20UL16wmLHEGENAPV-00119',
'SUS-RunIISummer20UL16wmLHEGENAPV-00120',
'SUS-RunIISummer20UL16wmLHEGENAPV-00121',
'SUS-RunIISummer20UL16wmLHEGENAPV-00122',
'SUS-RunIISummer20UL16wmLHEGENAPV-00123',
'SUS-RunIISummer20UL16wmLHEGENAPV-00124',
'SUS-RunIISummer20UL16wmLHEGENAPV-00125',
'SUS-RunIISummer20UL16wmLHEGENAPV-00126',
'SUS-RunIISummer20UL16wmLHEGENAPV-00127',
'SUS-RunIISummer20UL16wmLHEGENAPV-00128',
'SUS-RunIISummer20UL16wmLHEGENAPV-00129',
'SUS-RunIISummer20UL16wmLHEGENAPV-00130',
'SUS-RunIISummer20UL16wmLHEGENAPV-00131',
'SUS-RunIISummer20UL16wmLHEGENAPV-00132',
'SUS-RunIISummer20UL16wmLHEGENAPV-00133',
'SUS-RunIISummer20UL16wmLHEGENAPV-00134',
'SUS-RunIISummer20UL16wmLHEGENAPV-00135',
'SUS-RunIISummer20UL16wmLHEGENAPV-00136',
'SUS-RunIISummer20UL16wmLHEGENAPV-00137',
'SUS-RunIISummer20UL16wmLHEGENAPV-00138',
'SUS-RunIISummer20UL16wmLHEGENAPV-00139',
'SUS-RunIISummer20UL16wmLHEGENAPV-00140',
'SUS-RunIISummer20UL16wmLHEGENAPV-00141',
'SUS-RunIISummer20UL16wmLHEGENAPV-00142',
'SUS-RunIISummer20UL16wmLHEGENAPV-00143',
'SUS-RunIISummer20UL16wmLHEGENAPV-00144',
'SUS-RunIISummer20UL16wmLHEGENAPV-00145',
'SUS-RunIISummer20UL16wmLHEGENAPV-00146',
'SUS-RunIISummer20UL16wmLHEGENAPV-00147',

]

for ireq in mylist:
    request_prepid_to_update = ireq
    request = mcm.get('requests', request_prepid_to_update)
  
  
    if 'prepid' not in request:
        # In case the request doesn't exist, there is nothing to update
        print('Request "%s" doesn\'t exist' % (request_prepid_to_update))
    else:
        print('Request\'s "%s" field "%s" BEFORE update: %s' % (request_prepid_to_update,
                                                              'total_events',
                                                              request['total_events']))
  

    request['total_events'] = 150000

    # Push it back to McM
    update_response = mcm.update('requests', request)
    print('Update response: %s' % (update_response))

    # Fetch the request again, after the update, to check whether value actually changed
    request2 = mcm.get('requests', request_prepid_to_update)
    print('Request\'s "%s" field "%s" AFTER update: %s' % (request_prepid_to_update,
                                                           'total_events',
                                                           request2['total_events']))


#     pdb.set_trace()  

