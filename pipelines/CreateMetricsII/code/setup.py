from setuptools import setup, find_packages
setup(
    name = 'DecisionPipeline',
    version = '1.0',
    packages = find_packages(include = ('createmetricsii*', )) + ["prophecy_config_instances"],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.22'],
    entry_points = {
'console_scripts' : [
'main = createmetricsii.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
