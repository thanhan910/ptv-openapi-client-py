# V3DynamoDbTimetablesReponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timetables** | [**List[V3DynamoDbTimetable]**](V3DynamoDbTimetable.md) |  | [optional] 
**status** | [**V3Status**](V3Status.md) |  | [optional] 

## Example

```python
from ptv_openapi_client.models.v3_dynamo_db_timetables_reponse import V3DynamoDbTimetablesReponse

# TODO update the JSON string below
json = "{}"
# create an instance of V3DynamoDbTimetablesReponse from a JSON string
v3_dynamo_db_timetables_reponse_instance = V3DynamoDbTimetablesReponse.from_json(json)
# print the JSON string representation of the object
print(V3DynamoDbTimetablesReponse.to_json())

# convert the object into a dict
v3_dynamo_db_timetables_reponse_dict = v3_dynamo_db_timetables_reponse_instance.to_dict()
# create an instance of V3DynamoDbTimetablesReponse from a dict
v3_dynamo_db_timetables_reponse_from_dict = V3DynamoDbTimetablesReponse.from_dict(v3_dynamo_db_timetables_reponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


