import subprocess

def run_nikto_command(target, options):
    command = ['nikto', '-host', target] + options
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

def get_nikto_commands():
    return {
        'Basic Scan': {
            'description': 'Perform a basic scan on the target.',
            'options': []
        },
        'Tuning (Interesting Files)': {
            'description': 'Scan for interesting files.',
            'options': ['-Tuning', '2']
        },
        'Tuning (Error Messages)': {
            'description': 'Scan for error messages.',
            'options': ['-Tuning', '4']
        },
        'Force SSL Mode': {
            'description': 'Force SSL mode on the port.',
            'options': ['-ssl']
        },
        'Update Plugins': {
            'description': 'Update the plugin files and database from CIRT.net.',
            'options': ['-update']
        },
        'Database Check': {
            'description': 'Check the plugin and database versions.',
            'options': ['-dbcheck']
        }
    }

