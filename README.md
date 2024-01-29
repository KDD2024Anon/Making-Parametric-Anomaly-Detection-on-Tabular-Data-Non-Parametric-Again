# Making Parametric Anomaly Detection on Tabular Data Non-Parametric Again

  **[Overview](#overview)**
| **[Installation](#installation)**
| **[Examples](#examples)**

## Overview

This repo contains the code to run the experiments presented in the paper "Making Parametric Anomaly Detection on Tabular Data Non-Parametric Again".

## Installation

Set up and activate the Python environment by executing

```
conda env create -f environment.yml
```
Make sure to have the **latest version of condas**.

## Datasets

To download all datasets at once, with `wget`:
```
bash get_dataset_wget.sh
```
with `curl`:
```
bash get_dataset_curl.sh
```

## Examples

To run the experiments for each dataset, without retrieval, for cpu or mono-gpu:
```
source ./scripts/cpu/no_retrieval/abalone.sh
```
where ``abalone`` can be replaced by any dataset in the paper. 

For distributed training, change the number of GPUs accordingly in ``./scripts/distributed/no_retrieval/abalone.sh`` and run:

```
--nnodes=$NUMBER_OF_NODE --nproc_per_node=$NUMBER_OF_GPUS_PER_NODE
``` 
```
--mp_nodes $NUMBER_OF_NODE        #number of computing nodes
--mp_gpus $TOTAL_NUMBER_OF_GPUS   #total number of gpus
``` 

Similarly, for retrieval-augmented methods, replace ``no_retrieval`` in the previous path by the chosen retrieval method in ``['knn', 'v-attention', 'attention_bsim', 'attention_bsim_bval']``. For ``abalone`` and ``knn``retrieval, run the following:
```
source ./scripts/cpu/knn/abalone.sh
```
or 
```
source ./scripts/distributed/knn/abalone.sh
```
