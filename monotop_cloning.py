import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False)

# Script clones a request to other campaign.
# Fefine list of modifications
# If member_of_campaign is different, it will clone to other campaign

request_prepid_to_clone = "SUS-RunIISummer20UL18wmLHEGEN-00120"
request = mcm.get('requests', request_prepid_to_clone)
print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))

my_dict = {}
##      mphi, mchi       xsec 
# my_dict[195,   100  ]  =  4.9310000  ## this will be the one to be cloned
my_dict[200,   50   ]  =  57.5900000
my_dict[200,   150  ]  =  0.2533000
my_dict[295,   150  ]  =  2.3730000
my_dict[300,   100  ]  =  18.9600000
my_dict[300,   300  ]  =  0.0189000  
my_dict[495,   250  ]  =  0.7040000
my_dict[500,   150  ]  =  4.3150000
my_dict[500,   500  ]  =  0.0022620
my_dict[750,   150  ]  =  1.1240000
my_dict[995,   500  ]  =  0.0710200
my_dict[1000,  150  ]  =  0.3727000
my_dict[1000,  1000 ]  =  0.0000534
my_dict[1250,  150  ]  =  0.1444000
my_dict[1495,  750  ]  =  0.0120600
my_dict[1500,  150  ]  =  0.0621300
my_dict[1500,  1000 ]  =  0.0001071
my_dict[1700,  800  ]  =  0.0189000
my_dict[1750,  150  ]  =  0.0287900
my_dict[1750,  700  ]  =  0.0226300
my_dict[1995,  1000 ]  =  0.0026550
my_dict[2000,  150  ]  =  0.0141400
my_dict[2000,  500  ]  =  0.0129700
my_dict[2000,  1500 ]  =  4.319e-06
my_dict[2495,  1250 ]  =  0.0006786
my_dict[2500,  750  ]  =  0.0032370
my_dict[2500,  2000 ]  =  0.0000002682
my_dict[2995,  1500 ]  =  0.0001901
my_dict[3000,  1000 ]  =  0.0008935
my_dict[3000,  2000 ]  =  4.319E-7
# 
# 


for i,k in my_dict.items():
  mphi = i[0]
  mchi = i[1]
  xsec = k
  
  ### Get a request object which we want to clone
  request = mcm.get('requests', request_prepid_to_clone)
  request['dataset_name'] = 'TPhiTo2Chi_MPhi%s_MChi%s_TuneCP5_13TeV-amcatnlo-pythia8'%(mphi,mchi)
  print ('len of gen parameters is ', len(request['generator_parameters']))
  pdb.set_trace()
  request['generator_parameters'][0]['cross_section'] = xsec
  request['generator_parameters'][1]['cross_section'] = xsec
  
  request['fragment'] = request['fragment'].replace('Mphi-195', 'Mphi-%s'%i[0]).replace('Mchi-100', 'Mchi-%s'%i[1])
  
  print('New request for mPhi %s  mchi %s:\n%s' % (mphi,mchi, dumps(request, indent=4)))
  print('\n\n')

  clone_answer = mcm.clone_request(request)
  if clone_answer.get('results'):
    print('Clone PrepID: %s' % (clone_answer['prepid']))
  else:
    print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))
  
  pdb.set_trace()  

