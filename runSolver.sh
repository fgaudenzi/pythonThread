#!/bin/bash

for filename in /home/ubuntu/dataset0/*
do
  destination=${filename}.result
  glpsol -m deploy.mod -d $filename > $destination
done
