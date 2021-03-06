from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'WminusJToMuNu_TuneCUETP8M1_13TeV-powheg-NNLOPS-pythia8-photos_ex1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/WJ_NNLOPS_WmToMuNu_withPhotos_cfg.py'

config.Data.outputPrimaryDataset = 'WminusJToMuNu_TuneCUETP8M1_13TeV-powheg-NNLOPS-pythia8-photos'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 5000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/kelong'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
