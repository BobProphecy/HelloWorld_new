from setuptools import setup, find_packages
setup(
    name = 'schemachange',
    version = '1.0',
    packages = find_packages(include = ('schemachange*', )) + ['prophecy_config_instances.schemachange'],
    package_dir = {'prophecy_config_instances.schemachange' : 'configs/resources/schemachange'},
    package_data = {'prophecy_config_instances.schemachange' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = schemachange.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
