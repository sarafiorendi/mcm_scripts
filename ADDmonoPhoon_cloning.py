import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb
import itertools

mcm = McM(dev=False, id='oidc')


# Script clones a request to other campaign.
# Fefine list of modifications
# If member_of_campaign is different, it will clone to other campaign

request_prepid_to_clone = "SUS-RunIISummer20UL17GEN-00323"
request = mcm.get('requests', request_prepid_to_clone)
print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))

# md_range = [1]#,2,3,4,5,6]
# d_range = [4,5,6,8]
md_range = [2,3,4,5,6]
d_range = [3,4,5,6,8]

for md, d in itertools.product(md_range,d_range):
    print(md, d)

    request = mcm.get('requests', request_prepid_to_clone)
    dataset_name = 'ADDmonoPhoton_MD-%d_d-%d_TuneCP5_13TeV-pythia8'%(1000*md, d)
    print ('dataset_name: ', dataset_name)
    request['dataset_name'] =  dataset_name

    request['fragment'] = request['fragment'].replace('ExtraDimensionsLED:n = 3', 'ExtraDimensionsLED:n = %d'%d)
    request['fragment'] = request['fragment'].replace('ExtraDimensionsLED:MD = 1000','ExtraDimensionsLED:MD = %d'%(md*1000))

    print('New request for md, d %s :\n%s, %s' % (md, d, dumps(request, indent=4)))
    print('\n\n')

    clone_answer = mcm.clone_request(request)
    if clone_answer.get('results'):
      print('Clone PrepID: %s' % (clone_answer['prepid']))
      print ('https://cms-pdmv.cern.ch/mcm/requests?prepid=%s'% (clone_answer['prepid']))
    else:
      print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))

  # 

#     request['member_of_campaign'] = 'RunIISummer20UL17wmLHEGEN'

# my_dict[ 100 ] = [1]#,100]
# my_dict[ 100 ] = [100]
# my_dict[ 250 ] = [1,100]
# my_dict[ 500 ] = [1,100,200,400]
# my_dict[ 750 ] = [1,100]
# my_dict[ 1000] = [1,100,200,400,600,800]
# my_dict[ 1250] = [1,100]
# my_dict[ 1500] = [1,100,200,400,600,800]
# my_dict[ 1750] = [1,100,200,400,600,800]
# my_dict[ 2000] = [1,100,200,400,600,800]
# my_dict[ 2250] = [1,100,200,400,600,800]
# my_dict[ 2500] = [1,100,200,400,600,800]
# my_dict[ 3000] = [1,100,200]
# my_dict[ 3500] = [1,100]

# for i,k in my_dict.items():
#   mZ = i
#   for imchi in k:
#     mChi = imchi
    
#     print (mZ, mChi)

    ### Get a request object which we want to clone
#     request = mcm.get('requests', request_prepid_to_clone)
#     request['dataset_name'] =  'MonoHTobb_ZpBaryonic_MZp-%s_MChi-%s_TuneCP5_13TeV_madgraph_pythia8'%(mZ, mChi)
#     request['member_of_campaign'] = 'RunIISummer20UL17wmLHEGEN'
  
#     request['fragment'] = request['fragment'].replace('MZp100', 'MZp%s'%mZ)
#     request['fragment'] = request['fragment'].replace('MChi1', 'MChi%s'%mChi)
  
#     print('New request for mZ, mChi %s :\n%s, %s' % (mZ, mChi, dumps(request, indent=4)))
#     print('\n\n')
  
#     clone_answer = mcm.clone_request(request)
#     if clone_answer.get('results'):
#       print('Clone PrepID: %s' % (clone_answer['prepid']))
#       print ('https://cms-pdmv.cern.ch/mcm/requests?prepid=%s'% (clone_answer['prepid']))
#     else:
#       print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))
#   # 
  #   pdb.set_trace()  
  