import requests
from datetime import datetime, time, timedelta,timezone
from collections import defaultdict
import json

'''
this method split the call spanning multiple days into day segments
return:list of tuples(date,segment_start,segment_end)
'''
def process_timezone(start_ts, end_ts):
    start_dt = datetime.fromtimestamp(start_ts / 1000, tz=timezone.utc)
    end_dt = datetime.fromtimestamp(end_ts / 1000, tz=timezone.utc)
    
    current_date = start_dt.date()
    end_date = end_dt.date()
    date_ranges = []
    
    while current_date <= end_date:  
        # Calculate the start and end timestamps of the current date
        date_start = datetime.combine(current_date, time.min).replace(tzinfo=timezone.utc)
        date_end = date_start + timedelta(days=1)
        
        date_start_ts = int(date_start.timestamp() * 1000)
        date_end_ts = int(date_end.timestamp() * 1000)
        
        # Calculation of actual time period
        segments_start = max(start_ts, date_start_ts)
        segments_end = min(end_ts, date_end_ts)
        
        if segments_start < segments_end:
            date_str = current_date.isoformat()
            date_ranges.append((date_str, segments_start, segments_end))
        
        current_date += timedelta(days=1)
    
    return date_ranges
'''
this is a expected return 'date_ranges' tulple outcomes⬆️
[
    ("2024-02-08", 1707360600000, 1707436800000),  # 22:30 - 00:00
    ("2024-02-09", 1707436800000, 1707452100000)   # 00:00 - 02:15
]

'''



'''
process call data organize by customer and date
return: Dict[customer_id][date] -> list of (start, end, call_id)
'''

def process_calls(calls):
    """Main processing logic"""
    customer_dates = defaultdict(lambda: defaultdict(list))
    
    for call in calls:
        try:
            customer_id = call['customerId']
            call_id = call['callId']
            start_ts = call['startTimestamp']
            end_ts = call['endTimestamp']
            
            # Validate timestamps
            if start_ts >= end_ts:
                print(f"Invalid timestamps for call {call_id}")
                continue
                
            date_segments = process_timezone(start_ts, end_ts)
            
            for date_str, seg_start, seg_end in date_segments:
                customer_dates[customer_id][date_str].append(
                    (seg_start, seg_end, call_id)
                )
                
        except KeyError as e:
            print(f"Missing key {e} in call: {call}")
            continue
            
    return customer_dates
'''
calls = [
    {
        "customerId": 123,
        "callId": "call_1",
        "startTimestamp": 1707360600000,  # 2024-02-08 22:30:00
        "endTimestamp": 1707452100000    # 2024-02-09 02:15:00
    },
    {
        "customerId": 456,
        "callId": "call_2",
        "startTimestamp": 1707400000000,  # 2024-02-09 10:00:00
        "endTimestamp": 1707403600000    # 2024-02-09 11:00:00
    }
]

result = process_calls(calls)

{
    123: {
        "2024-02-08": [(1707360600000, 1707436800000, "call_1")],  # 22:30 - 00:00
        "2024-02-09": [(1707436800000, 1707452100000, "call_1")]   # 00:00 - 02:15
    },
    456: {
        "2024-02-09": [(1707400000000, 1707403600000, "call_2")]  # 10:00 - 11:00
    }
}


'''

def calculate_concurrent(customer_data):
    """Calculate max concurrent calls using sweep line algorithm"""
    results = []
    
    for customer_id, dates in customer_data.items():
        for date_str, intervals in dates.items():
            events = []
            for start, end, call_id in intervals:
                events.append((start, 'start', call_id))
                events.append((end, 'end', call_id))
            
            # Critical sorting: time first, end events before start events
            events.sort(key=lambda x: (x[0], 0 if x[1] == 'end' else 1))
            
            current_calls = 0
            max_concurrent = 0
            active_calls = set()
            peak_info = None
            
            for event in events:
                ts, event_type, call_id = event
                
                if event_type == 'start':
                    current_calls += 1
                    active_calls.add(call_id)
                    
                    if current_calls > max_concurrent:
                        max_concurrent = current_calls
                        peak_info = {
                            'timestamp': ts,
                            'call_ids': list(active_calls)
                        }
                    elif current_calls == max_concurrent:
                        # Keep the latest occurrence
                        peak_info = {
                            'timestamp': ts,
                            'call_ids': list(active_calls)
                        }
                else:
                    if call_id in active_calls:
                        current_calls -= 1
                        active_calls.remove(call_id)
            
            if max_concurrent > 0 and peak_info:
                results.append({
                    'customerId': customer_id,
                    'date': date_str,
                    'maxConcurrentCalls': max_concurrent,
                    'timestamp': peak_info['timestamp'],
                    'callIds': peak_info['call_ids']
                })
    
    return results

def main():
    user_key = '7c625ccbeec4dc7a70fe89a08fdb'
    
    # 1. fetch data set
    test_data_url = f'https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey={user_key}'
    response = requests.get(test_data_url)
    if response.status_code != 200:
        print(f"Failed to fetch test data: {response.status_code}")
        return
    
    try:
        #get the string from callRecords
        response_data = response.json()
        calls = response_data.get('callRecords', [])  
        
        if not isinstance(calls, list):
            raise ValueError("API return unexpected data structure")
            
    except Exception as e:
        print(f"filed the fetch the data: {str(e)}")
        return
    
    # 2. process the data
    customer_data = process_calls(calls)
    results = calculate_concurrent(customer_data)
    
    # 3. update the result the the endpoint
    test_result_url = f'https://candidate.hubteam.com/candidateTest/v3/problem/test-result?userKey={user_key}'
    response = requests.post(test_result_url, json={'results': results})
    
    print(f"\nTest Submission Status: {response.status_code}")
    print("Test Server Response:")
    print(response.text)


#fetch the data from endpoints and compare with the local result
def test_with_endpoint_answer():
    user_key = '7c625ccbeec4dc7a70fe89a08fdb'
    
    try:
        # fetch the dataset
        test_data_url = f'https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey={user_key}'
        response = requests.get(test_data_url)
        
        if response.status_code != 200:
            print(f"❌ failed to fetch the data | Status: {response.status_code}")
            return

        response_data = response.json()
        
        # previously testin failed due to nested callRecords data structure
        if isinstance(response_data, dict) and 'callRecords' in response_data:
            test_calls = response_data['callRecords']
        else:
            print("Exception Data Structure Format:")
            print(json.dumps(response_data, indent=2))
            return

        # process the calls
        customer_data = process_calls(test_calls)
        local_results = calculate_concurrent(customer_data)

        # get the testing endpoint result
        test_answer_url = f'https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset-answer?userKey={user_key}'
        answer_response = requests.get(test_answer_url)
        
        if answer_response.status_code != 200:
            print(f"❌ failed the fetch the test_answer | Status: {answer_response.status_code}")
            return
            
        test_answer = answer_response.json()

        # compare the result
        def normalize_results(results):
            for item in results:
                item['callIds'] = sorted(item['callIds'])
            return sorted(results, key=lambda x: (x['customerId'], x['date']))

        local_normalized = normalize_results(local_results)
        answer_normalized = normalize_results(test_answer.get('results', []))

        # compare the result
        if local_normalized == answer_normalized:
            print("✅ local result is the same as expected test standard result！")
        else:
            print("❌ Found diff：")
            print("local result：", json.dumps(local_normalized, indent=2))
            print("test standard result：", json.dumps(answer_normalized, indent=2))

    except Exception as e:
        print(f"⚠️ Exception Data Structure Format: {str(e)}")

if __name__ == "__main__":
    main()
    test_with_endpoint_answer()
