
#!/bin/bash

# set directory as first argument of shell script e.g. ./duration.sh /DATA/wav/
# the script prints the ms output to the terminal
# inspired by https://stackoverflow.com/a/33221213

DIRECTORY=$1 
echo "working in" $DIRECTORY
shopt -s nullglob
let total_duration_ms=0
for audio_fragment in "$DIRECTORY"*.wav; do
  audio_fragm_ms=$(mediainfo --Inform="Audio;%Duration%" "$audio_fragment")
  echo $audio_fragment: $audio_fragm_ms "ms"
  total_duration_ms=$(expr $total_duration_ms + $audio_fragm_ms)
done
shopt -u nullglob

let total_duration_secs=$(expr $total_duration_ms / 1000)

echo "total duration is" $total_duration_secs "seconds (badly rounded approximation)" # this does not round up the seconds