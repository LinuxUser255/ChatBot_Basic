#!/usr/bin/env bash

echo " "
echo " "
echo -e "\033[91mHello World!\033[0m"
echo " "
echo " "

echo -e "\033[91mPulling llama3l!\033[0m"

echo " "
echo " "
ollama pull llama3.1
echo " "
echo " "

echo " "
echo " "
echo -e "\033[91mRunning llama3l!\033[0m"
echo " "
echo " "

ollama run llama3.1
echo " "
