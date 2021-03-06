# -*- coding: utf-8 -*-
from QAutoLibrary.extension import TESTDATA
from selenium.webdriver.common.by import By
from QAutoLibrary.QAutoSelenium import *
from time import sleep
from pagemodel.ss_login import Ss_login
from pagemodel.ss_system_parameters import Ss_system_parameters
from pagemodel.ss_sidebar import Ss_sidebar
from pagemodel.ss_system_param_add_timestamp_dlg import Ss_system_param_add_timestamp_dlg
from pagemodel.open_application import Open_application

class Component_ss(CommonUtils):
    """
    Components common to security servers

    Changelog:

    * 11.07.2017
        | Documentation updated
    """
    ss_login = Ss_login()
    ss_system_parameters = Ss_system_parameters()
    ss_sidebar = Ss_sidebar()
    ss_system_param_add_timestamp_dlg = Ss_system_param_add_timestamp_dlg()
    open_application = Open_application()

    def login(self, section=u'security_server_url', initial_conf=False, wait_for_jquery=True):
        """
        Login to security server

        :param section:  Test data section name
        :param initial_conf:  If true server is in configurations state
        :param wait_for_jquery:  If true method waits for jquery
       """
        ## Go to security server
        self.open_application.open_application_url(TESTDATA[section])
        self.ss_login.login(TESTDATA[section], wait_for_jquery)
        if not initial_conf:
            self.ss_sidebar.verify_sidebar_title()

    def add_timestamping_url_to_ss(self, section=u'cs_url'):
        """
        Add timestamping url to security server

        :param section:  Test data section name
        """
        self.ss_system_parameters.click_button_id_tsp_add()
        sleep(3)
        self.ss_system_param_add_timestamp_dlg.click_trusted_tsp_first_row()
        sleep(3)
        self.ss_system_param_add_timestamp_dlg.click_button_ok()
        self.ss_system_parameters.verify_time_stamping_url(TESTDATA[section])

    def verify_login_fail(self, text=u'Authentication failed'):
        """
        Verify that login to security server fails

        :param text:  String value for text
        """
        self.ss_login.verify_contains_text(text)

    def delete_timestamping_url_from_ss(self, section=u'cs_url'):
        """
        Delete timestamping url from security server

        :param section:  Test data section name
        """
        self.wait_until_page_contains(TESTDATA[section][u'tsp_url'])
        self.ss_system_parameters.click_element_from_table_tsps_1(TESTDATA[section][u'tsp_url'])
        self.ss_system_parameters.click_button_id_tsp_delete()
