# coding: utf-8

"""
    PTV Timetable API - Version 3

    The PTV Timetable API provides direct access to Public Transport Victoria's public transport timetable data.    The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).    The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.    This Swagger is for Version 3 of the PTV Timetable API. By using this documentation you agree to comply with the licence and terms of service.    Train timetable data is updated daily, while the remaining data is updated weekly, taking into account any planned timetable changes (for example, due to holidays or planned disruptions). The PTV timetable API is the same API used by PTV for its apps. To access the most up to date data PTV has (including real-time data) you must use the API dynamically.    You can access the PTV Timetable API through a HTTP or HTTPS interface, as follows:        base URL / version number / API name / query string  The base URL is either:    *  http://timetableapi.ptv.vic.gov.au  or    *  https://timetableapi.ptv.vic.gov.au    The Swagger JSON file is available at http://timetableapi.ptv.vic.gov.au/swagger/docs/v3    Frequently asked questions are available on the PTV website at http://ptv.vic.gov.au/apifaq    Links to the following information are also provided on the PTV website at http://ptv.vic.gov.au/ptv-timetable-api/  * How to register for an API key and calculate a signature  * PTV Timetable API V2 to V3 Migration Guide  * PTV Timetable API Data Quality Statement    All information about how to use the API is in this documentation. PTV cannot provide technical support for the API.  

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ptv_openapi_client.models.v3_siri_line_ref_mappings_response import V3SiriLineRefMappingsResponse

class TestV3SiriLineRefMappingsResponse(unittest.TestCase):
    """V3SiriLineRefMappingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V3SiriLineRefMappingsResponse:
        """Test V3SiriLineRefMappingsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V3SiriLineRefMappingsResponse`
        """
        model = V3SiriLineRefMappingsResponse()
        if include_optional:
            return V3SiriLineRefMappingsResponse(
                mapping_version = '',
                line_refs = {
                    'key' : ptv_openapi_client.models.v3/siri_line_ref_direction_refs_dictionary.V3.SiriLineRefDirectionRefsDictionary(
                        direction_refs = {
                            'key' : [
                                ptv_openapi_client.models.v3/siri_reference_data_detail.V3.SiriReferenceDataDetail(
                                    route_id = 56, 
                                    route_number_short = '', 
                                    direction_id = 56, 
                                    tracking_supplier_id = 56, 
                                    route_type = 56, )
                                ]
                            }, 
                        unmatched_direction_refs = {
                            'key' : ''
                            }, )
                    },
                status = ptv_openapi_client.models.v3/status.V3.Status(
                    version = '', 
                    health = 0, )
            )
        else:
            return V3SiriLineRefMappingsResponse(
        )
        """

    def testV3SiriLineRefMappingsResponse(self):
        """Test V3SiriLineRefMappingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
