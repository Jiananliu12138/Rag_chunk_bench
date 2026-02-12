#!/bin/bash

MODEL_PATH="/data/h50056789/Rag_chunk_bench/model/Qwen3-4B"
PORT=8005
GPU=1

export CUDA_VISIBLE_DEVICES=$GPU

python -m vllm.entrypoints.openai.api_server \
  --model $MODEL_PATH \
  --served-model-name Qwen3-4B \
  --host 127.0.0.1 \
  --port $PORT \
  --tensor-parallel-size 1 \
  --gpu-memory-utilization 0.25\
  --max-model-len 3072 \
  --trust-remote-code
