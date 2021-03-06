import unittest
from main.maincontroller import MainController
import ca_management


class XroadEditCa(unittest.TestCase):
    '''
    UC TRUST_09 Edit the Settings of a Certification Service
    RIA URL: https://jira.ria.ee/browse/XT-435, https://jira.ria.ee/browse/XTKB-68
    Depends on finishing other test(s): XroadAddCa
    Requires helper scenarios:
    X-Road version: 6.16.0
    '''
    def __init__(self, methodName='test_xroad_add_ca'):
        unittest.TestCase.__init__(self, methodName)

    def test_xroad_add_ca(self):
        main = MainController(self)

        # Set test name and number
        main.test_number = 'UC TRUST_09'
        main.test_name = self.__class__.__name__

        cs_host = main.config.get('cs.host')
        cs_user = main.config.get('cs.user')
        cs_pass = main.config.get('cs.pass')

        ca_name = main.config.get('ca.name')
        certificate_classpath = main.config.get('ca.profile_class')

        cs_ssh_host = main.config.get('cs.ssh_host')
        cs_ssh_user = main.config.get('cs.ssh_user')
        cs_ssh_pass = main.config.get('cs.ssh_pass')

        # Configure the service
        test_edit_ca = ca_management.test_edit_ca(case=main, ca_name=ca_name,
                                                  certificate_classpath=certificate_classpath, cs_ssh_host=cs_ssh_host,
                                                  cs_ssh_user=cs_ssh_user, cs_ssh_pass=cs_ssh_pass)
        try:
            # Open webdriver
            main.reload_webdriver(url=cs_host, username=cs_user, password=cs_pass)

            # Run the test
            test_edit_ca()
        except:
            main.log('XroadEditCa: Failed to edit CA')
            main.save_exception_data()
            assert False
        finally:
            # Test teardown
            main.tearDown()
