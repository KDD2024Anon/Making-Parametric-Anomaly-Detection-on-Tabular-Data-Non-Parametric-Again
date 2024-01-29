import os, scipy.io 
import numpy as np

from datasets.base import BaseDataset

class WineDataset(BaseDataset):

    '''
    https://archive.ics.uci.edu/ml/datasets/wine
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.is_data_loaded = False
        self.tmp_file_names = ['wine.mat']

        self.name = 'wine'

    def load(self,):
        
        data = scipy.io.loadmat(os.path.join(self.data_path, self.tmp_file_names[0]))
        self.data_table  = data['X']
        self.target = ((data['y']).astype(np.int32)).reshape(-1)

        self.norm_samples = self.data_table [self.target == 0]
        self.anom_samples = self.data_table [self.target == 1]

        self.norm_samples = np.c_[self.norm_samples, 
                            np.zeros(self.norm_samples.shape[0])]
        self.anom_samples = np.c_[self.anom_samples, 
                                  np.ones(self.anom_samples.shape[0])]

        self.ratio = (100.0 * (0.5*len(self.norm_samples)) / ((0.5*len(self.norm_samples)) +
                                                             len(self.anom_samples)))
        #self.data_table = np.concatenate((self.norm_samples, self.anom_samples),
                                         #axis=0)
        self.N, self.D = self.data_table.shape
        self.D -= 1
        self.cat_features = []
        self.num_features = list(range(0, self.D))

        self.cardinalities = []
        self.num_or_cat = {idx: (idx in self.num_features) for idx in range(self.D)}

        self.is_data_loaded = True

    def __repr__(self):
        repr = f'WineDataset(BaseDataset): {self.N} samples, {self.D} features\n'\
               f'{len(self.cat_features_idx)} categorical features\n'\
               f'{len(self.num_features_idx )} numerical features'
        return repr