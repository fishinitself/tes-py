 #!/bin/bash

echo "Starting"
source /wrk/tes-py-env/bin/activate
export MPLBACKEND=TKAgg
python /wrk/main.py "$@"