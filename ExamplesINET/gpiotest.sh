#!/bin/bash
source gpio
gpio mode 4 out
while true; do
    gpio write 4 1
    sleep 0.5
    gpio write 4 0
    sleep 0.5
done