#!/bin/bash
y | conda create -n vig python==3.9
CONDA_BASE=$(conda info --base)
source ${CONDA_BASE}/etc/profile.d/conda.sh
conda activate vig




exec bash
