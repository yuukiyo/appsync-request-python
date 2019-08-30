from graphqlclient import graphqlclient

# GraphQL Endpoint
client = graphqlclient('https://xxx.appsync-api.ap-northeast-1.amazonaws.com/graphql')
client.inject_token('xxx', 'x-api-key')


ddb_stream_event = {
    'latitude': {'S': '35.423756'},
    'vehicleId': {'S': '1'},
    'deviceid': {'S': '1'},
    'speed': {'N': '79'},
    'longitude': {'S': '139.383258'},
    'timestamp': {'S': '2019-08-30T09:25:29'}
}

query = '''
mutation CreateVehicle($input: CreateVehicleInput!) {
  createVehicle(input: $input) {
    vehicleId
    vehicleCategory
    latitude
    longitude
    lastUpdate
  }
}
'''
vehicle = {
    'vehicleId': ddb_stream_event['vehicleId']['S'],
    'vehicleCategory': ddb_stream_event['vehicleId']['S'],
    'latitude': ddb_stream_event['latitude']['S'],
    'longitude': ddb_stream_event['longitude']['S'],
    'lastUpdate': 1567128124
}

variables = {'input': vehicle}

result = client.execute(query, variables)
print(result)
