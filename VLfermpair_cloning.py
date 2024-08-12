import sys, os, pdb
import itertools, time

#MA ,Ma ,tanB ,sinp ,process
all_points = [
[300,'EE'],
[350,'EE'],
[400,'EE'],
[450,'EE'],
[1050,'EE'],
[300,'EN'],
[350,'EN'],
[400,'EN'],
[450,'EN'],
[1050,'EN'],
[300,'NN'],
[350,'NN'],
[400,'NN'],
[450,'NN'],
[1050,'NN'],
]

gp_folder = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/slc7_amd64_gcc10/MadGraph5_aMCatNLO/SUS_VLferm/'

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False, id='oidc')

# # Script clones a request to other campaign.

# request_prepid_to_clone = "SUS-RunIISummer20UL17wmLHEGEN-01110"
request_prepid_to_clone = "SUS-RunIISummer20UL18wmLHEGEN-01148"

request = mcm.get('requests', request_prepid_to_clone)
print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))

for i,ipoint in enumerate(all_points):
  print ('point ', i, ':', ipoint)
  gp_name = 'VLferm_EWcouplings_4321_m{MA}GeV_{PROCESS}_to_4b_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'.format(
    MA = ipoint[0],
    PROCESS = ipoint[1]
    )

  request = mcm.get('requests', request_prepid_to_clone)

  dataset_name = 'VLferm_m{MA}GeV_{PROCESS}_to_4b_TuneCP5_13TeV_madgraph-pythia8'.format(
      MA = ipoint[0],
      PROCESS = ipoint[1]
  )

  request['total_events'] = 120000
  
  print ('dataset_name: ', dataset_name)
  request['dataset_name'] =  dataset_name


  to_replace = "args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/slc7_amd64_gcc10/MadGraph5_aMCatNLO/SUS_VLferm/VLferm_EWcouplings_4321_m500GeV_EE_to_4b_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),"
  gridpack_str = gp_folder+gp_name
  new_grid = "args = cms.vstring('" + gridpack_str + "'),"
  request['fragment'] = request['fragment'].replace(to_replace, new_grid)
    
#   request['member_of_campaign'] = 'RunIISummer20UL17wmLHEGEN'
#   request['member_of_campaign'] = 'RunIISummer20UL16wmLHEGEN'
  request['member_of_campaign'] = 'RunIISummer20UL16wmLHEGENAPV'

  clone_answer = mcm.clone_request(request)
  if clone_answer.get('results'):
    print('Clone PrepID: %s' % (clone_answer['prepid']))
    print ('https://cms-pdmv.cern.ch/mcm/requests?prepid=%s'% (clone_answer['prepid']))
  else:
    print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))

