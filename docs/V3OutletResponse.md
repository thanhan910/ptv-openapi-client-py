# V3OutletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outlets** | [**List[V3Outlet]**](V3Outlet.md) | myki ticket outlets | [optional] 
**status** | [**V3Status**](V3Status.md) |  | [optional] 

## Example

```python
from ptv_openapi_client.models.v3_outlet_response import V3OutletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V3OutletResponse from a JSON string
v3_outlet_response_instance = V3OutletResponse.from_json(json)
# print the JSON string representation of the object
print(V3OutletResponse.to_json())

# convert the object into a dict
v3_outlet_response_dict = v3_outlet_response_instance.to_dict()
# create an instance of V3OutletResponse from a dict
v3_outlet_response_from_dict = V3OutletResponse.from_dict(v3_outlet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


