from ConfigParser import ConfigParser
from setuptools import setup


cfg = ConfigParser()
cfg.read('acsoo.cfg')


setup(
    version=cfg.get('acsoo', 'series') + '.' + cfg.get('acsoo', 'version'),
    name='odoo-addons-car',
    description='CAR '
                'Odoo instance customizations',
    setup_requires=['setuptools-odoo'],
    odoo_addons=True,
)