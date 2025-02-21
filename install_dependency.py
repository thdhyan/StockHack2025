
def install_dependencies():
    import os
    os.system('pip install -r requirements.txt')
    print('All dependencies installed successfully!')

if __name__ == '__main__':    
    
    try:
        install_dependencies()
    except Exception as e:
        print('An error occurred while installing dependencies: ', e)
        raise e