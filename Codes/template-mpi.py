#!/usr/bin/env python
#
#
import os
import sys
import numpy as np
from mpi4py import MPI
import AnalysisFunctions as af

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
status = MPI.Status()
#
# INITIALIZATION
DO WHATEVER
#
# END INITIALIZATION

# RANK 0 (MASTER CORE) SETS UP SOME STUFF FOR ITSELF
if rank == 0:
   print 'Setting my own stuff up'
   t_start=MPI.Wtime()
   DO WHATEVER

comm.Barrier()

for it in range(rank,NUMBER_OF_TOTAL_TIMES,comm.size):
   DO WHATEVER
   COMMUNICATE IF YOU LIKE
comm.Barrier()

if rank == 0:
   COMMUNICATE THE DATA IF YOU LIKE
   t_fin = MPI.Wtime()-t_start
   print 'Total time taken %0.3f'%t_fin

