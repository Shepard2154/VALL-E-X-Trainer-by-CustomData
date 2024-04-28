#!/bin/bash

index=1
for audio in *.wav	
do
    echo mv "$audio" "utt$index.wav"
    index=$((index+1))
done 
