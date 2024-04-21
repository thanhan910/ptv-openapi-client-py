# coding: utf-8

"""
    PTV Timetable API - Version 3

    The PTV Timetable API provides direct access to Public Transport Victoria's public transport timetable data.    The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).    The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.    This Swagger is for Version 3 of the PTV Timetable API. By using this documentation you agree to comply with the licence and terms of service.    Train timetable data is updated daily, while the remaining data is updated weekly, taking into account any planned timetable changes (for example, due to holidays or planned disruptions). The PTV timetable API is the same API used by PTV for its apps. To access the most up to date data PTV has (including real-time data) you must use the API dynamically.    You can access the PTV Timetable API through a HTTP or HTTPS interface, as follows:        base URL / version number / API name / query string  The base URL is either:    *  http://timetableapi.ptv.vic.gov.au  or    *  https://timetableapi.ptv.vic.gov.au    The Swagger JSON file is available at http://timetableapi.ptv.vic.gov.au/swagger/docs/v3    Frequently asked questions are available on the PTV website at http://ptv.vic.gov.au/apifaq    Links to the following information are also provided on the PTV website at http://ptv.vic.gov.au/ptv-timetable-api/  * How to register for an API key and calculate a signature  * PTV Timetable API V2 to V3 Migration Guide  * PTV Timetable API Data Quality Statement    All information about how to use the API is in this documentation. PTV cannot provide technical support for the API.  

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ptv_openapi_client.models.v3_bulk_departures_update_response import V3BulkDeparturesUpdateResponse

class TestV3BulkDeparturesUpdateResponse(unittest.TestCase):
    """V3BulkDeparturesUpdateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V3BulkDeparturesUpdateResponse:
        """Test V3BulkDeparturesUpdateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V3BulkDeparturesUpdateResponse`
        """
        model = V3BulkDeparturesUpdateResponse()
        if include_optional:
            return V3BulkDeparturesUpdateResponse(
                departures = [
                    ptv_openapi_client.models.v3/departure.V3.Departure(
                        stop_id = 56, 
                        route_id = 56, 
                        run_id = 56, 
                        run_ref = '', 
                        direction_id = 56, 
                        disruption_ids = [
                            56
                            ], 
                        scheduled_departure_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        estimated_departure_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        at_platform = True, 
                        platform_number = '', 
                        flags = '', 
                        departure_sequence = 56, )
                    ],
                route_type = 56,
                stop_id = 56,
                requested_route_direction = ptv_openapi_client.models.v3/bulk_departures_route_direction_response.V3.BulkDeparturesRouteDirectionResponse(
                    route_id = '', 
                    direction_id = 56, 
                    direction_name = '', ),
                route_direction_status = 0,
                route_direction = ptv_openapi_client.models.v3/bulk_departures_route_direction_response.V3.BulkDeparturesRouteDirectionResponse(
                    route_id = '', 
                    direction_id = 56, 
                    direction_name = '', )
            )
        else:
            return V3BulkDeparturesUpdateResponse(
        )
        """

    def testV3BulkDeparturesUpdateResponse(self):
        """Test V3BulkDeparturesUpdateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
