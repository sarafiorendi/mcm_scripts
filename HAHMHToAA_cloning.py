import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False, id='oidc')


# Script clones a request to other campaign.
# Fefine list of modifications
# If member_of_campaign is different, it will clone to other campaign

request_prepid_to_clone = "SUS-Run3Summer22wmLHEGS-00001"
request = mcm.get('requests', request_prepid_to_clone)
print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))
pdb.set_trace()
# 
my_dict = {}
my_dict[15, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[20, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[25, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[30, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[35, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[40, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[45, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[50, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[55, 'Run3Summer22EEwmLHEGS']  =  500000
my_dict[60, 'Run3Summer22EEwmLHEGS']  =  500000


for i,k in my_dict.items():
  mA = i[0]

  ### Get a request object which we want to clone
  request = mcm.get('requests', request_prepid_to_clone)
  request['dataset_name'] = 'HAHMHTo2A_ATo2G_MA-%s_TuneCP5_13p6TeV_madgraph-pythia8'%(mA)
  request['member_of_campaign'] = i[1]
  request['total_events'] = k

# #   print ('len of gen parameters is ', len(request['generator_parameters']))
#   pdb.set_trace()
# #   request['generator_parameters'][0]['cross_section'] = xsec
# #   request['generator_parameters'][1]['cross_section'] = xsec
#   
  request['fragment'] = request['fragment'].replace('ma_15', 'ma_%s'%i[0])
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
