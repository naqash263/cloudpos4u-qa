#!/bin/bash

PROVIDER=${1:-lmstudio}
CACHE_MODE=${2:-cache}

cd "$(dirname "$0")"

CACHE_FLAG=""

if [ "$CACHE_MODE" = "no-cache" ]; then
  CACHE_FLAG="--no-cache"
fi

if [ "$PROVIDER" = "openai" ]; then
  echo "Running Promptfoo with OpenAI..."
  promptfoo eval -c configs/promptfoo-openai.yaml $CACHE_FLAG

elif [ "$PROVIDER" = "lmstudio" ]; then
  echo "Running Promptfoo with LM Studio..."
  promptfoo eval -c configs/promptfoo-lmstudio.yaml $CACHE_FLAG

elif [ "$PROVIDER" = "ollama" ]; then
  echo "Running Promptfoo with Ollama..."
  promptfoo eval -c configs/promptfoo-ollama.yaml $CACHE_FLAG

else
  echo "Unknown provider: $PROVIDER"
  echo "Use: ./run_promptfoo.sh openai | lmstudio | ollama"
  echo "Optional second argument: no-cache"
  exit 1
fi