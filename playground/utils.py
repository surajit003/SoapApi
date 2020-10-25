def create_request_body_for_number_conversion(number):
    xml = """
       <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="tns:ns">
       <SOAP-ENV:Body>
        <NumberToDollars xmlns="http://www.dataaccess.com/webservicesserver/">
      <dNum>""" + number + """</dNum>
    </NumberToDollars>
        
       </SOAP-ENV:Body>
       </SOAP-ENV:Envelope>
       """

    return xml
