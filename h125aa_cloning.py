import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False)

# Script clones a request to other campaign.
# Fefine list of modifications
# If member_of_campaign is different, it will clone to other campaign

request_prepid_to_clone = "SUS-RunIISummer20UL16pLHEGEN-00002"
request = mcm.get('requests', request_prepid_to_clone)
print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))
pdb.set_trace()
# 
my_dict = {}
# ##      mphi, mchi       xsec 
# # my_dict[195,   100  ]  =  4.9310000  ## this will be the one to be cloned
my_dict[25, 'RunIISummer20UL16pLHEGEN']  =  200000
my_dict[25, 'RunIISummer20UL16pLHEGENAPV']  =  200000
my_dict[25, 'RunIISummer20UL17pLHEGEN']  =  400000
my_dict[25, 'RunIISummer20UL18pLHEGEN']  =  400000

for i,k in my_dict.items():
  mA = i[0]

  ### Get a request object which we want to clone
  request = mcm.get('requests', request_prepid_to_clone)
  request['dataset_name'] = 'HToAATo2Mu2B-MA%s_TuneCP5_13TeV-madgraphMLM-pythia8'%(mA)
  request['member_of_campaign'] = i[1]
  request['total_events'] = k

# #   print ('len of gen parameters is ', len(request['generator_parameters']))
#   pdb.set_trace()
# #   request['generator_parameters'][0]['cross_section'] = xsec
# #   request['generator_parameters'][1]['cross_section'] = xsec
#   
  request['fragment'] = request['fragment'].replace('ma0 = 12', 'ma0 = %s'%i[0])
#   
  print('New request for mA %s :\n%s' % (mA, dumps(request, indent=4)))
  print('\n\n')
#   pdb.set_trace()

  clone_answer = mcm.clone_request(request)
  if clone_answer.get('results'):
    print('Clone PrepID: %s' % (clone_answer['prepid']))
    print ('https://cms-pdmv.cern.ch/mcm/requests?prepid=%s'% (clone_answer['prepid']))
  else:
    print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))

  pdb.set_trace()  
# 
