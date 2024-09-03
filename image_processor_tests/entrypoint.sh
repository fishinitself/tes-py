 #!/bin/bash

echo "Starting"
source /wrk/iptests-py-env/bin/activate
python /wrk/image_processor_tests.py "$@"