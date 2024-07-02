import subprocess

supportedLanguage = {
    'py': 'python',
    'js': 'node',
    'sh': 'bash',
}

def runScript(scriptPath):
    extension = scriptPath.split('.')[1]
    if extension in supportedLanguage:
        language = supportedLanguage[extension]
        subprocess.run([language, 'plugins/' + scriptPath])
    else:
        print(f"Unsupported file extension: {extension}")
