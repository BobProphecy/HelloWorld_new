from setuptools import setup, find_packages
setup(
    name = 'move_2_kenpei',
    version = '1.0',
    packages = find_packages(include = ('move_2_kenpei*', )) + ['prophecy_config_instances.move_2_kenpei'],
    package_dir = {'prophecy_config_instances.move_2_kenpei' : 'configs/resources/move_2_kenpei'},
    package_data = {'prophecy_config_instances.move_2_kenpei' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = move_2_kenpei.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
