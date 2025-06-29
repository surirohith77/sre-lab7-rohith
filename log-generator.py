import time
import random
import json
from datetime import datetime
log_levels = ['INFO', 'WARN', 'ERROR', 'DEBUG']
services = ['web-server', 'database', 'cache', 'auth-service']
while True:
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'level': random.choice(log_levels),
        'service': random.choice(services),
        'message': f'Sample log message {random.randint(1, 1000)}',
        'response_time': random.randint(10, 500)
    }
    print(json.dumps(log_entry))
    time.sleep(random.uniform(0.5, 2.0))
