from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZJToEE_svn3741_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/ZJ_MiNNLO_svn3741_Photos_cfg.py'

config.Data.outputPrimaryDataset = 'ZJToEE_svn3741_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 6000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/kelong/' 
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
