# ExportTestNames
This script is recursively passes through all Python scripts (in unittest structure)
in provided paths and exports all classes and test names.

Usage:
1) Use Conf.py configuration file to set all paths you might want to analyze.
2) Run ExportTestCases.py file 

Output Example:

/home/ashtempl/PycharmProjects/designate-tempest-plugin/designate_tempest_plugin/tests/api/v2/test_blacklists.py
class BlacklistsAdminTest(BaseBlacklistsTest):
    def test_create_blacklist(self):
    def test_create_blacklist_invalid_pattern(self):
    def test_create_blacklist_huge_size_description(self):
    def test_create_blacklist_as_primary_fails(self):
    def test_show_blacklist(self):
    def test_delete_blacklist(self):
    def test_list_blacklists(self):
    def test_update_blacklist(self):
class TestBlacklistNotFoundAdmin(BaseBlacklistsTest):
    def test_show_blacklist_404(self):
    def test_update_blacklist_404(self):
    def test_delete_blacklist_404(self):
class TestBlacklistInvalidIdAdmin(BaseBlacklistsTest):
    def test_show_blacklist_invalid_uuid(self):
    def test_update_blacklist_invalid_uuid(self):
    def test_delete_blacklist_invalid_uuid(self):
