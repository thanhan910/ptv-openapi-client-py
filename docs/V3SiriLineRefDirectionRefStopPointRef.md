# V3SiriLineRefDirectionRefStopPointRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_ref** | **str** | Siri LineRef | 
**direction_ref** | **int** | Siri DirectionRef  (in, out, up, down, clockwise, counterclockwise, Inbound, Outbound) | 
**stop_point_ref** | **int** | Siri StopPointRef | 

## Example

```python
from ptv_openapi_client.models.v3_siri_line_ref_direction_ref_stop_point_ref import V3SiriLineRefDirectionRefStopPointRef

# TODO update the JSON string below
json = "{}"
# create an instance of V3SiriLineRefDirectionRefStopPointRef from a JSON string
v3_siri_line_ref_direction_ref_stop_point_ref_instance = V3SiriLineRefDirectionRefStopPointRef.from_json(json)
# print the JSON string representation of the object
print(V3SiriLineRefDirectionRefStopPointRef.to_json())

# convert the object into a dict
v3_siri_line_ref_direction_ref_stop_point_ref_dict = v3_siri_line_ref_direction_ref_stop_point_ref_instance.to_dict()
# create an instance of V3SiriLineRefDirectionRefStopPointRef from a dict
v3_siri_line_ref_direction_ref_stop_point_ref_from_dict = V3SiriLineRefDirectionRefStopPointRef.from_dict(v3_siri_line_ref_direction_ref_stop_point_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


