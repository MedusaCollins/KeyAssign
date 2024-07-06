import subprocess

supportedLanguage = {
    'py': 'python',
    'js': 'node',
    'sh': 'bash',
}

def runPlugin(pluginPath):
    extension = pluginPath.split('.')[1]
    if extension in supportedLanguage:
        language = supportedLanguage[extension]
        subprocess.run([language, 'plugins/' + pluginPath])
    else:
        print(f"Unsupported file extension: {extension}")
