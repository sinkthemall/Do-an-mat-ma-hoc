#!/bin/bash
function display_help {
  echo "Usage: mycommand [OPTIONS] [ARGUMENTS]"
  echo ""
  echo "Options:"
  echo "  -h, --help           Display this help message"
  echo "  -a, --attack ATTACK  Choose an attack to run"
  echo ""
}

# count sum of all primes in range


attack=""


# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      display_help
      exit 0
      ;;
    -a|--attack)
      attack="$2"
      shift
      ;;
    *)
      echo "Unknown option: $1"
      display_help
      exit 1
      ;;
  esac
  shift
done

case $attack in
  "fermat")
    echo "Running fermat attack"
    echo -e "\033[1m Test fermat using RsaCtfTool \033[0m"
    time ./RsaCtfTool.py --publickey examples/close_primes.pub --attack fermat --tests

    echo -e "\033[1m Test fermat using my code \033[0m"
    time python3 ./python_test/close_pq.py
    ;;
  "pollard")
    echo "Running pollard attack"
    ;;
  "wiener")
    echo "Running wiener attack"
    ;;
  *)
    echo "No attack specified"
    display_help
    exit 1
    ;;
esac