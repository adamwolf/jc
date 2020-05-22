import os
import json
import unittest
import jc.parsers.netstat

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTests(unittest.TestCase):

    def setUp(self):
        #
        # input
        #

        # netstat
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-l.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_l = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-l.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_l = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-p.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-p.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-sudo-lnp.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_sudo_lnp = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-sudo-lnp.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_sudo_lnp = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-sudo-aeep.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_sudo_aeep = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-sudo-aeep.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_sudo_aeep = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/netstat.out'), 'r', encoding='utf-8') as f:
            self.fedora32_netstat = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat.out'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-An.out'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_An = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-Abn.out'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_Abn = f.read()

        # netstat -r
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-r.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_r = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-rne.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_rne = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-rnee.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_rnee = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-r.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_r = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-rne.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_rne = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-rnee.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_rnee = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-r.out'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_r = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-rnl.out'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_rnl = f.read()

        # netstat -i
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-i.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_i = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-i.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_i = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-i.out'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_i = f.read()

        #
        # output
        #

        # netstat
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-l.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_l_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-l.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_l_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-p.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-p.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-sudo-lnp.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_sudo_lnp_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-sudo-lnp.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_sudo_lnp_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-sudo-aeep.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_sudo_aeep_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-sudo-aeep.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_sudo_aeep_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/netstat.json'), 'r', encoding='utf-8') as f:
            self.fedora32_netstat_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat.json'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-An.json'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_An_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-Abn.json'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_Abn_json = json.loads(f.read())

        # netsat -r
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-r.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_r_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-rne.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_rne_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-rnee.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_rnee_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-r.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_r_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-rne.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_rne_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-rnee.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_rnee_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-r.json'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_r_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-rnl.json'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_rnl_json = json.loads(f.read())

        # netstat -i
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/netstat-i.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_netstat_i_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/netstat-i.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_netstat_i_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/netstat-i.json'), 'r', encoding='utf-8') as f:
            self.osx_14_6_netstat_i_json = json.loads(f.read())

    def test_netstat_centos_7_7(self):
        """
        Test 'netstat' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat, quiet=True), self.centos_7_7_netstat_json)

    def test_netstat_ubuntu_18_4(self):
        """
        Test 'netstat' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat, quiet=True), self.ubuntu_18_4_netstat_json)

    def test_netstat_l_centos_7_7(self):
        """
        Test 'netstat -l' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_l, quiet=True), self.centos_7_7_netstat_l_json)

    def test_netstat_l_ubuntu_18_4(self):
        """
        Test 'netstat -l' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_l, quiet=True), self.ubuntu_18_4_netstat_l_json)

    def test_netstat_p_centos_7_7(self):
        """
        Test 'netstat -l' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_p, quiet=True), self.centos_7_7_netstat_p_json)

    def test_netstat_p_ubuntu_18_4(self):
        """
        Test 'netstat -l' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_p, quiet=True), self.ubuntu_18_4_netstat_p_json)

    def test_netstat_sudo_lnp_centos_7_7(self):
        """
        Test 'sudo netstat -lnp' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_sudo_lnp, quiet=True), self.centos_7_7_netstat_sudo_lnp_json)

    def test_netstat_sudo_lnp_ubuntu_18_4(self):
        """
        Test 'sudo netstat -lnp' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_sudo_lnp, quiet=True), self.ubuntu_18_4_netstat_sudo_lnp_json)

    def test_netstat_sudo_aeep_centos_7_7(self):
        """
        Test 'sudo netstat -aeep' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_sudo_aeep, quiet=True), self.centos_7_7_netstat_sudo_aeep_json)

    def test_netstat_sudo_aeep_ubuntu_18_4(self):
        """
        Test 'sudo netstat -aeep' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_sudo_aeep, quiet=True), self.ubuntu_18_4_netstat_sudo_aeep_json)

    def test_netstat_fedora32(self):
        """
        Test 'netstat' on Fedora32
        """
        self.assertEqual(jc.parsers.netstat.parse(self.fedora32_netstat, quiet=True), self.fedora32_netstat_json)

    def test_netstat_osx_16_4(self):
        """
        Test 'netstat' on OSX 16.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.osx_14_6_netstat, quiet=True), self.osx_14_6_netstat_json)

    def test_netstat_An_osx_16_4(self):
        """
        Test 'netstat -An' on OSX 16.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.osx_14_6_netstat_An, quiet=True), self.osx_14_6_netstat_An_json)

    def test_netstat_Abn_osx_16_4(self):
        """
        Test 'netstat -Abn' on OSX 16.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.osx_14_6_netstat_Abn, quiet=True), self.osx_14_6_netstat_Abn_json)

    def test_netstat_r_centos_7_7(self):
        """
        Test 'netstat -r' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_r, quiet=True), self.centos_7_7_netstat_r_json)

    def test_netstat_rne_centos_7_7(self):
        """
        Test 'netstat -rne' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_rne, quiet=True), self.centos_7_7_netstat_rne_json)

    def test_netstat_rnee_centos_7_7(self):
        """
        Test 'netstat -rnee' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_rnee, quiet=True), self.centos_7_7_netstat_rnee_json)

    def test_netstat_r_ubuntu_18_4(self):
        """
        Test 'netstat -r' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_r, quiet=True), self.ubuntu_18_4_netstat_r_json)

    def test_netstat_rne_ubuntu_18_4(self):
        """
        Test 'netstat -rne' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_rne, quiet=True), self.ubuntu_18_4_netstat_rne_json)

    def test_netstat_rnee_ubuntu_18_4(self):
        """
        Test 'netstat -rnee' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_rnee, quiet=True), self.ubuntu_18_4_netstat_rnee_json)

    def test_netstat_r_osx_16_4(self):
        """
        Test 'netstat -r' on OSX 16.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.osx_14_6_netstat_r, quiet=True), self.osx_14_6_netstat_r_json)

    def test_netstat_rnl_osx_16_4(self):
        """
        Test 'netstat -rnl' on OSX 16.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.osx_14_6_netstat_rnl, quiet=True), self.osx_14_6_netstat_rnl_json)

    def test_netstat_i_centos_7_7(self):
        """
        Test 'netstat -i' on Centos 7.7
        """
        self.assertEqual(jc.parsers.netstat.parse(self.centos_7_7_netstat_i, quiet=True), self.centos_7_7_netstat_i_json)

    def test_netstat_i_ubuntu_18_4(self):
        """
        Test 'netstat -i' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.ubuntu_18_4_netstat_i, quiet=True), self.ubuntu_18_4_netstat_i_json)

    def test_netstat_i_osx_16_4(self):
        """
        Test 'netstat -i' on OSX 16.4
        """
        self.assertEqual(jc.parsers.netstat.parse(self.osx_14_6_netstat_i, quiet=True), self.osx_14_6_netstat_i_json)


if __name__ == '__main__':
    unittest.main()
