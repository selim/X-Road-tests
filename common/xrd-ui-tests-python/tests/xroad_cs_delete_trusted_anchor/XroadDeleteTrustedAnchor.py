import unittest

from helpers import auditchecker
from main.maincontroller import MainController
from tests.xroad_cs_delete_trusted_anchor.delete_trusted_anchor import test_delete_trusted_anchor


class XroadDeleteTrustedAnchor(unittest.TestCase):
    """
    FED_07 Delete a Trusted Anchor
    RIA URL: https://jira.ria.ee/browse/XTKB-232
    Depends on finishing other test(s): FED_03
    Requires helper scenarios:
    X-Road version: 6.16.0
    """
    def __init__(self, methodName='test_a_delete_trusted_anchor_cancel'):
        unittest.TestCase.__init__(self, methodName)

    def test_a_delete_trusted_anchor_cancel(self):
        main = MainController(self)
        cs_host = main.config.get('cs.host')
        cs_user = main.config.get('cs.user')
        cs_pass = main.config.get('cs.pass')
        delete_trusted_anchor = test_delete_trusted_anchor(main, cancel=True)
        try:
            main.reload_webdriver(cs_host, cs_user, cs_pass)
            delete_trusted_anchor()
        except:
            main.save_exception_data()
            raise
        finally:
            main.tearDown()

    def test_b_delete_trusted_anchor(self):
        main = MainController(self)
        cs_host = main.config.get('cs.host')
        cs_user = main.config.get('cs.user')
        cs_pass = main.config.get('cs.pass')
        cs_ssh_host = main.config.get('cs.ssh_host')
        cs_ssh_user = main.config.get('cs.ssh_user')
        cs_ssh_pass = main.config.get('cs.ssh_pass')
        log_checker = auditchecker.AuditChecker(cs_ssh_host, cs_ssh_user, cs_ssh_pass)

        delete_trusted_anchor = test_delete_trusted_anchor(main, log_checker=log_checker)
        try:
            main.reload_webdriver(cs_host, cs_user, cs_pass)
            delete_trusted_anchor()
        except:
            main.save_exception_data()
            raise
        finally:
            main.tearDown()
