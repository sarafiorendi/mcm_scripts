import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False, id='oidc')


# Script clones a request to other campaign.
# Fefine list of modifications
# If member_of_campaign is different, it will clone to other campaign

# request_prepid_to_clone = "SUS-Run3Summer22GS-00013"
# request_prepid_to_clone = "SUS-Run3Summer22GS-00014"

# request_prepid_to_clone = "SUS-Run3Summer22GS-00015"
request_prepid_to_clone = "SUS-Run3Summer22GS-00016"

# request_prepid_to_clone = "SUS-Run3Summer22GS-00017"
# request_prepid_to_clone = "SUS-Run3Summer22GS-00018"
request = mcm.get('requests', request_prepid_to_clone)
print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))

my_dict = {}
my_dict['Run3Summer22EEGS']  =  21000000
my_dict['Run3Summer23GS'  ]  =  19000000
my_dict['Run3Summer23BPixGS']  =  9300000

for i,k in my_dict.items():

  ### Get a request object which we want to clone
  request = mcm.get('requests', request_prepid_to_clone)
  request['total_events'] =  k
  request['member_of_campaign'] = i
  
  clone_answer = mcm.clone_request(request)
  if clone_answer.get('results'):
    print('Clone PrepID: %s' % (clone_answer['prepid']))
    print ('https://cms-pdmv.cern.ch/mcm/requests?prepid=%s'% (clone_answer['prepid']))
  else:
    print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))
    