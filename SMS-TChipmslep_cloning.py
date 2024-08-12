import sys, os, pdb
import itertools, time

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False, id='oidc')

# # Script clones a request to other campaign.
list_to_clone = [
# 'SUS-RunIISpring21UL16FSGSPremixLLPBugFix-00012',  	
# 'SUS-RunIISpring21UL16FSGSPremixLLPBugFix-00013',  	
# 'SUS-RunIISpring21UL17FSGSPremixLLPBugFix-00009',  	
# 'SUS-RunIISpring21UL17FSGSPremixLLPBugFix-00018',  	
# 'SUS-RunIISpring21UL18FSGSPremixLLPBugFix-00010',  	
# 'SUS-RunIISpring21UL18FSGSPremixLLPBugFix-00011',  
'SUS-RunIISpring21UL16FSGSPremixLLPBugFix-00016',  
'SUS-RunIISpring21UL17FSGSPremixLLPBugFix-00013',
'SUS-RunIISpring21UL18FSGSPremixLLPBugFix-00013',
]

for ireq in list_to_clone:
  request_prepid_to_clone = ireq

  request = mcm.get('requests', request_prepid_to_clone)
#   print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))

  request['process_string'] = 'slhaFix'

  clone_answer = mcm.clone_request(request)
  if clone_answer.get('results'):
    print('Clone PrepID: %s' % (clone_answer['prepid']))
    print ('https://cms-pdmv.cern.ch/mcm/requests?prepid=%s'% (clone_answer['prepid']))
  else:
    print('Something went wrong while cloning a request. ')

# #     request['member_of_campaign'] = 'RunIISummer20UL17wmLHEGEN'
