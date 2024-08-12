import sys, os, pdb
import itertools, time

#MA ,Ma ,tanB ,sinp ,process
all_points = [
[1000,150,1.0 ,0.35,'bb'],
[1000,250,1.0 ,0.35,'bb'],
[1000,300,1.0 ,0.35,'bb'],
[1000,350,1.0 ,0.35,'bb'],
[1000,500,1.0 ,0.35,'bb'],
[1050,200,1.0 ,0.35,'bb'],
[1200,150,1.0 ,0.35,'bb'],
[1200,200,1.0 ,0.35,'bb'],
[1200,250,1.0 ,0.35,'bb'],
[1200,300,1.0 ,0.35,'bb'],
[1200,350,1.0 ,0.35,'bb'],
[1200,500,1.0 ,0.35,'bb'],
[1300,200,1.0 ,0.35,'bb'],
[1400,150,1.0 ,0.35,'bb'],
[1400,250,1.0 ,0.35,'bb'],
[1400,350,1.0 ,0.35,'bb'],
[1500,400,1.0 ,0.35,'bb'],
[1600,150,1.0 ,0.35,'bb'],
[1600,350,1.0 ,0.35,'bb'],
[200,150,1.0 ,0.35,'bb'],
[400,150,1.0 ,0.35,'bb'],
[400,200,1.0 ,0.35,'bb'],
[400,250,1.0 ,0.35,'bb'],
[500,300,1.0 ,0.35,'bb'],
[600,150,1.0 ,0.35,'bb'],
[600,200,1.0 ,0.35,'bb'],
[600,250,1.0 ,0.35,'bb'],
[600,300,1.0 ,0.35,'bb'],
[600,350,1.0 ,0.35,'bb'],
[600,400,1.0 ,0.35,'bb'],
[600,500,1.0 ,0.35,'bb'],
[700,250,1.0 ,0.35,'bb'],
[750,150,1.0 ,0.35,'bb'],
[750,200,1.0 ,0.35,'bb'],
[750,250,1.0 ,0.35,'bb'],
[800,250,1.0 ,0.35,'bb'],
[800,300,1.0 ,0.35,'bb'],
[800,350,1.0 ,0.35,'bb'],
[800,400,1.0 ,0.35,'bb'],
[800,500,1.0 ,0.35,'bb'],
[850,150,1.0 ,0.35,'bb'],
[850,200,1.0 ,0.35,'bb'],
[850,250,1.0 ,0.35,'bb'],
[900,300,1.0 ,0.35,'bb'],
[900,400,1.0 ,0.35,'bb'],
[950,200,1.0 ,0.35,'bb'],
[1000 ,150,1.0 ,0.35 ,'gg'],
[1000 ,250,1.0 ,0.35 ,'gg'],
[1000 ,300,1.0 ,0.35 ,'gg'],
[1000 ,350,1.0 ,0.35 ,'gg'],
[1000 ,500,1.0 ,0.35 ,'gg'],
[1050 ,200,1.0 ,0.35 ,'gg'],
[1200 ,150,1.0 ,0.35 ,'gg'],
[1200 ,200,1.0 ,0.35 ,'gg'],
[1200 ,250,1.0 ,0.35 ,'gg'],
[1200 ,300,1.0 ,0.35 ,'gg'],
[1200 ,350,1.0 ,0.35 ,'gg'],
[1200 ,500,1.0 ,0.35 ,'gg'],
[1300 ,200,1.0 ,0.35 ,'gg'],
[1400 ,150,1.0 ,0.35 ,'gg'],
[1400 ,250,1.0 ,0.35 ,'gg'],
[1400 ,350,1.0 ,0.35 ,'gg'],
[1500 ,400,1.0 ,0.35 ,'gg'],
[1600 ,150,1.0 ,0.35 ,'gg'],
[1600 ,350,1.0 ,0.35 ,'gg'],
[200 ,150,1.0 ,0.35 ,'gg'],
[400 ,150,1.0 ,0.35 ,'gg'],
[400 ,200,1.0 ,0.35 ,'gg'],
[400 ,250,1.0 ,0.35 ,'gg'],
[500 ,300,1.0 ,0.35 ,'gg'],
[600 ,150,1.0 ,0.35 ,'gg'],
[600 ,200,1.0 ,0.35 ,'gg'],
[600 ,250,1.0 ,0.35 ,'gg'],
[600 ,300,1.0 ,0.35 ,'gg'],
[600 ,350,1.0 ,0.35 ,'gg'],
[600 ,400,1.0 ,0.35 ,'gg'],
[600 ,500,1.0 ,0.35 ,'gg'],
[700 ,250,1.0 ,0.35 ,'gg'],
[750 ,150,1.0 ,0.35 ,'gg'],
[750 ,200,1.0 ,0.35 ,'gg'],
[750 ,250,1.0 ,0.35 ,'gg'],
[800 ,250,1.0 ,0.35 ,'gg'],
[800 ,300,1.0 ,0.35 ,'gg'],
[800 ,350,1.0 ,0.35 ,'gg'],
[800 ,400,1.0 ,0.35 ,'gg'],
[800 ,500,1.0 ,0.35 ,'gg'],
[850 ,150,1.0 ,0.35 ,'gg'],
[850 ,200,1.0 ,0.35 ,'gg'],
[850 ,250,1.0 ,0.35 ,'gg'],
[900 ,300,1.0 ,0.35 ,'gg'],
[900 ,400,1.0 ,0.35 ,'gg'],
[950 ,200,1.0 ,0.35 ,'gg'],
[600 ,100 ,0.5 ,0.35 ,'bb'],
[600 ,150 ,0.5 ,0.35 ,'bb'],
[600 ,200 ,0.5 ,0.35 ,'bb'],
[600 ,250 ,0.5 ,0.35 ,'bb'],
[600 ,300 ,0.5 ,0.35 ,'bb'],
[600 ,100 ,0.8 ,0.35 ,'bb'],
[600 ,150 ,0.8 ,0.35 ,'bb'],
[600 ,200 ,0.8 ,0.35 ,'bb'],
[600 ,250 ,0.8 ,0.35 ,'bb'],
[600 ,300 ,0.8 ,0.35 ,'bb'],
[600 ,100 ,10.0 ,0.35 ,'bb'],
[600 ,150 ,10.0 ,0.35 ,'bb'],
[600 ,200 ,10.0 ,0.35 ,'bb'],
[600 ,250 ,10.0 ,0.35 ,'bb'],
[600 ,300 ,10.0 ,0.35 ,'bb'],
[600 ,100 ,1.5 ,0.35 ,'bb'],
[600 ,150 ,1.5 ,0.35 ,'bb'],
[600 ,200 ,1.5 ,0.35 ,'bb'],
[600 ,250 ,1.5 ,0.35 ,'bb'],
[600 ,100 ,2.0 ,0.35 ,'bb'],
[600 ,150 ,2.0 ,0.35 ,'bb'],
[600 ,200 ,2.0 ,0.35 ,'bb'],
[600 ,250 ,2.0 ,0.35 ,'bb'],
[600 ,300 ,2.0 ,0.35 ,'bb'],
[600 ,100 ,2.5 ,0.35 ,'bb'],
[600 ,150 ,2.5 ,0.35 ,'bb'],
[600 ,200 ,2.5 ,0.35 ,'bb'],
[600 ,100 ,4.0 ,0.35 ,'bb'],
[600 ,150 ,4.0 ,0.35 ,'bb'],
[600 ,250 ,4.0 ,0.35 ,'bb'],
[600 ,300 ,4.0 ,0.35 ,'bb'],
[600 ,100 ,6.0 ,0.35 ,'bb'],
[600 ,150 ,6.0 ,0.35 ,'bb'],
[600 ,200 ,6.0 ,0.35 ,'bb'],
[600 ,250 ,6.0 ,0.35 ,'bb'],
[600 ,100 ,0.5 ,0.35 ,'gg'],
[600 ,150 ,0.5 ,0.35 ,'gg'],
[600 ,200 ,0.5 ,0.35 ,'gg'],
[600 ,250 ,0.5 ,0.35 ,'gg'],
[600 ,300 ,0.5 ,0.35 ,'gg'],
[600 ,100 ,0.8 ,0.35 ,'gg'],
[600 ,150 ,0.8 ,0.35 ,'gg'],
[600 ,200 ,0.8 ,0.35 ,'gg'],
[600 ,250 ,0.8 ,0.35 ,'gg'],
[600 ,300 ,0.8 ,0.35 ,'gg'],
[600 ,100 ,10.0 ,0.35 ,'gg'],
[600 ,150 ,10.0 ,0.35 ,'gg'],
[600 ,200 ,10.0 ,0.35 ,'gg'],
[600 ,250 ,10.0 ,0.35 ,'gg'],
[600 ,300 ,10.0 ,0.35 ,'gg'],
[600 ,100 ,1.5 ,0.35 ,'gg'],
[600 ,150 ,1.5 ,0.35 ,'gg'],
[600 ,200 ,1.5 ,0.35 ,'gg'],
[600 ,250 ,1.5 ,0.35 ,'gg'],
[600 ,100 ,2.0 ,0.35 ,'gg'],
[600 ,150 ,2.0 ,0.35 ,'gg'],
[600 ,200 ,2.0 ,0.35 ,'gg'],
[600 ,250 ,2.0 ,0.35 ,'gg'],
[600 ,300 ,2.0 ,0.35 ,'gg'],
[600 ,100 ,2.5 ,0.35 ,'gg'],
[600 ,150 ,2.5 ,0.35 ,'gg'],
[600 ,200 ,2.5 ,0.35 ,'gg'],
[600 ,100 ,4.0 ,0.35 ,'gg'],
[600 ,150 ,4.0 ,0.35 ,'gg'],
[600 ,250 ,4.0 ,0.35 ,'gg'],
[600 ,300 ,4.0 ,0.35 ,'gg'],
[600 ,100 ,6.0 ,0.35 ,'gg'],
[600 ,150 ,6.0 ,0.35 ,'gg'],
[600 ,200 ,6.0 ,0.35 ,'gg'],
[600 ,250 ,6.0 ,0.35 ,'gg'],
## [600 ,200 ,1.0,0.1 ,'bb'],
[600 ,200 ,1.0,0.2 ,'bb'],
[600 ,200 ,1.0,0.3 ,'bb'],
[600 ,200 ,1.0,0.4 ,'bb'],
[600 ,200 ,1.0,0.45 ,'bb'],
[600 ,200 ,1.0,0.55 ,'bb'],
[600 ,200 ,1.0,0.65 ,'bb'],
[600 ,200 ,1.0,0.75 ,'bb'],
[600 ,200 ,1.0,0.10,'gg'],
[600 ,200 ,1.0,0.20,'gg'],
[600 ,200 ,1.0,0.30,'gg'],
[600 ,200 ,1.0,0.40,'gg'],
[600 ,200 ,1.0,0.45,'gg'],
[600 ,200 ,1.0,0.55,'gg'],
[600 ,200 ,1.0,0.65,'gg'],
[600 ,200 ,1.0,0.75,'gg'],
[1000 ,350 ,1.0,0.1 ,'gg'],
[1000 ,350 ,1.0,0.2 ,'gg'],
[1000 ,350 ,1.0,0.3 ,'gg'],
[1000 ,350 ,1.0,0.4 ,'gg'],
[1000 ,350 ,1.0,0.45 ,'gg'],
[1000 ,350 ,1.0,0.55 ,'gg'],
[1000 ,350 ,1.0,0.65 ,'gg'],
[1000 ,350 ,1.0,0.75 ,'gg']
]

gp_folder = '/eos/user/s/slomte/monoHiggs2HDMa_gridpacks/'
# 
# for i,ipoint in enumerate(all_points):
#   print ('point ', i, ':', ipoint)
#   gp_name = '2HDMa_{PROCESS}_sinp_{SINP}_tanb_{TANB}_mXd_10_MH3_{MA}_MH4_{Ma}_MH2_{MA}_MHC_{MA}_slc7_amd64_gcc10_CMSSW_10_6_32_tarball.tar.xz'.format(
#     MA = ipoint[0],
#     Ma = ipoint[1],
#     TANB = str(ipoint[2]).replace('.','p'),
#     SINP = str(ipoint[3]).replace('.','p'),
#     PROCESS = ipoint[4]
#     )
#   if not os.path.isfile(gp_folder+gp_name):
#     print ('file not found: ', gp_folder+gp_name)
#     print ('point ', i, ':', ipoint)
#     pdb.set_trace()
# 
# ## here is to copy the gridpacks
#   else:
#     src = gp_folder+gp_name
#     dst = '/eos/cms/store/group/phys_generator/cvmfs/gridpacks/slc7_amd64_gcc10/13TeV/madgraph/v5_2.6.5/monoHiggsBB_2HDMa/'
#     cmd = f'cp "{src}" "{dst}"'
#     os.system(cmd)
#     time.sleep(0.5)
#  
# exit(0)
# 
import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import pdb

mcm = McM(dev=False, id='oidc')

# # Script clones a request to other campaign.

# request_prepid_to_clone = "SUS-RunIISummer20UL17wmLHEGEN-01110"
request_prepid_to_clone = "SUS-RunIISummer20UL18wmLHEGEN-01181"

request = mcm.get('requests', request_prepid_to_clone)
print('Original request "%s":\n%s' % (request_prepid_to_clone, dumps(request, indent=4)))

for i,ipoint in enumerate(all_points):
  print ('point ', i, ':', ipoint)
  gp_name = '2HDMa_{PROCESS}_sinp_{SINP}_tanb_{TANB}_mXd_10_MH3_{MA}_MH4_{Ma}_MH2_{MA}_MHC_{MA}_slc7_amd64_gcc10_CMSSW_10_6_32_tarball.tar.xz'.format(
    MA = ipoint[0],
    Ma = ipoint[1],
    TANB = str(ipoint[2]).replace('.','p'),
    SINP = str(ipoint[3]).replace('.','p'),
    PROCESS = ipoint[4]
    )

  request = mcm.get('requests', request_prepid_to_clone)

    
  dataset_name = 'MonoHTobb_2HDMa_{PROCESS}_sinp-{SINP}_tanb-{TANB}_mXd-10_MH3-{MA}_MH4-{Ma}_TuneCP5_13TeV_madgraph-pythia8'.format(
      MA = ipoint[0],
      Ma = ipoint[1],
      TANB = str(ipoint[2]).replace('.','p'),
      SINP = str(ipoint[3]).replace('.','p'),
      PROCESS = ipoint[4]
  )

  if ipoint[4] == 'bb':
    request['total_events'] = 100000
  else:
    request['total_events'] = 50000
  
  print ('dataset_name: ', dataset_name)
  request['dataset_name'] =  dataset_name


  to_replace = "args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc10/13TeV/madgraph/v5_2.6.5/monoHiggsBB_2HDMa/2HDMa_bb_sinp_0p1_tanb_1p0_mXd_10_MH3_600_MH4_200_MH2_600_MHC_600_slc7_amd64_gcc10_CMSSW_10_6_32_tarball.tar.xz'),"
  gridpack_str = gp_folder+gp_name
  new_grid = "args = cms.vstring('" + gridpack_str + "'),"
  request['fragment'] = request['fragment'].replace(to_replace, new_grid)
    

  clone_answer = mcm.clone_request(request)
  if clone_answer.get('results'):
    print('Clone PrepID: %s' % (clone_answer['prepid']))
    print ('https://cms-pdmv.cern.ch/mcm/requests?prepid=%s'% (clone_answer['prepid']))
  else:
    print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))

# #     request['member_of_campaign'] = 'RunIISummer20UL17wmLHEGEN'
