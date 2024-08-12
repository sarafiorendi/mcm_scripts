import sys, os, pdb
import itertools, time

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False, id='oidc')

# # Script clones a request to other campaign.

# request_prepid_to_clone = "SUS-RunIISummer20UL17wmLHEGEN-01110"

# for i in rage(1111,1295):
#   request_prepid_to_fix = "SUS-RunIISummer20UL17wmLHEGEN-0%d"%i
# 
#   request = mcm.get('requests', request_prepid_to_fix)
#   if 'prepid' not in request:
#         # In case the request doesn't exist, there is nothing to update
#       print('Request "%s" doesn\'t exist' % (request_prepid_to_fix))
#       continue
#   dataset_name =  request['dataset_name'] 
#   new_name = dataset_name.replace(' ','')
#   request['dataset_name'] = new_name
# 
#   # Push it back to McM
#   update_response = mcm.update('requests', request)
#   print('Update response: %s' % (update_response))
# 
#   # Fetch the request again, after the update, to check whether value actually changed
#   request2 = mcm.get('requests', request_prepid_to_fix)
# #   print('Request\'s "%s" field "%s" AFTER update: %' % (request_prepid_to_fix,
# #                                                          'dataset_name',
# #                                                          request2['dataset_name']))



# for i in range(1112,1196):
#   request_prepid_to_fix = "SUS-RunIISummer20UL17wmLHEGEN-0%d"%i

for i in range(1181,1367):
  request_prepid_to_fix = "SUS-RunIISummer20UL18wmLHEGEN-0%d"%i

  request = mcm.get('requests', request_prepid_to_fix)
  if 'prepid' not in request:
        # In case the request doesn't exist, there is nothing to update
      print('Request "%s" doesn\'t exist' % (request_prepid_to_fix))
      continue
  request['fragment'] = request['fragment'].replace('/eos/user/s/slomte/monoHiggs2HDMa_gridpacks/', '/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc10/13TeV/madgraph/v5_2.6.5/monoHiggsBB_2HDMa/')
    
#   dataset_name =  request['dataset_name'] 
#   new_name = dataset_name.replace(' ','')
#   request['dataset_name'] = new_name

  # Push it back to McM
  update_response = mcm.update('requests', request)
  print('Update response: %s' % (update_response))

  # Fetch the request again, after the update, to check whether value actually changed
  request2 = mcm.get('requests', request_prepid_to_fix)
#   print('Request\'s "%s" field "%s" AFTER update: %' % (request_prepid_to_fix,
#                                                          'dataset_name',
#                                                          request2['dataset_name']))


