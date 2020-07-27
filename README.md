# Battery-Safe
Python daemon to notify you when you should plug and unplug your computer. The need for this project was born out from my carelessness of letting my previous Macbook charge for hours, until my battery stopped holding charge, and I had to move to a new machine. 

## Instructions
### Set up virtual environment
    source venv/bin/activate
    pip install requirements.txt

### Start the daemon
    nohup python3 -u -m BatterySafe &

### Viewing the logs
    tail -f nohup.out

### Kill the daemon
    ps ax | grep BatterySafe
    kill -9 <process_id>
