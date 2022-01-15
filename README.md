# aiVLE Parallelization Experiment

Raw logs and analyzing scripts (Jupyter notebooks) for aiVLE parallelization experiment. aiVLE Web logs are under `web`, and aiVLE Worker logs are under `workers` (sub-directories are named after the corresponding nodes).

## Machine configuration

- aiVLE Web (master server): Linode Nanode 1GB
    - CPU: 1 shared CPU core
    - RAM: 1GiB
    - OS: Ubuntu 20.04
- aiVLE Workers (slave nodes): xgpg nodes
    - CPU: 2x AMD Epyc 7352, in total 48 cores/96 threads
    - RAM: 256GiB DDR4
    - GPU: NVIDIA A100-PCI, Driver 495.29, CUDA 11.5
    - OS: Ubuntu 20.04

## Experiments

1. Per-worker concurrency experiment: on one selected worker, measure time taken to finish 100 submissions
    1. concurrency=1
    2. concurrency=2
    3. concurrency=4
    4. concurrency=8

2. Load balancing experiment: fix concurrency on all workers to be 8, measure time taken to finish 100 submissions
    1. 1 node (xgpg0)
    2. 2 nodes (xgpg0,1)
    3. 3 nodes (xgpg0,1,2)

## Index table

### Per-worker concurrency

| aiVLE Web log index          | Worker log index  | Node count  | Concurrency of worker  | Submission count  | Concurrency of submission  | Note       |
|------------------------------|-------------------|-------------|------------------------|-------------------|----------------------------|------------|
| 7                            | 4                 | 1           | 8                      | 100               | 100                        |            |
| 8                            | 5                 | 1           | 4                      | 100               | 100                        |            |
| 9                            | 6                 | 1           | 2                      | 100               | 100                        |            |
| 10                           | 7                 | 1           | 1                      | 100               | 100                        |            |

### Load balancing

| aiVLE Web log index          | Worker log index  | Node count  | Concurrency of worker  | Submission count  | Concurrency of submission  | Note       |
|------------------------------|-------------------|-------------|------------------------|-------------------|----------------------------|------------|
| 5                            | 2                 | 3           | 8                      | 100               | 100                        |            |
| 6                            | 3                 | 2           | 8                      | 100               | 100                        |            |
| 7                            | 4                 | 1           | 8                      | 100               | 100                        |            |