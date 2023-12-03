def handle_event(event):
    #print(Web3.toJSON(event))
    try:
        getTrans = Web3.toJSON(event).strip('"')
        #print(web3.eth.get_transaction(getTrans))
        trans = web3.eth.get_transaction(getTrans)
        #print(trans['input'])
        data = trans['input']
        to = trans['to']
        if to == pcsRouter:
            decoded = pcsContract.decode_function_input(data)
            print(decoded[1]['path'])
        else:
            print('nothing')
        
    except Exception as e:
        print(f'error occurred: {e}')



async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def main():
   # block_filter = w3.eth.filter('latest')
    tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                #log_loop(block_filter, 2),
                log_loop(tx_filter, 1)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()