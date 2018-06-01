
ANCHOR_FILE_PREFIX = 'configuration_anchor'
ANCHOR_VALIDATOR_SCRIPT = '/usr/share/xroad/scripts/verify_external_configuration.sh'
SUCCESS_STATUS = '0'
INTERNAL_CONF_ERROR_STATUS = '120'
CONFIGURATION_DOWNLOAD_FAIL_STATUS = '122'
CONFIGURATION_EXPIRED_STATUS = '123'
SIGNATURE_VALUE_FAILED_STATUS = '124'
OTHER_ERROR_STATUS = '125'
ANCHOR_GENERATED_AT_CSS = '#trusted_anchors_tab .anchor-generated_at'
UPLOAD_ANCHOR_BTN_ID = 'upload_trusted_anchor'
SAVE_ANCHOR_BTN_ID = 'save_trusted_anchor_ok'
TRUSTED_ANCHOR_BY_IDENTIFIER_XPATH = '//span[@class="box-title" and text()="{}"]'
INSTANCE_IDENTIFIER = 'ASD2'
DOWNLOAD_BTN_XPATH = '//button[text()="Download"]'
DELETE_BTN_XPATH = '//button[text()="Delete"]'
ANCHOR_HASH = '#trusted_anchors_tab .anchor-hash'
ANCHOR_HASH_REGEX = '([A-Z0-9]{2}:){27}[A-Z0-9]{2}'
GENERATED_AT_REGEX = 'UTC \d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'