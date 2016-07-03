#!/bin/sh
cd day2/datasets
curl -o mnist.pkl.gz https://s3.amazonaws.com/img-datasets/mnist.pkl.gz
gzip mnist.pkl.gz
